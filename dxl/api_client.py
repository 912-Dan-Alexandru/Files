"""
APIClient
"""

import json
import uuid
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile

import httpx
from httpx import (
    AsyncClient,
    AsyncHTTPTransport,
    Client,
    HTTPStatusError,
    HTTPTransport,
)
from httpx._client import UseClientDefault
from httpx._types import AuthTypes
from pydantic import AnyHttpUrl
from structlog import get_logger

from . import models

DEFAULT_TIMEOUT: float = 30.0


def handle_request_errors(api_calling_func):
    """
    Exception Handling Decorator
    """

    def decorated_func(self, *args, **kwargs):
        try:
            return api_calling_func(self, *args, **kwargs)
        except json.decoder.JSONDecodeError as exception:
            self.log.error("Error Parsing Response Data as JSON", exc_info=True)
            raise exception
        except httpx.HTTPError as http_exception:
            self.log.error("Error Making Request", exc_info=True)
            raise http_exception

    return decorated_func


class APIClient:
    """
    API Client
    """

    def __init__(
        self,
        endpoint: AnyHttpUrl | None,
        mutual_ssl: models.MutualSSLConfig | None = None,
        auth: models.AuthConfig | None = None,
        dxl: models.DXLConfig | None = None,
        retries: int = 3,
    ):
        self.endpoint = endpoint
        self.mutual_ssl = mutual_ssl
        self.mutual_ssl_config = self.generate_cert_files()
        self.auth = auth
        self.dxl = dxl
        self.token_data: models.TokenResponse | None = None
        self.log = get_logger()
        self.base_transport = HTTPTransport(
            retries=retries, cert=self.mutual_ssl_config
        )
        self.async_transport = AsyncHTTPTransport(
            retries=retries, cert=self.mutual_ssl_config
        )

    def generate_cert_files(self):
        """
        httpx library requires certificates to be files
        To be able to store certs as secrets this load strings and convert to files
        """
        if self.mutual_ssl is not None:
            with (
                NamedTemporaryFile(mode="w+b", delete=False) as cert_file,
                NamedTemporaryFile(mode="w+b", delete=False) as private_key_file,
            ):
                cert_file.write(self.mutual_ssl.cert_public.encode("utf-8"))
                cert_file.seek(0)

                private_key_file.write(self.mutual_ssl.cert_private.encode("utf-8"))
                private_key_file.seek(0)

                return (
                    f"{ cert_file.name }",
                    f"{ private_key_file.name }",
                    self.mutual_ssl.cert_passphrase,
                )
        return None

    def request_headers(self, transaction_id):
        """
        Returns a dict containing the authentication headers
        """
        if self.token_data is None:
            self.log.debug("OAuth Token is not Available")
            token = None
        else:
            token = self.token_data.access_token
        if self.dxl is not None:
            headers = {
                "x-source-system": self.dxl.x_source_system,
                "x-destination-system": self.dxl.x_destination_system,
                "x-route-info": self.dxl.x_route_info,
                "x-transaction-id": transaction_id,
                "Authorization": f"Bearer {token}",
            }
        else:
            headers = {
                "x-transaction-id": transaction_id,
                "Authorization": f"Bearer {token}",
            }
        response = models.RequestHeaders(**headers)
        return response.dict(by_alias=True, exclude_none=True)

    def check_token(self):
        """
        Check if the token is valid and if not renew it
        """
        if self.token_data is None:
            return False
        issued_at = datetime.utcfromtimestamp(int(self.token_data.issued_at) / 1000)
        expires_in_delta = timedelta(seconds=int(self.token_data.expires_in))
        token_valid = datetime.utcnow() < issued_at + expires_in_delta

        if token_valid is True:
            self.log.info("Token is is still valid", issued_at=issued_at)
            return True
        return False

    def get_auth(self) -> AuthTypes | UseClientDefault:
        """
        Get Auth data for API calls
        """
        if self.auth is not None and self.auth.basic is not None:
            return (self.auth.basic.username, self.auth.basic.password)
        return UseClientDefault()

    @handle_request_errors
    def authenticate_endpoint(self):
        """
        Authenticate against DXL
        """

        if (
            self.auth is not None
            and self.auth.type.value == models.AuthTypes.OAUTH
            and self.auth.oauth is not None
        ):
            if self.check_token():
                return
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = models.AuthBody(
                client_id=self.auth.oauth.client_id,
                client_secret=self.auth.oauth.client_secret,
                scope=self.auth.oauth.scope,
                grant_type="client_credentials",
            ).dict()

            response = httpx.post(
                url=self.auth.oauth.token_endpoint,
                headers=headers,
                cert=self.mutual_ssl_config,
                data=data,
            )
            try:
                response.raise_for_status()
                self.token_data = models.TokenResponse(**response.json())
            except HTTPStatusError as http_error:
                self.error_handler(response, http_error)
        self.log.debug("Not Using Authentication")

    @handle_request_errors
    def request_get(self, resource):
        """
        Make a GET request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        headers = self.request_headers(transaction_id=str(uuid.uuid4()))
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        with Client(transport=self.base_transport, timeout=DEFAULT_TIMEOUT) as client:
            response = client.get(
                request_url, headers=headers, auth=auth_data, follow_redirects=True
            )
        response.raise_for_status()
        return response

    @handle_request_errors
    def request_post(self, resource, data):
        """
        Make a POST Request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        headers = self.request_headers(transaction_id=str(uuid.uuid4()))
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        with Client(transport=self.base_transport, timeout=DEFAULT_TIMEOUT) as client:
            response = client.post(
                url=request_url,
                headers=headers,
                auth=auth_data,
                json=data,
            )
        response.raise_for_status()
        return response

    async def async_request_get(self, resource):
        """
        Make a async GET request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        headers = self.request_headers(transaction_id=str(uuid.uuid4()))
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        async with AsyncClient(
            transport=self.async_transport, timeout=DEFAULT_TIMEOUT
        ) as client:
            response = await client.get(request_url, headers=headers, auth=auth_data)
        response.raise_for_status()
        return response

    async def async_request_post(self, resource, data):
        """
        Make a async POST Request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        transaction_id = str(uuid.uuid4())
        headers = self.request_headers(transaction_id=transaction_id)
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        async with AsyncClient(
            transport=self.async_transport, timeout=DEFAULT_TIMEOUT
        ) as client:
            response = await client.post(
                url=request_url,
                auth=auth_data,
                headers=headers,
                json=data,
            )
        response.raise_for_status()
        self.log.info(
            "Sent Message to next component.",
            status_code=response.status_code,
            url=resource,
            auth_type=self.auth.type if self.auth else None,
            x_transaction_id=transaction_id,
        )
        return response

    async def async_request_patch(self, resource, data):
        """
        Make a async PATCH Request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        transaction_id = str(uuid.uuid4())
        headers = self.request_headers(transaction_id=transaction_id)
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        async with AsyncClient(
            transport=self.async_transport, timeout=DEFAULT_TIMEOUT
        ) as client:
            response = await client.patch(
                url=request_url,
                auth=auth_data,
                headers=headers,
                json=data,
            )
        response.raise_for_status()
        self.log.info(
            "Sent Message to next component.",
            status_code=response.status_code,
            url=resource,
            auth_type=self.auth.type if self.auth else None,
            x_transaction_id=transaction_id,
        )
        return response

    @handle_request_errors
    def request_delete(self, resource):
        """
        Make a Delete Request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        headers = self.request_headers(transaction_id=str(uuid.uuid4()))
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        with Client(transport=self.base_transport, timeout=DEFAULT_TIMEOUT) as client:
            response = client.delete(
                url=request_url,
                headers=headers,
                auth=auth_data,
            )
        response.raise_for_status()
        return response

    @handle_request_errors
    def request_patch(self, resource, data):
        """
        Make a PATCH Request
        """
        if not self.check_token():
            self.authenticate_endpoint()
        headers = self.request_headers(transaction_id=str(uuid.uuid4()))
        request_url = self.endpoint + resource
        auth_data = self.get_auth()
        with Client(transport=self.base_transport, timeout=DEFAULT_TIMEOUT) as client:
            response = client.patch(
                url=request_url,
                headers=headers,
                auth=auth_data,
                json=data,
            )
        response.raise_for_status()
        return response

    def error_handler(self, response, http_error):
        """
        Method to handle connection errors
        """
        error_type = response.json().get("error", "")
        error_description = response.json().get("error_description", "")
        if error_type == "invalid_scope":
            self.log.error(
                "Missing or invalid scope",
                error_description=error_description,
                exc_info=True,
            )
        elif error_type == "invalid_client":
            self.log.error(
                "Invalid client", error_description=error_description, exc_info=True
            )
        elif error_type == "server_error":
            self.log.error(
                "Server error", error_description=error_description, exc_info=True
            )
        else:
            self.log.error(
                "Unknown error", error_description=error_description, exc_info=True
            )
        raise http_error
