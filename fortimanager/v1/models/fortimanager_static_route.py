"""
Pydantic model representing a FortiManager/FortiOS static route representation
"""

from enum import Enum

from pydantic import BaseModel, Field


class State(str, Enum):
    """
    Fortinet generic configuration state
    """

    DISABLE = "disable"
    ENABLE = "enable"


class SdwanZoneItem(BaseModel):
    """
    Fortinet SD-WAN zone item
    """

    name: str


class FortinetStaticRouteBase(BaseModel, use_enum_values=True):
    """
    Pydantic representation of a Fortinet model used for
    static routes management operations
    """

    bfd: State | None = Field(
        description="Enable/disable Bidirectional Forwarding Detection (BFD).",
        default=None,
    )
    blackhole: State | None = Field(
        description="Enable/disable blackhole route",
        default=None,
    )
    comment: str | None = Field(
        description="Optional comments.",
        max_length=255,
        default=None,
    )
    device: str | list[str] | None = Field(
        description="Gateway out interface or tunnel.",
        default=None,
    )
    distance: int | None = Field(
        description="Administrative distance (1 - 255).",
        ge=1,
        le=255,
        default=None,
    )
    dst: list[str] | str | None = Field(
        description="Destination IP and mask for this route.",
        default=None,
    )
    dstaddr: list[str] | str | None = Field(
        description="Name of firewall address or address group.",
        max_length=79,
        default=None,
    )
    dynamic_gateway: State | None = Field(
        alias="dynamic-gateway",
        description=(
            "Enable use of dynamic gateway retrieved from a DHCP or PPP server."
        ),
        default=None,
    )
    gateway: str | None = Field(
        description="Gateway IP for this route.",
        regex=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",
        default=None,
    )
    internet_service: list[int] | int | None = Field(
        description="Application ID in the Internet service database.",
        ge=0,
        le=4294967295,
        default=None,
    )
    internet_service_custom: list[str] | str | None = Field(
        alias="internet-service-custom",
        description="Application name in the Internet service custom database.",
        max_length=64,
        default=None,
    )
    link_monitor_exempt: State | None = Field(
        alias="link-monitor-exempt",
        description="Enable/disable withdrawal of this static route when link "
        "monitor or health check is down. enable - Keep this static route "
        "when link monitor or health check is down. disable - Withdraw "
        "this static route when link monitor or health check is down (default)",
        default=None,
    )
    preferred_source: str = Field(
        alias="preferred-source",
        description="Preferred source IP for this route.",
        regex=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",
        default=None,
    )
    priority: int | None = Field(
        description="Administrative priority (1 - 65535).",
        ge=1,
        le=65535,
        default=None,
    )
    sdwan_zone: list[SdwanZoneItem] | list[str] | None = Field(
        alias="sdwan-zone",
        description="list of Fortinet SD-WAN zone items associated with the route.",
        default=None,
    )
    src: list[str] | str | None = Field(
        description="Source prefix for this route.",
        default=None,
    )
    status: State | None = Field(
        description="Enable/disable this static route.",
        default=None,
    )
    tag: int | None = Field(
        description="Route tag.",
        ge=0,
        le=4294967295,
        default=None,
    )
    vrf: int | None = Field(
        description="Virtual Routing Forwarding ID.",
        ge=0,
        le=251,
        default=None,
    )
    weight: int | None = Field(
        description="Administrative weight (0 - 255).",
        ge=0,
        le=255,
        default=None,
    )


class CreateFortinetStaticRoute(FortinetStaticRouteBase):
    """
    Pydantic representation of a Fortinet model used for
    static routes management operations
    """

    seq_num: int | None = Field(
        alias="seq-num",
        description="Sequence number.",
        ge=0,
        le=4294967295,
        default=None,
    )


class UpdateFortinetStaticRoute(FortinetStaticRouteBase):
    """
    Pydantic representation of a Fortinet model used for
    static routes management operations
    """


class FortinetStaticRoute(FortinetStaticRouteBase, use_enum_values=True):
    """
    Pydantic representation of a Fortinet model used for
    static routes management operations
    """

    seq_num: int = Field(
        alias="seq-num",
        description="Sequence number.",
        ge=0,
        le=4294967295,
    )
