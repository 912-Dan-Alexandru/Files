"""
FortiManager DHCPs API Calls
pm/config/device/{device_name}/vdom/{vdom_name}/system/dhcp/server Endpoint
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.fortimanager import SBFortiManagerV1
from common.southbound.fortimanager.v1.models.fortimanager_dhcp_server import (
    CreateFortiManagerDHCPServerV1,
    FortiManagerDHCPServerV1,
    UpdateFortiManagerDHCPServerV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)

DEVICE_API = "pm/config/device"
ENDPOINT = "vdom/root/system/dhcp/server"


def get_device_dhcp_servers(
    client: SBFortiManagerV1, device_name: str
) -> list[FortiManagerDHCPServerV1]:
    """

    Select all device's DHCP servers entries.
    API: GET "/system/dhcp/server"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"{DEVICE_API}/{device_name}/{ENDPOINT}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortiManagerDHCPServerV1], response)


def get_device_dhcp_server(
    client: SBFortiManagerV1,
    device_name: str,
    dhcp_server_id: int,
) -> FortiManagerDHCPServerV1:
    """

    Select a specific device's DHCP servers entry by the
    entry's sequence number.
    API: GET "/system/dhcp/server/{dhcp_server_id}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"{DEVICE_API}/{device_name}/{ENDPOINT}/{dhcp_server_id}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerDHCPServerV1, response)


def add_device_dhcp_server(
    client: SBFortiManagerV1,
    dhcp_server: CreateFortiManagerDHCPServerV1,
    device_name: str,
) -> dict:
    """
    Add a single FortiManager DHCP Server
    API: POST "pm/config/device/{device_name}/vdom/{vdom_name}/system/dhcp/server"
    """
    request_parameter = FortiManagerAPIRequestParameterV1[
        CreateFortiManagerDHCPServerV1
    ](url=f"{DEVICE_API}/{device_name}/{ENDPOINT}", data=dhcp_server)
    request = FortiManagerAPIRequestV1(method="add", params=[request_parameter])
    response = client.post_api(request)
    return response


def update_device_dhcp_server(
    client: SBFortiManagerV1,
    device_name: str,
    dhcp_server: UpdateFortiManagerDHCPServerV1,
    dhcp_server_id: int,
) -> dict:
    """

    Update a DHCP Server.
    API: PUT "pm/config/device/{device_name}/vdom/{vdom_name}/system/dhcp/server"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[
        UpdateFortiManagerDHCPServerV1
    ](url=f"{DEVICE_API}/{device_name}/{ENDPOINT}/{dhcp_server_id}", data=dhcp_server)

    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request)
    return response


def delete_device_dhcp_server(
    client: SBFortiManagerV1,
    device_name: str,
    dhcp_server_id: int,
) -> FortiManagerAPIResponseStatusV1:
    """

    Delete a DHCP Server.
    API: DELETE
    "pm/config/device/{device_name}
        /vdom/{vdom_name}/system/dhcp/server/{dhcp_server_id}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"{DEVICE_API}/{device_name}/{ENDPOINT}/{dhcp_server_id}"
    )
    request = FortiManagerAPIRequestV1(method="delete", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
