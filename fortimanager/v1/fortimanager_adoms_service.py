"""
FortiManager ADOMs API Calls
/dvmdb/adom Endpoint
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)
from common.southbound.fortimanager.v1.models.policy_package import (
    FolderWithPolicyPkgs,
    PolicyPackage,
)

from .fortimanager import SBFortiManagerV1
from .models.fortimanager_adom import (
    CreateFortiManagerADOMV1,
    FortiManagerADOMV1,
    UpdateFortiManagerADOMV1,
)
from .models.fortimanager_device import (
    FortiManagerDeviceV1,
    FortiManagerLicenses,
    FortiManagerModifyDeviceV1,
)
from .models.fortimanager_device_group import FortiManagerDeviceGroupV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)

VF_SDWAN_SERVICE_PROVIDED = "VF SDWAN Service Provided"
OPCO_NAME = "VF OpCo Name"
VF_CUSTOMER_ID = "VF Customer ID"
VF_3C_REF = "VF 3C Ref"
ADDRESS = "Address"
CONTACT_EMAIL = "Contact Email"
CONTACT_PHONE_NUMBER = "Contact Phone Number"
VF_ORDER_REF = "VF Order Ref"
ADOM_URL = "/dvmdb/adom"
META_FIELDS = [VF_SDWAN_SERVICE_PROVIDED, OPCO_NAME, VF_CUSTOMER_ID]


def get_adoms(client: SBFortiManagerV1) -> list[FortiManagerADOMV1]:
    """
    Get all FortiManager ADOMs
    API: POST "/dvmdb/adom"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=ADOM_URL, meta_fields=META_FIELDS
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortiManagerADOMV1], response)


def get_adom_device_groups(
    client: SBFortiManagerV1, adom_name: str
) -> list[FortiManagerDeviceGroupV1]:
    """
    Get FortiManager DevicesGroups by ADOM name
    API: POST "/dvmdb/adom/{adom_name}/group"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"{ADOM_URL}/{adom_name}/group"
    )

    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortiManagerDeviceGroupV1], response)


def get_adom_devices(
    client: SBFortiManagerV1, adom_name: str
) -> list[FortiManagerDeviceV1]:
    """
    Get FortiManager Devices by ADOM name
    API: POST "/dvmdb/adom/{adom_name}/device"
    """

    meta_fields = [
        VF_3C_REF,
        ADDRESS,
        CONTACT_EMAIL,
        CONTACT_PHONE_NUMBER,
        VF_ORDER_REF,
    ]
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"/dvmdb/adom/{adom_name}/device", meta_fields=meta_fields
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortiManagerDeviceV1], response)


def get_device(
    client: SBFortiManagerV1, adom_name: str, device_name: str
) -> FortiManagerDeviceV1:
    """
    Get FortiManager Device info by ADOM name
    API: POST "/dvmdb/adom/{adom_name}/device"
    """

    meta_fields = [
        VF_3C_REF,
        ADDRESS,
        CONTACT_EMAIL,
        CONTACT_PHONE_NUMBER,
        VF_ORDER_REF,
    ]
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"/dvmdb/adom/{adom_name}/device/{device_name}", meta_fields=meta_fields
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerDeviceV1, response)


def modify_adom_devices(
    client: SBFortiManagerV1,
    adom_name: str,
    device_name: str,
    device_data: FortiManagerModifyDeviceV1,
) -> FortiManagerModifyDeviceV1:
    """
    Modify a device from an ADOM
    API: POST "/dvmdb/adom/{adom_name}/device/{device_name}"
    """

    meta_fields = [
        VF_3C_REF,
        ADDRESS,
        CONTACT_EMAIL,
        CONTACT_PHONE_NUMBER,
        VF_ORDER_REF,
    ]

    request_parameter = FortiManagerAPIRequestParameterV1[FortiManagerModifyDeviceV1](
        url=f"/dvmdb/adom/{adom_name}/device/{device_name}",
        meta_fields=meta_fields,
        data=device_data,
    )

    request = FortiManagerAPIRequestV1(method="update", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerModifyDeviceV1, response)


def get_license_info(client: SBFortiManagerV1) -> list[FortiManagerLicenses]:
    """
    Get FortiManager license info
    API: POST "/um/misc/dump_contract"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url="/um/misc/dump_contract"
    )

    request = FortiManagerAPIRequestV1(method="exec", params=[request_parameter])
    response = client.post_api(request)["contract"]

    return evaluate_model(list[FortiManagerLicenses], response)


