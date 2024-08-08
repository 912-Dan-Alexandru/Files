"""
Pydantic model representing a FortiManager/FortiOS static route template representation
"""
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class TemplateScopeMember(BaseModel):
    """
    A scope member of static route template (device or device group)
    to which the static route template is applied
    """

    name: str
    vdom: str = "root"


class TemplateType(str, Enum):
    """
    Types of template
    """

    TEMPLATE_STATIC_ROUTE = "template"


class TemplateSetting(BaseModel):
    """
    Template static route settings
    """

    description: str | None = Field(
        description="Template Static Route description.",
        default=None,
    )
    option: Any | None
    stype: str | None = Field(
        description="Template Static Route stype.",
    )
    widgets: list[str] | None = Field(
        description="Template Static Route widgets.",
        default=[],
    )


class FortinetStaticRouteTemplate(BaseModel, use_enum_values=True):
    """
    Pydantic representation of a Fortinet model used for
    static routes template management operations
    """

    name: str = Field(
        description="Template Static Route name.",
    )
    oid: int | None = Field(
        description="Oid of a template static route.",
        default=None,
    )
    scope_member: TemplateScopeMember | None = Field(
        ...,
        description="Template static route scope member setting.",
        alias="scope member",
    )
    template_setting: TemplateSetting | None = Field(
        ...,
        description="Template static route setting.",
        alias="template setting",
    )
    type: TemplateType = TemplateType.TEMPLATE_STATIC_ROUTE
