"""
Southbound interactions with the Meraki API
"""

from collections.abc import Callable
from typing import Final

from meraki import DashboardAPI
from meraki.config import DEFAULT_BASE_URL
from meraki.exceptions import APIError, APIKeyError, AsyncAPIError

from common.southbound.cisco_meraki import exceptions
from common.southbound.cisco_meraki.messages import MerakiMessages
from common.southbound.exceptions import SouthboundBaseError
from common.tools.tmf_logger import TMFLogger

logger = TMFLogger()


class SBMeraki:
    """
    Class to Abstract Setting up and doing Operations using the Meraki API
    """

    STATUS_CODE_TO_ERROR: Final[dict[str, type[SouthboundBaseError]]] = {
        "400": exceptions.BadRequestError,
        "401": exceptions.UnauthorizedError,
        "403": exceptions.ForbiddenError,
        "404": exceptions.NotFoundError,
        "429": exceptions.TooManyRequestsError,
        "500": exceptions.InternalServerError,
        "502": exceptions.InternalServerError,
        "503": exceptions.InternalServerError,
        "504": exceptions.InternalServerError,
    }

    def __init__(self, host: str | None, api_key: Callable[[], str] | str):
        if not api_key:
            raise ValueError("Meraki token not provided")

        if host:
            self.host = host
        else:
            self.host = DEFAULT_BASE_URL
        self.api_key = api_key
        if isinstance(api_key, str):
            self.__set_meraki_client(api_key)
        else:
            self.__set_meraki_client(api_key())

    def __set_meraki_client(self, api_key: str):
        # TODO-D: Tmp fix because all modules are not using TMFLogger yet (ex. workflow)
        try:
            supress_logging = logger.get_log_level() != "DEBUG"
        except AttributeError:
            supress_logging = False

        self._meraki_client = DashboardAPI(
            base_url=self.host,
            api_key=api_key,
            output_log=False,
            log_path="./logs/",
            print_console=True,
            maximum_retries=5,
            inherit_logging_config=True,
            retry_4xx_error=False,
            suppress_logging=supress_logging,
        )

    @property
    def api(self) -> DashboardAPI:
        """
        Get the Meraki Dashboard API

        Returns:
            meraki.DashboardAPI: the Meraki API
        """
        if isinstance(self.api_key, str):
            token = self.api_key
        else:
            token = self.api_key()

        # pylint: disable-next=protected-access
        if self._meraki_client._session._api_key != token:
            self.__set_meraki_client(token)
        return self._meraki_client

    @staticmethod
    def code_to_exception_mapping(status_code) -> type[SouthboundBaseError]:
        """Given an HTTP status code, return the appropiate exception type"""
        status_code = str(status_code) if status_code else ""
        return SBMeraki.STATUS_CODE_TO_ERROR.get(status_code, exceptions.UnknownError)

    @staticmethod
    def exception_handler(func: Callable):
        """
        Meraki API Exception Handler
        """

        def inner_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except APIKeyError as exc:
                logger.log(MerakiMessages.APIKEY_NOT_SET_ERROR)
                raise exceptions.NoAPIKeyError(
                    MerakiMessages.APIKEY_NOT_SET_ERROR.event
                ) from exc

            except (APIError, AsyncAPIError) as exc:
                logger.log(
                    MerakiMessages.MERAKI_UNSUPPORTED_OPERATION
                    if exc.status == 400
                    else MerakiMessages.MERAKI_RETURNED_ERROR,
                    error=str(exc),
                    message=exc.message,
                    status=exc.status,
                    operation=exc.operation,
                )
                exc_type = SBMeraki.code_to_exception_mapping(exc.status)
                raise exc_type(str(exc)) from None

        inner_function.__name__ = func.__name__
        inner_function.__module__ = func.__module__

        return inner_function