def get_adom_folders_and_policy_packages(
    client: SBFortiManagerV1, adom_name: str
) -> list[PolicyPackage | FolderWithPolicyPkgs]:
    """
    Get FortiManager folders and policy packages by ADOM name
    API: POST "/pm/pkg/adom/{adom_name}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"/pm/pkg/adom/{adom_name}"
    )

    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[PolicyPackage | FolderWithPolicyPkgs], response)


def get_adom_folder_or_policy_package(
    client: SBFortiManagerV1, adom_name: str, directory: list[str]
) -> PolicyPackage | FolderWithPolicyPkgs:
    """
    Get FortiManager folder or policy package by ADOM name
    API: POST "/pm/pkg/adom/{adom_name}/{tree_path}"
    """
    tree_path = "/".join(directory)
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"/pm/pkg/adom/{adom_name}/{tree_path}"
    )

    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(PolicyPackage, response)


def add_adom_folder_or_policy_package(
    client: SBFortiManagerV1,
    adom_name: str,
    directory: list[str],
    policy_package_or_folder: PolicyPackage | FolderWithPolicyPkgs,
) -> FortiManagerAPIResponseStatusV1:
    """
    add FortiManager folder or policy package by ADOM name
    API: POST "/pm/pkg/adom/{adom_name}{tree_path}"
    """
    tree_path: str = ("/" if directory else "") + "/".join(directory)
    request_parameter = FortiManagerAPIRequestParameterV1[
        PolicyPackage | FolderWithPolicyPkgs
    ](
        url=f"/pm/pkg/adom/{adom_name}{tree_path}",
        data=policy_package_or_folder,
    )
    request = FortiManagerAPIRequestV1(method="add", params=[request_parameter])
    response = client.post_api(request, False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def update_adom_folder_or_policy_package(
    client: SBFortiManagerV1,
    adom_name: str,
    directory: list[str],
    policy_package_or_folder: PolicyPackage | FolderWithPolicyPkgs,
) -> FortiManagerAPIResponseStatusV1:
    """
    update FortiManager folder or policy package by ADOM name
    API: POST "/pm/pkg/adom/{adom_name}{tree_path}"
    """
    tree_path = "/".join(directory)
    request_parameter = FortiManagerAPIRequestParameterV1[
        PolicyPackage | FolderWithPolicyPkgs
    ](url=f"/pm/pkg/adom/{adom_name}/{tree_path}", data=policy_package_or_folder)

    request = FortiManagerAPIRequestV1(method="update", params=[request_parameter])
    response = client.post_api(request, False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def add_adom(
    client: SBFortiManagerV1, adom_payload: CreateFortiManagerADOMV1
) -> FortiManagerADOMV1:
    """
    Add a single FortiManager ADOM
    API: POST "/dvmdb/adom"
    """
    request_parameter = FortiManagerAPIRequestParameterV1[CreateFortiManagerADOMV1](
        url=ADOM_URL, data=adom_payload
    )
    request = FortiManagerAPIRequestV1(method="add", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerADOMV1, response)


def get_adom(client: SBFortiManagerV1, name: str) -> FortiManagerADOMV1:
    """
    Get a sinle FortiManager ADOM by name
    API: POST "/dvmdb/adom/{adom}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url="/dvmdb/adom/" + name, meta_fields=META_FIELDS
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerADOMV1, response)


def update_adom(
    client: SBFortiManagerV1, to_add: UpdateFortiManagerADOMV1
) -> FortiManagerADOMV1:
    """
    Updates a single FortiManager ADOM
    API: POST "/dvmdb/adom"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[UpdateFortiManagerADOMV1](
        url=ADOM_URL, data=to_add
    )
    request = FortiManagerAPIRequestV1(method="update", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerADOMV1, response)


def delete_adom(client: SBFortiManagerV1, name: str) -> FortiManagerAPIResponseStatusV1:
    """
    Deletes a FortiManager ADOM by its name
    API: DELETE "/dvmdb/adom/{adom}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url="/dvmdb/adom/" + name, meta_fields=META_FIELDS
    )
    request = FortiManagerAPIRequestV1(method="delete", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
