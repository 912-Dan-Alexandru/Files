"""
Wrapper class for SBVelocloud V1 and V2
"""

from collections.abc import Callable
from functools import wraps
from typing import Final, TypeVar
from typing_extensions import ParamSpec

import httpx

from common.models.velocloud.velocloud_version import VelocloudVersion
from common.southbound.exceptions import (
    ClientError,
    PermissionsError,
    RateLimitError,
    ResourceNotFoundError,
    ServerError,
    SouthboundBaseError,
    UnknownError,
)
from common.tools.tmf_logger import TMFLogger

from .enterprise import get_enterprise_id, get_enterprises, get_events
from .models import VeloEnterprise, VeloEventData
from .v1.velocloud import SBVelocloudV1
from .v2.velocloud import SBVelocloudV2

logger = TMFLogger()

P = ParamSpec("P")
T = TypeVar("T")
SDWAN_API_V2_BASEPATH = "api/sdwan/v2"


class SBVelocloud:
    """
    Generic class to manage SBVelocloud V1 and V2
    """

    STATUS_CODE_TO_ERROR: Final[dict[int, type[SouthboundBaseError]]] = {
        400: ClientError,
        401: PermissionsError,
        403: PermissionsError,
        404: ResourceNotFoundError,
        429: RateLimitError,
        500: ServerError,
        502: ServerError,
        503: ServerError,
        504: ServerError,
    }

    velocloud_api: SBVelocloudV1 | SBVelocloudV2
    version: VelocloudVersion = VelocloudVersion.UNKNOWN
    host: str

    def __init__(
        self,
        host: str,
        api_key: Callable[[], str],
        version: VelocloudVersion,
    ):
        """
        Initialization for SBVelocloud
        """
        if version == VelocloudVersion.V1:
            self.velocloud_api = SBVelocloudV1(host=host, api_key=api_key)
        elif version == VelocloudVersion.V2:
            host = host + SDWAN_API_V2_BASEPATH
            self.velocloud_api = SBVelocloudV2(
                host=host, api_key=api_key, base_path=SDWAN_API_V2_BASEPATH
            )

        self.version = version
        self.host = host

    @staticmethod
    def handle_exception(func: Callable[P, T]) -> Callable[P, T]:
        """
        Decorator to transform generic httpx exceptions into Southbound exceptions.
        """

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            """
            Wrapper function that handles the httpx exceptions
            """
            try:
                return func(*args, **kwargs)

            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
                error_cls = SBVelocloud.STATUS_CODE_TO_ERROR.get(
                    status_code, UnknownError
                )
                raise error_cls(
                    f"Error {status_code} in SBVelocloud: {exc.response.text}"
                ) from exc
            except httpx.RequestError as exc:
                raise ClientError(f"Request error in SBVelocloud: {exc!s}") from exc

        return wrapper

    @handle_exception
    def get_enterprises(self) -> list[VeloEnterprise]:
        """
        Function to get enterprises with get_enterprises
        """
        list_enterprises: list[VeloEnterprise] = []
        for ent in get_enterprises(self.velocloud_api):
            list_enterprises.append(VeloEnterprise(enterprise=ent))
        return list_enterprises

    @handle_exception
    def get_event_with_pagination(
        self, enterprise: VeloEnterprise, start_time: str, end_time: str
    ) -> list[VeloEventData]:
        """
        Wrapper of get_event including the pagination logic

        Args:
            enterprise_obj (VeloEnterprise): input generic type of enterprise
            start_time (str): start time used for get_event
            end_time (str): end time used for get_event

        Returns:
            list[VeloEventData]: VeloEventData that contain the list of data
        """
        enterprise_id: str = get_enterprise_id(enterprise.enterprise)
        all_events: list[VeloEventData] = []
        more_pages: bool = True
        next_page_link: str | None = None

        while more_pages:
            response = get_events(
                self.velocloud_api, enterprise_id, next_page_link, start_time, end_time
            )

            for event_data in response.data or []:
                all_events.append(VeloEventData(event_data=event_data))

            next_page_link = (
                response.metaData.nextPageLink if response.metaData else None
            )
            more_pages = response.metaData.more or False if response.metaData else False

        return all_events
