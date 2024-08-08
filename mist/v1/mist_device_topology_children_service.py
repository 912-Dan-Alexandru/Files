"""
Mist V1 API Calls: MSP site
"""
from .mist import SBMistV1
from .models import MistDeviceTopologyChildrenV1


def get_mist_device_topology_children(
    client: SBMistV1, site_id: str, device_mac: str
) -> MistDeviceTopologyChildrenV1:
    """
    API: /labs/sites/{{site_id}}/device/{{device_mac}}/topology_children
    Raises:
        `httpx.HTTPError`
        `pydantic.ValidationError`
    """
    return client.get_api(
        f"/labs/sites/{site_id}/device/{device_mac}/topology_children",
        MistDeviceTopologyChildrenV1,
    )
