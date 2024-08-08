"""
Pydantic model representing a FortiManager/FortiOS IPsec Tunnel Template representation
"""

from enum import Enum

from pydantic import BaseModel, Field


class TemplateScopeMember(BaseModel):
    """
    A scope member of IPsec Tunnel Template (device or device group)
    to which the IPsec Tunnel Template is applied
    """

    name: str
    vdom: str = "root"


class TemplateType(str, Enum):
    """
    Types of template
    """

    TEMPLATE_IPSEC_TUNNEL = "template"


class TemplateSetting(BaseModel):
    """
    Template IPsec Tunnel settings
    """

    description: str | None = Field(
        description="Template ipsec tunnel description.",
        default=None,
    )
    option: str | None = Field(
        description="Template ipsec tunnel option.",
        default=None,
    )
    stype: str | None = Field(
        description="Template ipsec tunnel stype.",
    )
    widgets: list[str] = Field(
        description="Template ipsec tunnel widgets.",
        default=[],
    )


class FortinetIpsecTunnelTemplateV1(BaseModel, use_enum_values=True):
    """
    Pydantic representation of a Fortinet model used for
    IPsec Tunnels Template management operations
    """

    name: str = Field(
        description="Template ipsec tunnel name.",
    )
    oid: int | None = Field(
        description="Oid of a template ipsec tunnel.",
        default=None,
    )
    scope_member: TemplateScopeMember | None = Field(
        ...,
        description="Template ipsec tunnel scope member setting.",
        alias="scope member",
    )
    template_setting: TemplateSetting | None = Field(
        ...,
        description="Template ipsec tunnel setting.",
        alias="template setting",
    )
    type: TemplateType = Field(
        description="Template ipsec tunnel type.",
        default=TemplateType.TEMPLATE_IPSEC_TUNNEL,
    )
