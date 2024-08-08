"""
Fortinet System templates client REST API wrapper
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_system_templates import (
    CreateSystemTemplate,
    CreateSystemTemplateDNSWidget,
    FortinetSystemTemplate,
    ScopeMember,
    SystemTemplateDNSWidget,
    SystemTemplateEnabledSettings,
    UpdateSystemTemplate,
    UpdateSystemTemplateDNSWidget,
    UpdateSystemTemplateEnabledSettings,
)

from .fortimanager import SBFortiManagerV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1List,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)


def get_system_templates(
    client: SBFortiManagerV1, adom_name: str
) -> list[FortinetSystemTemplate]:
    """
    Select all System templates for a given ADOM.
    API: GET "pm/devprof/adom/{ADOM_NAME}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/devprof/adom/{adom_name}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortinetSystemTemplate], response)


def get_system_template(
    client: SBFortiManagerV1, adom_name: str, system_template_name: str
) -> FortinetSystemTemplate:
    """

    Selects, for a given ADOM, a specific System template by its name.
    API: GET "pm/devprof/adom/{ADOM_NAME}/{SYSTEM_TEMPLATE_NAME}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/devprof/adom/{adom_name}/{system_template_name}",
        meta_fields=["scope member", "description", "enabled options"],
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortinetSystemTemplate, response)


def get_system_template_available_pages(
    client: SBFortiManagerV1, adom_name: str, system_template_name: str
) -> SystemTemplateEnabledSettings:
    """

    Selects, for a given ADOM and System template the available
    configuration pages/options, ex. DNS, LOG, etc
    API: GET
    "pm/config/adom/{ADOM_NAME}/devprof/{SYSTEM_TEMPLATE_NAME}/device/profile/setting"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/adom/{adom_name}/devprof/{system_template_name}"
        "/device/profile/setting"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(SystemTemplateEnabledSettings, response)


def get_system_template_dns_settings(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
) -> list[SystemTemplateDNSWidget]:
    """

    Selects, for a given ADOM and System template the available
    DNS configuration list.
    The DNS configuration ID represents it sequence number.
    API: GET
    "pm/config/adom/{ADOM_NAME}/devprof/{SYSTEM_TEMPLATE_NAME}/
    device/template/widget/dns/action-list"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/adom/{adom_name}/devprof/{system_template_name}"
        f"/device/template/widget/dns/action-list"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[SystemTemplateDNSWidget], response)


def create_system_template(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template: CreateSystemTemplate,
) -> FortiManagerAPIResponseStatusV1:
    """

    Create a System template.
    API: ADD "/pm/devprof/adom/{ADOM_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[CreateSystemTemplate](
        url=f"/pm/devprof/adom/{adom_name}",
        data=system_template,
    )
    request = FortiManagerAPIRequestV1(method="add", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def create_system_template_dns_settings(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    system_template_dns_settings: CreateSystemTemplateDNSWidget,
) -> FortiManagerAPIResponseStatusV1:
    """

    Create a System template DNS settings configuration.
    API: SET "pm/config/adom/{ADOM_NAME}/devprof/{SYSTEM_TEMPLATE_NAME}}
    /device/template/widget/dns/action-list"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[
        CreateSystemTemplateDNSWidget
    ](
        url=f"pm/config/adom/{adom_name}/devprof/{system_template_name}"
        "/device/template/widget/dns/action-list",
        data=system_template_dns_settings,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def update_system_template(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    system_template: UpdateSystemTemplate,
) -> FortiManagerAPIResponseStatusV1:
    """

    Update a specific System template.
    Note: The "name" property cannot be updated because it acts like
    the internal ID of the entity.
    API: SET "/pm/devprof/adom/{ADOM_NAME}/{SYSTEM_TEMPLATE_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[UpdateSystemTemplate](
        url=f"/pm/devprof/adom/{adom_name}/{system_template_name}",
        data=system_template,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def update_system_template_available_pages(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    system_template: UpdateSystemTemplateEnabledSettings,
) -> FortiManagerAPIResponseStatusV1:
    """

    Update a specific System template's available setting options.
    API: SET "/pm/config/adom/{adom_name}/devprof/{system_template_name}
    /device/profile/setting"
    """

    req_param = FortiManagerAPIRequestParameterV1[UpdateSystemTemplateEnabledSettings](
        url=f"/pm/config/adom/{adom_name}/devprof/{system_template_name}"
        "/device/profile/setting",
        data=system_template,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[req_param])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def update_system_template_dns_settings(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    dns_setting_id: str,
    system_template_dns_settings: UpdateSystemTemplateDNSWidget,
) -> FortiManagerAPIResponseStatusV1:
    """

    Updates a System template DNS setting configuration.
    The DNS_SETTING_ID is representing by the setting's sequence number
    API: SET "pm/config/adom/{ADOM_NAME}/devprof/{SYSTEM_TEMPLATE_NAME}}
    /device/template/widget/dns/action-list/{DNS_SETTING_ID}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[
        UpdateSystemTemplateDNSWidget
    ](
        url=f"pm/config/adom/{adom_name}/devprof/{system_template_name}/"
        f"device/template/widget/dns/action-list/{dns_setting_id}",
        data=system_template_dns_settings,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def delete_system_template(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
) -> FortiManagerAPIResponseStatusV1:
    """

    Delete a System template entry.
    API: DELETE "pm/devprof/adom/{ADOM_NAME}/{SYSTEM_TEMPLATE_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/devprof/adom/{adom_name}/{system_template_name}"
    )
    request = FortiManagerAPIRequestV1(
        method="delete",
        params=[request_parameter],
    )
    response = client.post_api(request)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def assign_system_template(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    devices: list[ScopeMember],
) -> FortiManagerAPIResponseStatusV1:
    """

    Assign a System templates  to a device or a device group
    API: SET "/pm/devprof/adom/{ADOM_NAME}/{SYSTEM_TEMPLATE_NAME}/scope member"
    """

    request_parameter = FortiManagerAPIRequestParameterV1List[ScopeMember](
        url=f"/pm/devprof/adom/{adom_name}/{system_template_name}scope member",
        data=devices,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def remove_assigned_system_template(
    client: SBFortiManagerV1,
    adom_name: str,
    system_template_name: str,
    devices: list[ScopeMember],
) -> FortiManagerAPIResponseStatusV1:
    """

    Remove and assigned System templates from a device or a device group
    API: SET "/pm/devprof/adom/{ADOM_NAME}/{SYSTEM_TEMPLATE_NAME}/scope member"
    """

    request_parameter = FortiManagerAPIRequestParameterV1List[ScopeMember](
        url=f"/pm/devprof/adom/{adom_name}/{system_template_name}/scope member",
        data=devices,
    )
    request = FortiManagerAPIRequestV1(method="delete", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
