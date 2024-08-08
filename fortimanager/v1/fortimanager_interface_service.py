"""
FortiManager Interface API Calls
pm/config/device/{device_name}/global/system/interface Endpoint
"""
# pylint: disable=line-too-long

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.fortimanager import SBFortiManagerV1
from common.southbound.fortimanager.v1.models.fortimanager_interface import (
    FortiManagerCreateVlanInterfaceV1,
    FortiManagerUpdateVlanInterfaceV1,
    FortiManagerVlanInterfaceV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)


def get_vlan_interfaces(
    client: SBFortiManagerV1, device_name: str
) -> list[FortiManagerVlanInterfaceV1]:
    """

    Select all device's vlan interfaces.
    API: GET "/system/interface"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device_name}/global/system/interface",
        filter=["type", "in", "vlan"],
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortiManagerVlanInterfaceV1], response)


def get_vlan_interface(
    client: SBFortiManagerV1,
    device_name: str,
    interface_name: str,
) -> FortiManagerVlanInterfaceV1:
    """

    Select a specific device's vlan interface by the sequence number.
    API: GET "/system/interface/{interface_name}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device_name}/global/system/interface/{interface_name}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerVlanInterfaceV1, response)


def add_vlan_interface(
    client: SBFortiManagerV1,
    interface: FortiManagerCreateVlanInterfaceV1,
    device_name: str,
):
    """
    Add a single FortiManager VLAN Interface
    API: POST "/system/interface"
    """
    request_parameter = FortiManagerAPIRequestParameterV1[
        FortiManagerCreateVlanInterfaceV1
    ](url=f"pm/config/device/{device_name}/global/system/interface", data=interface)
    request = FortiManagerAPIRequestV1(method="add", params=[request_parameter])
    response = client.post_api(request)
    return response


def update_vlan_interface(
    client: SBFortiManagerV1,
    device_name: str,
    interface_name: str,
    interface: FortiManagerUpdateVlanInterfaceV1,
):
    """

    Update an Interface.
    API: PUT "system/interface/{interface_name}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[
        FortiManagerUpdateVlanInterfaceV1
    ](
        url=f"pm/config/device/{device_name}/global/system/interface/{interface_name}",
        data=interface,
    )
    request = FortiManagerAPIRequestV1(method="update", params=[request_parameter])
    response = client.post_api(request)
    return response


def delete_interface(
    client: SBFortiManagerV1,
    device_name: str,
    interface_name: str,
) -> FortiManagerAPIResponseStatusV1:
    """

    Delete an Interface.
    API: DELETE "system/interface/{interface_name}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device_name}/global/system/interface/{interface_name}"
    )
    request = FortiManagerAPIRequestV1(method="delete", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
