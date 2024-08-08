"""
Fortimanager virtual IPv6 rule model
"""

# pylint: disable=too-many-lines
from enum import (
    Enum,
)

from pydantic import (
    BaseModel,
    Field,
)

from common.southbound.fortimanager.v1.models.policy_package.rules.common.enums import (
    StatusEnum,
)
from common.southbound.fortimanager.v1.models.policy_package.rules.virtual_ip import (
    DynamicMapping,
    PolicyPackageFirewall,
    ProtocolEnum,
)


class TypeEnum(Enum):
    """
    Types
    """

    ACCESS_PROXY = "access-proxy"  # 6
    SERVER_LOAD_BALANCE = "server-load-balance"  # 3
    STATIC_NAT = "static-nat"  # 0


class FirewallVip6(PolicyPackageFirewall, DynamicMapping):
    """
    Configure virtual IP for IPv6.
    """

    add_nat64_route: StatusEnum = Field(
        alias="add-nat64-route",
        default=StatusEnum.ENABLE,
        description="Enable/disable adding NAT64 route.",
    )

    type: TypeEnum = Field(
        default=TypeEnum.STATIC_NAT,
        description="Configure a static NAT server load balance"
        " VIP or access proxy.",
    )

    embedded_ipv4_address: StatusEnum = Field(
        alias="embedded-ipv4-address",
        default=StatusEnum.DISABLE,
        description="Enable/disable use of the lower 32 bits of the "
        "external IPv6 address as mapped IPv4 address.",
    )
    extip: str = Field(
        default="::",
        description="IPv6 address or address range on the external interface"
        " that you want to map to an address or address range on the destination"
        " network.",
    )
    extport: str = Field(
        default="0",
        description="Incoming port number range that you want to map to a port"
        " number range on the destination network.",
    )
    ipv4_mappedip: str = Field(
        alias="ipv4-mappedip",
        default="0.0.0.0",  # noqa: S104
        description="Range of mapped IP addresses. Specify the start IP address"
        " followed by a space and the end IP address.",
    )
    ipv4_mappedport: str = Field(
        alias="ipv4-mappedport",
        default="0",
        description="IPv4 port number range on the destination network to which"
        " the external port number range is mapped.",
    )
    mappedip: str = Field(
        default="::",
        description="Mapped IPv6 address range in the format startIP-endIP.",
    )

    name: str = Field(
        ...,
        description="Virtual ip6 name.",
        max_length=79,
    )
    nat64: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable DNAT64.",
    )
    nat66: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable/disable DNAT66.",
    )
    ndp_reply: StatusEnum = Field(
        alias="ndp-reply",
        default=StatusEnum.ENABLE,
        description="Enable/disable this FortiGate unit's ability to respond to "
        "NDP requests for this virtual IP address (default = enable).",
    )
    src_filter: list[str] = Field(
        ...,
        alias="src-filter",
        description="Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses"
        " with spaces.",
    )


class FortiManagerFirewallVip6V1(BaseModel):
    """
    Fortimanager firewall virtual ipv6
    """

    name: str = Field(
        ...,
        description="Virtual ip6 name.",
        max_length=79,
    )
    comment: str | None = Field(
        default=None,
        description="Comment.",
        max_length=255,
    )
    type: TypeEnum = Field(
        default=TypeEnum.STATIC_NAT,
        description="Configure a static NAT server load balance"
        " VIP or access proxy.",
    )
    extip: str = Field(
        default="::",
        description="IPv6 address or address range on the external interface"
        " that you want to map to an address or address range on the destination"
        " network.",
    )
    extport: str = Field(
        default="0",
        description="Incoming port number range that you want to map to a port"
        " number range on the destination network.",
    )
    mappedip: str = Field(
        default="::",
        description="Mapped IPv6 address range in the format startIP-endIP.",
    )
    mappedport: str = Field(
        default="0",
        description="Port number range on the destination network to which"
        " the external port number range is mapped.",
    )
    protocol: ProtocolEnum = Field(
        default=ProtocolEnum.TCP, description="Protocol to use when forwarding packets."
    )
