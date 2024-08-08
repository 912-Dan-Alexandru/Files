"""
Mist V1 API Calls: MSP device stats
"""
from .mist import SBMistV1
from .models import MistDeviceStatsV1


def get_msp_site_device_stats(
    client: SBMistV1, site_id: str, device_type: str = "all", status: str = "all"
) -> list[MistDeviceStatsV1]:
    """
    API: GET /sites/:site_id/stats/devices
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    url = f"/sites/{site_id}/stats/devices?type={device_type}&status={status}"
    return client.get_api(url, list[MistDeviceStatsV1])


def get_msp_device_stats(
    client: SBMistV1, site_id: str, device_id: str
) -> MistDeviceStatsV1:
    """
    API: GET /sites/:site_id/stats/devices/:device_id
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    url = f"/sites/{site_id}/stats/devices/{device_id}"
    return client.get_api(url, MistDeviceStatsV1)
