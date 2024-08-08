"""
FortiOs Device API Calls
Include:
 * pm/config/device/{{DEVICE_NAME}}
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.models.fortimanager_dns import (
    FortiManagerDeviceSystemDnsV1,
    FortiManagerModifyDeviceSystemDnsV1,
)

from .fortimanager import SBFortiManagerV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)


def get_device_global_system_dns(
    client: SBFortiManagerV1,
    device_name: str,
) -> FortiManagerDeviceSystemDnsV1:
    """
    Get FortiManager device system dns info
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"/pm/config/device/{device_name}/global/system/dns"
    )

    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request=request)

    return evaluate_model(FortiManagerDeviceSystemDnsV1, response)


def update_device_global_system_dns(
    client: SBFortiManagerV1,
    device_name: str,
    data: FortiManagerModifyDeviceSystemDnsV1,
) -> None:
    """
    Modify FortiManager Device System DNS info
    """

    request_parameter = FortiManagerAPIRequestParameterV1[
        FortiManagerModifyDeviceSystemDnsV1
    ](url=f"/pm/config/device/{device_name}/global/system/dns", data=data)

    request = FortiManagerAPIRequestV1(method="update", params=[request_parameter])
    client.post_api(request=request, respond_with_data=False)
