"""
Southbound FortiManager V1 Client
"""

import httpx

from common.errors import ErrorMessage
from common.southbound.fortimanager.v1.models.fortimanager_msp import FortiManagerMSPV1
from common.tools.tmf_logger import TMFLogger

from .messages import SBFortiManagerV1Messages as Messages
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestV1,
    UserCredentials,
)

logger = TMFLogger()


class SBFortiManagerV1:
    """
    FortiManager API Operations
    """

    OK_STATUS_CODE: int = 0
    AUTHENTICATION_ERROR_STATUS_CODE: int = -11
    LOGIN_ERROR_STATUS_CODE: int = -22
    LOGIN_ENDPOINT: str = "/sys/login/user"

    session_token: str | None = None
    msp: FortiManagerMSPV1 | None = None

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        verify_ssl: bool = True,
    ):
        """
        SBFortiManagerV1 Constructor
        Example for host (str): "https://<url>/" or "https://<url>"
        """

        self.host = host
        self.base_path = "jsonrpc" if self.host and self.host[-1] == "/" else "/jsonrpc"
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl

    def __str__(self):
        """Override string representation"""
        return f"SBFortiManagerV1(host={self.host}, username={self.username}"

    def __repr__(self):
        """Override repr string representation (used by str(list[SBFortiManagerV1])"""
        return self.__str__()

    def post_api(
        self,
        request: FortiManagerAPIRequestV1,
        respond_with_data=True,
        is_first_auth_call=True,
    ) -> dict:
        """
        Send the FortiManager API Request
        """
        if self.session_token is None:
            self.get_new_session_token()

        request.session = self.session_token or None

        response = httpx.post(
            url=self.host + self.base_path,
            json=request.dict(exclude_none=True, by_alias=True),
            verify=self.verify_ssl,
        ).json()

        status_code = response["result"][0]["status"]["code"]

        match status_code:
            case self.OK_STATUS_CODE:
                if respond_with_data:
                    return response["result"][0]["data"]
                return response
            case self.AUTHENTICATION_ERROR_STATUS_CODE:
                if is_first_auth_call:
                    self.get_new_session_token()
                    return self.post_api(request, is_first_auth_call=False)

                logger.log(
                    Messages.LOGIN_ERROR,
                    code=status_code,
                    message=response,
                    content=request.json(exclude_none=True),
                )
                raise httpx.HTTPError("FortiManager API Request Login Failed")
            case _:
                logger.log(
                    Messages.API_REQUEST_FAILED,
                    code=status_code,
                    message=response,
                    content=request.json(exclude_none=True),
                )
                message = self.get_error_message(status_code, response)
                raise httpx.HTTPError(message)

    def get_error_message(self, status_code, response):
        """
        Raises an HTTPError with the response message
        """
        result = response.get("result")
        message = ErrorMessage.UNKNOWN_ERROR.message
        if result is not None and len(result) > 0:
            for res in result:
                if (
                    res.get("status") is not None
                    and res.get("status").get("code") == status_code
                ):
                    message = res.get("status").get("message")

        return message

    def get_new_session_token(self) -> None:
        """
        Get new session token creating a new
        FortiManager Login Request and hitting the login api endpoint
        """
        login_request = FortiManagerAPIRequestV1(
            method="exec",
            params=[
                FortiManagerAPIRequestParameterV1[UserCredentials](
                    url=self.LOGIN_ENDPOINT,
                    data=UserCredentials(user=self.username, passwd=self.password),
                )
            ],
        )

        response = httpx.post(
            url=self.host + self.base_path,
            json=login_request.dict(exclude_none=True),
            verify=self.verify_ssl,
        ).json()

        if (session := response.get("session")) is not None:
            self.session_token = session
        else:
            logger.log(
                Messages.LOGIN_ERROR,
                status_code=response["result"][0]["status"]["code"],
            )

    def bind_to_msp(self, msp: FortiManagerMSPV1):
        """
        bind client to correct msp
        """
        self.msp = msp
