"""
Fortinet template groups client REST API wrapper
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)
from common.southbound.fortimanager.v1.models.fortimanager_template_groups import (
    TemplateGroup,
    TemplateScopeMember,
)

from .fortimanager import SBFortiManagerV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1List,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)


def create_template_group(
    client: SBFortiManagerV1, adom_name: str, template_group: TemplateGroup
) -> FortiManagerAPIResponseStatusV1:
    """

    Create a Template Group.
    API: ADD "pm/tmplgrp/adom/{ADOM_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[TemplateGroup](
        url=f"pm/tmplgrp/adom/{adom_name}", data=template_group
    )
    request = FortiManagerAPIRequestV1(
        method="add",
        params=[request_parameter],
    )
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def get_template_groups(
    client: SBFortiManagerV1, adom_name: str
) -> list[TemplateGroup]:
    """
    Select all Template groups for a given ADOM.
    API: GET "pm/tmplgrp/adom/{ADON_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/tmplgrp/adom/{adom_name}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[TemplateGroup], response)


def get_template_group(
    client: SBFortiManagerV1, adom_name: str, template_group_name: str
) -> TemplateGroup:
    """

    Selects, for a given ADOM, a specific Template Group by its name.
    API: GET "pm/tmplgrp/adom/{ADOM_NAME}/{TEMPLATE_GROUP_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/tmplgrp/adom/{adom_name}/{template_group_name}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(TemplateGroup, response)


def update_template_group(
    client: SBFortiManagerV1,
    adom_name: str,
    template_group_name: str,
    template_group: TemplateGroup,
) -> FortiManagerAPIResponseStatusV1:
    """

    Update a specific Template Group.
    Note: The "name" property cannot be updated because it acts like
    the internal ID of the entity.
    API: SET "pm/tmplgrp/adom/{ADOM_NAME}/{TEMPLATE_GROUP_NAME}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1[TemplateGroup](
        url=f"pm/tmplgrp/adom/{adom_name}/{template_group_name}", data=template_group
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def delete_template_group(
    client: SBFortiManagerV1,
    adom_name: str,
    template_group_name: str,
) -> FortiManagerAPIResponseStatusV1:
    """

    Delete a Template Group entry.
    API: DELETE "pm/tmplgrp/adom/{ADOM_NAME}/{TEMPLATE_GROUP_NAME}"
    """

    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/tmplgrp/adom/{adom_name}/{template_group_name}"
    )
    request = FortiManagerAPIRequestV1(method="delete", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def assign_template_group(
    client: SBFortiManagerV1,
    adom_name: str,
    template_group_name: str,
    devices: list[TemplateScopeMember],
) -> FortiManagerAPIResponseStatusV1:
    """

    Assign a template groups  to a device or a device group
    API: SET "pm/tmplgrp/adom/{ADOM_NAME}/{TEMPLATE_GROUP_NAME}/scope member"
    """

    request_parameter = FortiManagerAPIRequestParameterV1List[TemplateScopeMember](
        url=f"pm/tmplgrp/adom/{adom_name}/{template_group_name}scope member",
        data=devices,
    )
    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
