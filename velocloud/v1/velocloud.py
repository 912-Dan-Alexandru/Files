"""
Southbound velocloud v1 client
"""

from collections.abc import Callable

import httpx
from structlog import get_logger

log = get_logger()


class SBVelocloudV1:
    """
    Velocloud V1 API Operations
    """

    def __init__(
        self,
        host: str,
        api_key: str | Callable,
        verify_ssl: bool = True,
        vco_index: int = 1,
    ):
        if not api_key:
            raise ValueError("Velocloud token not provided")

        self.host = host
        self.api_key = api_key
        self.base_path = "portal/rest" if self.host[-1] == "/" else "/portal/rest"
        self.verify_ssl = verify_ssl
        self.vco_index = vco_index

    def __str__(self):
        """Override string representation"""
        return (
            f"SBVelocloudV1(host={self.host}, api_key=****, "
            f"verify_ssl={self.verify_ssl}, vco=vco{self.vco_index})"
        )

    def __repr__(self):
        """Override repr string representation (used by str(list[SBVelocloudV1])"""
        return self.__str__()

    def post_api(self, endpoint, body=None):
        """
        Get Request for API
        """
        if isinstance(self.api_key, str):
            token = self.api_key
        else:
            token = self.api_key()

        headers = {"Authorization": f"Token {token}"}
        request = httpx.Request(
            "POST",
            self.host + self.base_path + endpoint,
            headers=headers,
            json=body,
        )
        client = httpx.Client()
        response = client.send(request)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            log.error(
                "Failed to Fetch",
                code=exc.response.status_code,
                url=exc.response.url,
                data=exc.response.text,
                body=body,
            )
        response_json = response.json()
        if isinstance(response_json, dict) and response_json.get("error") is not None:
            error_message = response_json.get("error", {}).get("message")
            log.critical(
                "Error Querying Velocloud API",
                message=error_message,
                request_data=body,
            )
            nested_error_messages = self._format_error_message(response_json)
            raise httpx.HTTPError(
                f"Velocloud API Returned Error: {error_message} {nested_error_messages}"
            )
        return response_json

    @staticmethod
    def _format_error_message(json: dict):
        """format the nested error messages into a string"""
        error_message = json.get("error", {}).get("message", "")
        nested_error_messages = [
            res["message"]
            for res in json.get("error", {}).get("data", {}).get("error", [{}])
            if res.get("message")
        ]
        if nested_error_messages:
            return error_message + ": " + "; ".join(nested_error_messages)
        return error_message
