"""
FortiManager BGP Templates V1 Pydantic models
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

# ruff: noqa: S104
# pylint: disable=line-too-long
# pylint: disable=too-many-lines


ADDITIONAL_PATH_DESCRIPTION = "Enable/disable IPv4 additional-path capability."
ADDITIONAL_PATH6_DESCRIPTION = "Enable/disable IPv6 additional-path capability."
PASSIVE_DESCRIPTION = "Enable/disable sending of open messages to this neighbor."
SOFT_RECONFIGURATION = "Enable/disable allow IPv4 inbound soft reconfiguration."


class TemplateType(str, Enum):
    """
    BGP Template Type
    """

    BGP_TEMPLATE = "template"


class StatusEnum(str, Enum):
    """
    Enum representing Status option for BGP Templates
    """

    DISABLE = "disable"  # 0
    ENABLE = "enable"  # 1


class StatusEnumAdditionalPath(str, Enum):
    """
    Enum representing Status option for Additional Paths related configurations
    """

    SEND = "send"  # 0
    RECEIVE = "receive"  # 1
    BOTH = "both"  # 2
    DISABLE = "disable"  # 3


class StatusEnumAttributeUnchanged(str, Enum):
    """
    Enum representing Status option for Attributed Unchanged related configurations
    """

    AS_PATH = "as-path"
    MED = "med"
    NEXT_HOP = "next-hop"


class StatusEnumCapability(str, Enum):
    """
    Enum representing Status option for Capability related configurations
    """

    NONE = "none"  # 0
    RECEIVE = "receive"  # 1
    SEND = "send"  # 2
    BOTH = "both"  # 3


class ConfederationPeer(BaseModel):
    """
    Pydantic representation of confederation peers as part of the BGP Templates
    """

    peer: str | None


class StatusEnumSendCommunity(str, Enum):
    """
    Enum representing Status option for Send Community related configurations
    """

    STANDARD = "standard"  # 0
    EXTENDED = "extended"  # 1
    BOTH = "both"  # 2
    DISABLE = "disable"  # 3


class TagResolveModeEnum(str, Enum):
    """
    Enum representing Status option for Tag Resolve Mode related configurations
    """

    DISABLE = "disable"
    PREFERRED = "preferred"
    MERGE = "merge"


class TemplateScopeMember(BaseModel):
    """
    A scope member of BGP template (device or device group)
    to which the BGP template is applied
    """

    name: str
    oid: int
    vdom: str = "root"
    vdom_oid: int


class TemplateSetting(BaseModel):
    """
    BGP Template settings
    """

    description: str | None = Field(
        description="BGP Template description.",
        default=None,
    )
    option: Any | None = Field(default=None)
    stype: str | None = Field(description="BGP Template stype", default="router_bgp")
    widgets: list[str] | None = Field(
        description="BGP Template widgets.",
        default=["rout_bgp"],
    )


class BGPTemplate(BaseModel, use_enum_values=True):
    """
    Pydantic representation of the BGP Template used in GET methods
    """

    name: str
    oid: int
    scope_member: TemplateScopeMember | None = Field(
        ...,
        description="Assigned devices or groups to BGP template",
        alias="scope member",
    )
    template_setting: TemplateSetting | None = Field(
        ..., description="BGP Template setting", alias="template setting"
    )
    type: TemplateType = TemplateType.BGP_TEMPLATE


class NeighborBase(
    BaseModel, allow_population_by_field_name=True, use_enum_values=True
):
    """
    Pydantic model containing common fields between Neighbor related configurations
    such as Neghbors and Neighbor Groups
    """

    activate: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable/disable address family IPv4 for this neighbor.",
    )
    activate_evpn: StatusEnum | None = Field(
        default=None,
        description="Enable/disable address family L2VPN EVPN for this neighbor.",
    )
    activate_vpnv4: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="activate-vpnv4",
        description="Enable/disable address family IPv4 for this neighbor.",
    )
    activate_vpnv6: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="activate-vpnv6",
        description="Enable/disable address family IPv6 for this neighbor.",
    )
    activate6: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description="Enable/disable address family IPv6 for this neighbor.",
    )
    additional_path_vpnv4: StatusEnumAdditionalPath = Field(
        default=StatusEnumAdditionalPath.DISABLE,
        alias="additional-path-vpnv4",
        description="Enable/disable VPNv4 additional-path capability.",
    )
    additional_path_vpnv6: StatusEnumAdditionalPath = Field(
        default=StatusEnumAdditionalPath.DISABLE,
        alias="additional-path-vpnv6",
        description="Enable/disable VPNv6 additional-path capability.",
    )
    additional_path6: StatusEnumAdditionalPath = Field(
        default=StatusEnumAdditionalPath.DISABLE,
        alias="additional-path6",
        description=ADDITIONAL_PATH6_DESCRIPTION,
    )
    adv_additional_path: int = Field(
        default=2,
        alias="adv-additional-path",
        le=255,
        ge=2,
        description="Number of IPv4 additional paths that can be advertised to this neighbor.",
    )
    adv_additional_path_vpnv4: int = Field(
        default=2,
        alias="adv-additional-path-vpnv4",
        le=255,
        ge=2,
        description="Number of VPNv4 additional paths that can be advertised to this neighbor.",
    )
    adv_additional_path_vpnv6: int = Field(
        default=2,
        alias="adv-additional-path-vpnv6",
        le=255,
        ge=2,
        description="Number of VPNv6 additional paths that can be advertised to this neighbor.",
    )
    adv_additional_path6: int = Field(
        default=2,
        alias="adv-additional-path6",
        le=255,
        ge=2,
        description="Number of IPv6 additional paths that can be advertised to this neighbor.",
    )
    allowas_in_enable: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="allowas-in-enable",
        description="Enable/disable IPv4 Enable to allow my AS in AS path.",
    )
    allowas_in_enable_evpn: StatusEnum | None = Field(
        default=StatusEnum.DISABLE,
        alias="allowas-in-enable-evpn",
        description="Enable/disable to allow my AS in AS path for L2VPN EVPN route.",
    )
    allowas_in_enable_vpn4: StatusEnum | None = Field(
        default=StatusEnum.DISABLE,
        alias="allowas-in-enable-vpnv4",
        description="Enable/disable to allow my AS in AS path for VPNv4 route.",
    )
    allowas_in_enable_vpn6: StatusEnum | None = Field(
        default=StatusEnum.DISABLE,
        alias="allowas-in-enable-vpnv6",
        description="Enable/disable to allow my AS in AS path for VPNv6 route.",
    )
    allowas_in_enable6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="allowas-in-enable6",
        description="Enable/disable IPv6 Enable to allow my AS in AS path.",
    )
    allowas_in_evpn: int = Field(
        default=3,
        alias="allowas-in-evpn",
        description="The maximum number of occurrence of my AS number allowed for L2VPN EVPN route.",
        ge=1,
        le=10,
    )
    allowas_in_vpnv6: int = Field(
        default=0,
        alias="allowas-in-vpnv6",
        description="The maximum number of occurrence of my AS number allowed for VPNv6 route.",
        ge=1,
        le=10,
    )
    as_override: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="as-override",
        description="Enable/disable replace peer AS with own AS for IPv4.",
    )
    as_override6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="as-override6",
        description="Enable/disable replace peer AS with own AS for IPv6.",
    )
    attribute_unchanged: StatusEnumAttributeUnchanged = Field(
        default=StatusEnumAttributeUnchanged.AS_PATH,
        alias="attribute-unchanged",
        description="IPv4 List of attributes that should be unchanged.",
    )
    attribute_unchanged_vpnv4: StatusEnumAttributeUnchanged = Field(
        default=StatusEnumAttributeUnchanged.AS_PATH,
        alias="attribute-unchanged-vpnv4",
        description="List of attributes that should be unchanged for VPNv4 route.",
    )
    attribute_unchanged_vpnv6: StatusEnumAttributeUnchanged = Field(
        default=StatusEnumAttributeUnchanged.AS_PATH,
        alias="attribute-unchanged-vpnv6",
        description="List of attributes that should be unchanged for VPNv6 route.",
    )
    attribute_unchanged6: StatusEnumAttributeUnchanged = Field(
        default=StatusEnumAttributeUnchanged.AS_PATH,
        alias="attribute-unchanged6",
        description="IPv4 List of attributes that should be unchanged.",
    )
    auth_options: str | None = Field(
        default=None,
        alias="auth-options",
        description="Key-chain name for TCP authentication options.",
        max_length=35,
    )
    bfd: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable BFD for this neighbor."
    )
    capability_default_originate: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-default-originate",
        description="Enable/disable advertise default IPv4 route to this neighbor.",
    )
    capability_default_originate6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-default-originate6",
        description="Enable/disable advertise default IPv6 route to this neighbor.",
    )
    capability_dynamic: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-dynamic",
        description="Enable/disable advertise dynamic capability to this neighbor.",
    )
    capability_graceful_restart_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-graceful-restart-evpn",
        description="Enable/disable advertisement of L2VPN EVPN graceful restart capability to this neighbor.",
    )
    capability_graceful_restart_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-graceful-restart-vpnv4",
        description="Enable/disable advertise VPNv4 graceful restart capability to this neighbor.",
    )
    capability_graceful_restart_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-graceful-restart-vpnv6",
        description="Enable/disable advertise VPNv6 graceful restart capability to this neighbor.",
    )
    capability_graceful_restart6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-graceful-restart6",
        description="Enable/disable advertise IPv6 graceful restart capability to this neighbor.",
    )
    capability_orf: StatusEnumCapability = Field(
        default=StatusEnumCapability.NONE,
        alias="capability-orf",
        description="Accept/Send IPv4 ORF lists to/from this neighbor.",
    )
    capability_orf6: StatusEnumCapability = Field(
        default=StatusEnumCapability.NONE,
        alias="capability-orf6",
        description="Accept/Send IPv6 ORF lists to/from this neighbor.",
    )
    capability_route_refresh: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="capability-route-refresh",
        description="Enable/disable advertise route refresh capability to this neighbor.",
    )
    default_originate_routemap: str | None = Field(
        default=None,
        alias="default-originate-routemap",
        description="Route map to specify criteria to originate IPv4 default.",
    )
    default_originate_routemap6: str | None = Field(
        default=None,
        alias="default-originate-routemap6",
        description="Route map to specify criteria to originate IPv6 default.",
    )
    distribute_list_in: str | None = Field(
        default=None, description="Filter for IPv4 updates from this neighbor."
    )
    distribute_list_in_vpnv4: str | None = Field(
        default=None, description="Filter for VPNv4 updates from this neighbor."
    )
    distribute_list_in_vpnv6: str | None = Field(
        default=None, description="Filter for VPNv6 updates from this neighbor."
    )
    distribute_list_in6: str | None = Field(
        default=None, description="Filter for IPv6 updates from this neighbor."
    )
    distribute_list_out: str | None = Field(
        default=None, description="Filter for IPv4 updates to this neighbor."
    )
    distribute_list_out_vpnv4: str | None = Field(
        default=None, description="Filter for VPNv4 updates to this neighbor."
    )
    distribute_list_out_vpnv6: str | None = Field(
        default=None, description="Filter for VPNv6 updates to this neighbor."
    )
    distribute_list_out6: str | None = Field(
        default=None, description="Filter for IPv6 updates to this neighbor."
    )
    dont_capability_negotiate: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="dont-capability-negotiate",
        description="Do not negotiate capabilities with this neighbor.",
    )
    ebgp_enforce_multihop: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="ebgp-enforce-multihop",
        description="Enable/disable allow multi-hop EBGP neighbors.",
    )
    ebgp_multihop_ttl: int = Field(
        default=255,
        alias="ebgp-multihop-ttl",
        le=255,
        ge=1,
        description="EBGP multihop TTL for this peer.",
    )
    filter_list_in: str | None = Field(
        default=None,
        alias="filter-list-in",
        description="Filter for VPNv4 updates to this neighbor.",
        max_length=35,
    )
    filter_list_in_vpnv4: str | None = Field(
        default=None,
        alias="filter-list-in-vpnv4",
        description="BGP filter for VPNv4 inbound routes.",
        max_length=35,
    )
    filter_list_in_vpnv6: str | None = Field(
        default=None,
        alias="filter-list-in-vpnv6",
        description="BGP filter for VPNv6 inbound routes.",
        max_length=35,
    )
    filter_list_in6: str | None = Field(
        default=None,
        alias="filter-list-in6",
        description="Filter for VPNv6 updates to this neighbor.",
        max_length=35,
    )
    filter_list_out: str | None = Field(
        default=None,
        alias="filter-list-out",
        description="BGP filter for IPv4 outbound routes.",
        max_length=35,
    )
    filter_list_out_vpnv4: str | None = Field(
        default=None,
        alias="filter-list-out-vpnv4",
        description="BGP filter for VPNv4 outbound routes.",
        max_length=35,
    )
    filter_list_out_vpnv6: str | None = Field(
        default=None,
        alias="filter-list-out-vpnv6",
        description="BGP filter for VPNv6 outbound routes.",
        max_length=35,
    )
    filter_list_out6: str | None = Field(
        default=None,
        alias="filter-list-out6",
        description="BGP filter for IPv6 outbound routes.",
        max_length=35,
    )
    holdtime_timer: int = Field(
        default=65535,
        alias="holdtime-timer",
        ge=3,
        le=65535,
        description="Interval (sec) before peer considered dead.",
    )
    keep_alive_timer: int = Field(
        default=65535,
        alias="keep-alive-timer",
        description="Keep alive timer interval (sec).",
    )
    local_as: str | None = Field(
        default=None, alias="local-as", description="Local AS number of neighbor."
    )
    local_as_no_prepend: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="local-as-no-prepend",
        description="Do not prepend local-as to incoming updates.",
    )
    local_as_replace_as: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="local-as-replace-as",
        description="Replace real AS with local-as in outgoing updates.",
    )
    maximum_prefix: int | None = Field(
        default=None,
        alias="maximum-prefix",
        description="Maximum number of IPv4 prefixes to accept from this peer.",
    )
    maximum_prefix_evpn: int | None = Field(
        default=None,
        alias="maximum-prefix-evpn",
        description="Maximum number of L2VPN EVPN prefixes to accept from this peer.",
    )
    maximum_prefix_threshold: int | None = Field(
        default=75,
        alias="maximum-prefix-threshold",
        description="Maximum IPv4 prefix threshold value (1 - 100 percent).",
    )
    maximum_prefix_threshold_evpn: int | None = Field(
        default=75,
        alias="maximum-prefix-threshold-evpn",
        description="Maximum L2VPN EVPN prefix threshold value (1 - 100 percent).",
    )
    maximum_prefix_threshold_vpnv4: int | None = Field(
        default=75,
        alias="maximum-prefix-threshold-vpnv4",
        description="Maximum VPNv4 prefix threshold value (1 - 100 percent).",
    )
    maximum_prefix_threshold_vpnv6: int | None = Field(
        default=75,
        alias="maximum-prefix-threshold-vpnv6",
        description="Maximum VPNv6 prefix threshold value (1 - 100 percent).",
    )
    maximum_prefix_threshold6: int | None = Field(
        default=75,
        alias="maximum-prefix-threshold6",
        description="Maximum IPv6 prefix threshold value (1 - 100 percent).",
    )
    maximum_prefix_vpnv4: int | None = Field(
        default=None,
        alias="maximum_prefix_vpnv4",
        description="Maximum number of VPNv4 prefixes to accept from this peer.",
    )
    maximum_prefix_vpnv6: int | None = Field(
        default=None,
        alias="maximum_prefix_vpnv6",
        description="Maximum number of VPNv6 prefixes to accept from this peer.",
    )
    maximum_prefix_warning_only: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="maximum-prefix-warning-only",
        description="Enable/disable IPv4 Only give warning message when limit is exceeded.",
    )
    maximum_prefix_warning_only_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="maximum-prefix-warning-only-evpn",
        description="Enable/disable only sending warning message when exceeding limit of L2VPN EVPN routes.",
    )
    maximum_prefix_warning_only_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="maximum-prefix-warning-only-vpnv4",
        description="Enable/disable only giving warning message when limit is exceeded for VPNv4 routes.",
    )
    maximum_prefix_warning_only_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="maximum-prefix-warning-only-vpnv6",
        description="Enable/disable only giving warning message when limit is exceeded for VPNv6 routes.",
    )
    maximum_prefix_warning_only6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="maximum-prefix-warning-only6",
        description="Enable/disable IPv6 Only give warning message when limit is exceeded.",
    )
    maximum_prefix6: int | None = Field(
        default=None,
        alias="maximum-prefix6",
        description="Maximum number of IPv6 prefixes to accept from this peer.",
    )
    next_hop_self: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self",
        description="Enable/disable IPv4 next-hop calculation for this neighbor.",
    )
    next_hop_self_rr: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self-rr",
        description="Enable/disable setting nexthop's address to interface's IPv4 address for route-reflector routes.",
    )
    next_hop_self_rr6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self-rr6",
        description="Enable/disable setting nexthop's address to interface's IPv6 address for route-reflector routes.",
    )
    next_hop_self_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self-vpnv4",
        description="Enable/disable setting VPNv4 next-hop to interface's IP address for this neighbor.",
    )
    next_hop_self_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self-vpnv6",
        description="Enable/disable setting VPNv6 next-hop to interface's IP address for this neighbor.",
    )
    next_hop_self6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="next-hop-self6",
        description="Enable/disable IPv6 next-hop calculation for this neighbor.",
    )
    override_capability: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="override-capability",
        description="Enable/disable override result of capability negotiation.",
    )
    prefix_list_in: str | None = Field(
        default=None,
        alias="prefix-list-in",
        description="IPv4 Inbound filter for updates from this neighbor.",
    )
    prefix_list_in_vpnv4: str | None = Field(
        default=None,
        alias="prefix-list-in-vpnv4",
        description="Inbound filter for VPNv4 updates from this neighbor.",
    )
    prefix_list_in_vpnv6: str | None = Field(
        default=None,
        alias="prefix-list-in-vpnv6",
        description="Inbound filter for VPNv6 updates from this neighbor.",
    )
    prefix_list_in6: str | None = Field(
        default=None,
        alias="prefix-list-in6",
        description="IPv6 Inbound filter for updates from this neighbor.",
    )
    prefix_list_out: str | None = Field(
        default=None,
        alias="prefix-list-out",
        description="IPv4 Outbound filter for updates to this neighbor.",
    )
    prefix_list_out_vpnv4: str | None = Field(
        default=None,
        alias="prefix-list-out-vpnv4",
        description="Outbound filter for VPNv4 updates to this neighbor.",
    )
    prefix_list_out_vpnv6: str | None = Field(
        default=None,
        alias="prefix-list-out-vpnv6",
        description="Outbound filter for VPNv4 updates to this neighbor.",
    )
    prefix_list_out6: str | None = Field(
        default=None,
        alias="prefix-list-out6",
        description="IPv6 Outbound filter for updates to this neighbor.",
    )
    remote_as: str | None = Field(
        default=None, alias="remote-as", description="AS number of neighbor."
    )
    remove_private_as: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="remove-private-as",
        description="Enable/disable remove private AS number from IPv4 outbound updates.",
    )
    remove_private_as_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="remove-private-as-evpn",
        description="Enable/disable removing private AS number from L2VPN EVPN outbound updates.",
    )
    remove_private_as_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="remove-private-as-vpnv4",
        description="Enable/disable remove private AS number from VPNv4 outbound updates.",
    )
    remove_private_as_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="remove-private-as-vpnv6",
        description="Enable/disable remove private AS number from VPNv6 outbound updates.",
    )
    remove_private_as6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="remove-private-as6",
        description="Enable/disable remove private AS number from IPv6 outbound updates.",
    )
    restart_time: int = Field(
        default=0,
        alias="restart-time",
        description="Graceful restart delay time (sec, 0 = global default).",
    )
    retain_stale_time: int = Field(
        default=0, alias="retain-stale-time", description="Time to retain stale routes."
    )
    route_map_in: str | None = Field(
        default=None, alias="route-map-in", description="IPv4 Inbound route map filter."
    )
    route_map_in_evpn: str | None = Field(
        default=None,
        alias="route-map-in-evpn",
        description="L2VPN EVPN inbound route map filter.",
    )
    route_map_in_vpnv4: str | None = Field(
        default=None,
        alias="route-map-in-vpnv4",
        description="VPNv4 inbound route map filter.",
    )
    route_map_in_vpnv6: str | None = Field(
        default=None,
        alias="route-map-in-vpnv6",
        description="VPNv6 inbound route map filter.",
    )
    route_map_in6: str | None = Field(
        default=None,
        alias="route-map-in6",
        description="IPv6 Inbound route map filter.",
    )
    route_map_out: str | None = Field(
        default=None,
        alias="route-map-out",
        description="IPv4 outbound route map filter.",
    )
    route_map_out_evpn: str | None = Field(
        default=None,
        alias="route-map-out-evpn",
        description="L2VPN EVPN outbound route map filter.",
    )
    route_map_out_preferable: str | None = Field(
        default=None,
        alias="route-map-out-preferable",
        description="IPv4 outbound route map filter if the peer is preferred.",
    )
    route_map_out_vpnv4: str | None = Field(
        default=None,
        alias="route-map-out-vpnv4",
        description="VPNv4 outbound route map filter.",
    )
    route_map_out_vpnv4_preferable: str | None = Field(
        default=None,
        alias="route-map-out-vpnv4-preferable",
        description="VPNv4 outbound route map filter if the peer is preferred.",
    )
    route_map_out_vpnv6: str | None = Field(
        default=None,
        alias="route-map-out-vpnv6",
        description="VPNv6 outbound route map filter.",
    )
    route_map_out_vpnv6_preferable: str | None = Field(
        default=None,
        alias="route-map-out-vpnv6-preferable",
        description="VPNv6 outbound route map filter if the peer is preferred.",
    )
    route_map_out6: str | None = Field(
        default=None,
        alias="route-map-out6",
        description="IPv6 outbound route map filter.",
    )
    route_map_out6_preferable: str | None = Field(
        default=None,
        alias="route-map-out6-preferable",
        description="IPv6 outbound route map filter if the peer is preferred.",
    )
    route_reflector_client: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-reflector-client",
        description="Enable/disable IPv4 AS route reflector client.",
    )
    route_reflector_client_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-reflector-client-evpn",
        description="Enable/disable L2VPN EVPN AS route reflector client for this neighbor.",
    )
    route_reflector_client_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-reflector-client-vpnv4",
        description="Enable/disable VPNv4 AS route reflector client for this neighbor.",
    )
    route_reflector_client_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-reflector-client-vpnv6",
        description="Enable/disable VPNv6 AS route reflector client for this neighbor.",
    )
    route_reflector_client6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-reflector-client6",
        description="Enable/disable IPv6 AS route reflector client.",
    )
    route_server_client: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-server-client",
        description="Enable/disable IPv4 AS route server client.",
    )
    route_server_client_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-server-client-evpn",
        description="Enable/disable L2VPN EVPN AS route server client for this neighbor.",
    )
    route_server_client_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-server-client-vpnv4",
        description="Enable/disable VPNv4 AS route server client for this neighbor.",
    )
    route_server_client_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-server-client-vpnv6",
        description="Enable/disable VPNv6 AS route server client for this neighbor.",
    )
    route_server_client6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="route-server-client6",
        description="Enable/disable IPv6 AS route server client.",
    )
    send_community: StatusEnumSendCommunity = Field(
        default=StatusEnumSendCommunity.DISABLE,
        alias="send-community",
        description="IPv4 Send community attribute to neighbor.",
    )
    send_community_evpn: StatusEnumSendCommunity = Field(
        default=StatusEnumSendCommunity.DISABLE,
        alias="send-community-evpn",
        description="Enable/disable sending community attribute to neighbor for L2VPN EVPN address family.",
    )
    send_community_vpnv4: StatusEnumSendCommunity = Field(
        default=StatusEnumSendCommunity.DISABLE,
        alias="send-community-vpnv4",
        description="Send community attribute to neighbor for VPNv4 address family.",
    )
    send_community_vpnv6: StatusEnumSendCommunity = Field(
        default=StatusEnumSendCommunity.DISABLE,
        alias="send-community-vpnv6",
        description="Send community attribute to neighbor for VPNv6 address family.",
    )
    send_community6: StatusEnumSendCommunity = Field(
        default=StatusEnumSendCommunity.DISABLE,
        alias="send-community6",
        description="IPv6 Send community attribute to neighbor.",
    )
    shutdown: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable shutdown this neighbor."
    )
    soft_reconfiguration_evpn: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="soft-reconfiguration-evpn",
        description="Enable/disable L2VPN EVPN inbound soft reconfiguration.",
    )
    soft_reconfiguration_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="soft-reconfiguration-vpnv4",
        description="Enable/disable allow VPNv4 inbound soft reconfiguration.",
    )
    soft_reconfiguration_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="soft-reconfiguration-vpnv6",
        description="Enable/disable allow VPNv6 inbound soft reconfiguration.",
    )
    soft_reconfiguration6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="soft-reconfiguration6",
        description="Enable/disable allow IPv6 inbound soft reconfiguration.",
    )
    stale_route: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="stale-route",
        description="Enable/disable stale route after neighbor down.",
    )
    strict_capability_match: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="strict-capability-match",
        description="Enable/disable strict capability matching.",
    )
    unsuppress_map: str | None = Field(
        default=None,
        alias="unsuppress-map",
        description="IPv4 Route map to selectively unsuppress suppressed routes.",
    )
    unsuppress_map6: str | None = Field(
        default=None,
        alias="unsuppress-map6",
        description="IPv6 Route map to selectively unsuppress suppressed routes.",
    )
    update_source: str | None = Field(
        default=None,
        alias="update-source",
        description="Interface to use as source IP/IPv6 address of TCP connections.",
        max_length=15,
    )
    weight: int | None = Field(
        default=None, description="Neighbor weight.", ge=0, le=65535
    )


class Neighbor(NeighborBase, allow_population_by_field_name=True, use_enum_values=True):
    """
    Pydantic model containing Neighbor configurations
    """

    additional_path: StatusEnumAdditionalPath = Field(
        default=StatusEnumAdditionalPath.RECEIVE,
        alias="additional-path",
        description=ADDITIONAL_PATH_DESCRIPTION,
    )
    advertisement_interval: int = Field(
        default=1,
        alias="advertisement-interval",
        description="Minimum interval (sec) between sending updates.",
    )
    allowas_in: int = Field(
        default=0,
        alias="allowas-in",
        description="IPv4 The maximum number of occurrence of my AS number allowed.",
    )
    allowas_in_vpnv4: int = Field(
        default=0,
        alias="allowas-in-vpnv4",
        description="The maximum number of occurrence of my AS number allowed for VPNv4 route.",
    )
    allowas_in6: int = Field(
        default=0,
        alias="allowas-in6",
        description="IPv6 The maximum number of occurrence of my AS number allowed.",
    )
    capability_graceful_restart: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="capability-graceful-restart",
        description="Enable/disable advertise IPv4 graceful restart capability to this neighbor.",
    )
    connect_timer: int = Field(
        default=10,
        alias="connect-timer",
        description="Interval (sec) for connect timer.",
    )
    description: str | None = Field(default=None, description="Description.")
    interface: list[str] | None = Field(
        default=[],
        description="Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address.",
    )
    ip: str | None = Field(default=None, description="IP/IPv6 address of neighbor.")
    link_down_failover: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="link-down-failover",
        description="Enable/disable failover upon link down.",
    )
    passive: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description=PASSIVE_DESCRIPTION,
    )
    soft_reconfiguration: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="soft-reconfiguration",
        description=SOFT_RECONFIGURATION,
    )


class NeighborGroup(
    NeighborBase, allow_population_by_field_name=True, use_enum_values=True
):
    """
    Pydantic model containing Neighbor Group configurations
    """

    additional_path: StatusEnumAdditionalPath = Field(
        default=StatusEnumAdditionalPath.DISABLE,
        alias="additional-path",
        description=ADDITIONAL_PATH_DESCRIPTION,
    )
    advertisement_interval: int = Field(
        default=30,
        alias="advertisement-interval",
        description="Minimum interval (sec) between sending updates.",
    )
    allowas_in: int = Field(
        default=3,
        alias="allowas-in",
        description="IPv4 The maximum number of occurrence of my AS number allowed.",
    )
    allowas_in_vpnv4: int = Field(
        default=3,
        alias="allowas-in-vpnv4",
        description="The maximum number of occurrence of my AS number allowed for VPNv4 route.",
    )
    allowas_in6: int = Field(
        default=3,
        alias="allowas-in6",
        description="IPv6 The maximum number of occurrence of my AS number allowed.",
    )
    capability_graceful_restart: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="capability-graceful-restart",
        description="Enable/disable advertise IPv4 graceful restart capability to this neighbor.",
    )
    connect_timer: int | None = Field(
        default=None,
        alias="connect-timer",
        description="Interval (sec) for connect timer.",
    )
    interface: list[str] | None = Field(
        default=None,
        description="Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address.",
    )
    ip: str | None = Field(default=None, description="IP/IPv6 address of neighbor.")
    link_down_failover: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="link-down-failover",
        description="Enable/disable failover upon link down.",
    )
    name: str = Field(description="Neighbor group name.", max_length=45)
    passive: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        description=PASSIVE_DESCRIPTION,
    )
    soft_reconfiguration: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="soft-reconfiguration",
        description=SOFT_RECONFIGURATION,
    )


class NeighborRange(BaseModel):
    """
    Pydantic model containing Neighbor Range configurations
    """

    id: int
    prefix: str
    max_neighbor_num: int = Field(
        alias="max-neighbor-num", description="Maximum number of neighbors."
    )
    neighbor_group: list[str] = Field(
        alias="neighbor-group", description="Neighbor group name."
    )


class Network(BaseModel):
    """
    Pydantic model representing Network configuration
    """

    prefix: str


class Network6(BaseModel):
    """
    Pydantic model representing IPv6 Network configuration
    """

    prefix6: str


class Redistribute(BaseModel):
    """
    Pydantic model representing Redistribute configuration
    """

    name: str
    status: StatusEnum
    route_map: str = Field(alias="route-map", description="Route map name.")


class BGPRouterConfig(BaseModel):
    """
    Pydantic model representing main SET BGP router configurations
    """

    additional_path: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="additional-path",
        description=ADDITIONAL_PATH_DESCRIPTION,
    )
    additional_path6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="additional-path6",
        description=ADDITIONAL_PATH6_DESCRIPTION,
    )
    additional_path_select: int = Field(
        default=2,
        alias="additional-path-select",
        ge=2,
        le=255,
        description="Number of additional paths to be selected for each IPv4 NLRI.",
    )
    additional_path_select6: int = Field(
        default=2,
        alias="additional-path-select6",
        ge=2,
        le=255,
        description="Number of additional paths to be selected for each IPv6 NLRI.",
    )
    additional_path_select_vpnv4: int = Field(
        default=2,
        alias="additional-path-select-vpnv4",
        ge=2,
        le=255,
        description="Number of additional paths to be selected for each VPNv4 NLRI.",
    )
    additional_path_select_vpnv6: int = Field(
        default=2,
        alias="additional-path-select-vpnv6",
        ge=2,
        le=255,
        description="Number of additional paths to be selected for each VPNv6 NLRI.",
    )
    additional_path_vpnv4: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="additional-path-vpnv4",
        description="Enable/disable selection of BGP VPNv4 additional paths.",
    )
    additional_path_vpnv6: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="additional-path-vpnv6",
        description="Enable/disable selection of BGP VPNv6 additional paths.",
    )
    always_compare_med: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="always-compare-med",
        description="Enable/disable always compare MED.",
    )
    as_field: str = Field(
        default="0",
        alias="as",
        description="Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.",
    )
    bestpath_as_path_ignore: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="bestpath-as-path-ignore",
        description="Enable/disable ignore AS path.",
    )
    bestpath_cmp_confed_aspath: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="bestpath-cmp-confed-aspath",
        description="Enable/disable compare federation AS path length.",
    )
    bestpath_cmp_routerid: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="bestpath-cmp-routerid",
        description="Enable/disable compare router ID for identical EBGP paths.",
    )
    bestpath_med_confed: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="bestpath-med-confed",
        description="Enable/disable compare MED among confederation paths.",
    )
    bestpath_med_missing_as_worst: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="bestpath-med-missing-as-worst",
        description="Enable/disable treat missing MED as least preferred.",
    )
    client_to_client_reflection: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="client-to-client-reflection",
        description="Enable/disable client-to-client route reflection.",
    )
    cluster_id: str = Field(
        default="0.0.0.0",
        alias="cluster-id",
        description="Route reflector cluster ID.",
    )
    confederation_identifier: int = Field(
        default=0,
        alias="confederation-identifier",
        description="Confederation identifier.",
    )
    confederation_peers: list[ConfederationPeer] | None = Field(
        default=[], alias="confederation-peers", description="Confederation peers."
    )
    dampening: StatusEnum = Field(
        default=StatusEnum.DISABLE, description="Enable/disable route-flap dampening."
    )
    dampening_max_suppress_time: int = Field(
        default=60,
        alias="dampening-max-suppress-time",
        description="Maximum minutes a route can be suppressed. Can have values between 1 and 255",
    )
    dampening_reachability_half_life: int = Field(
        default=15,
        alias="dampening-reachability-half-life",
        description="Reachability half-life time for penalty (min). Can have values between 1 and 45",
    )
    dampening_reuse: int = Field(
        default=750, alias="dampening-reuse", description="Threshold to reuse routes."
    )
    dampening_route_map: str | None = Field(
        default=None, alias="dampening-route-map", description="Criteria for dampening."
    )
    dampening_suppress: int = Field(
        default=2000,
        alias="dampening-suppress",
        description="Threshold to suppress routes.",
    )
    dampening_unreachability_half_life: int = Field(
        default=15,
        alias="dampening-unreachability-half-life",
        description="Unreachability half-life time for penalty (min). Can have values between 1 and 45",
    )
    default_local_preference: int = Field(
        default=100,
        alias="default-local-preference",
        description="Default local preference.",
    )
    deterministic_med: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="deterministic-med",
        description="Enable/disable enforce deterministic comparison of MED.",
    )
    distance_external: int = Field(
        default=20,
        alias="distance-external",
        ge=1,
        le=255,
        description="Distance for routes external to the AS.",
    )
    distance_internal: int = Field(
        default=200,
        alias="distance-internal",
        ge=1,
        le=255,
        description="Distance for routes internal to the AS.",
    )
    distance_local: int = Field(
        default=200,
        alias="distance-local",
        ge=1,
        le=255,
        description="Distance for routes local to the AS.",
    )
    ebgp_multipath: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="ebgp-multipath",
        description="Enable/disable EBGP multi-path.",
    )
    enforce_first_as: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="enforce-first-as",
        description="Enable/disable enforce first AS for EBGP routes.",
    )
    fast_external_failover: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="fast-external-failover",
        description="Enable/disable reset peer BGP session if link goes down.",
    )
    graceful_end_on_timer: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="graceful-end-on-timer",
        description="Enable/disable to exit graceful restart on timer only.",
    )
    graceful_restart: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="graceful-restart",
        description="Enable/disable BGP graceful restart capabilities.",
    )
    graceful_restart_time: int = Field(
        default=120,
        alias="graceful-restart-time",
        description="Time needed for neighbors to restart (sec).",
    )
    graceful_stalepath_time: int = Field(
        default=360,
        alias="graceful-stalepath-time",
        description="Time to hold stale paths of restarting neighbor (sec).",
    )
    graceful_update_delay: int = Field(
        default=120,
        alias="graceful-update-delay",
        description="Route advertisement/selection delay after restart (sec).",
    )
    holdtime_timer: int = Field(
        default=180,
        alias="holdtime-timer",
        description="Interval (sec) before peer considered dead.",
    )
    ibgp_multipath: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="ibgp-multipath",
        description="Enable/disable IBGP multi-path.",
    )
    ignore_optional_capability: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="ignore-optional-capability",
        description="Do not send unknown optional capability notification message.",
    )
    keepalive_timer: int = Field(
        default=60,
        alias="keepalive-timer",
        description="Keep alive timer interval (sec).",
    )
    log_neighbour_changes: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="log-neighbour-changes",
        description="Log BGP neighbor changes.",
    )
    multipath_recursive_distance: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="multipath-recursive-distance",
        description="Enable/disable use of recursive distance to select multipath.",
    )
    neighbor: list[Neighbor] | None = Field(
        default=None, description="BGP neighbor table."
    )
    neighbor_group: list[NeighborGroup] | None = Field(
        default=None, alias="neighbor-group", description="BGP neighbor table."
    )
    neighbor_range: list[NeighborRange] | None = Field(
        default=None,
        alias="neighbor-range",
        description="BGP IPv6 neighbor range table.",
    )
    network_import_check: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="network-import-check",
        description="Enable/disable ensure BGP network route exists in IGP.",
    )
    network: list[Network] | None = Field(
        default=None, description="BGP network table."
    )
    network6: list[Network6] | None = Field(
        default=None, description="BGP network table."
    )
    recursive_inherit_priority: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        alias="recursive-inherit-priority",
        description="Enable/disable priority inheritance for recursive resolution.",
    )
    recursive_next_hop: StatusEnum = Field(
        default=StatusEnum.ENABLE,
        alias="recursive-next-hop",
        description="Enable/disable recursive resolution of next-hop using BGP route.",
    )
    redistribute: list[Redistribute] | None = Field(
        default=None, description="BGP IPv4 redistribute table."
    )
    redistribute6: list[Redistribute] | None = Field(
        default=None, description="BGP IPv6 redistribute table. "
    )
    router_id: str = Field(alias="router-id")
    scan_time: int = Field(
        default=60,
        alias="scan-time",
        description="Background scanner interval (sec), 0 to disable it. ",
    )
    synchronization: StatusEnum = Field(
        default=StatusEnum.DISABLE,
        description="Enable/disable only advertise routes from iBGP if routes present in an IGP.",
    )
    tag_resolve_mode: TagResolveModeEnum = Field(
        default=TagResolveModeEnum.DISABLE,
        alias="tag-resolve-mode",
        description="Configure tag-match mode. Resolves BGP routes with other routes containing the "
        "same tag. disable:Disable tag-match mode. preferred:Use tag-match if a BGP route resolution "
        "with another route containing the same tag is successful. merge:Merge tag-match with best-match "
        "if they are using different routes. The result will exclude the next hops of tag-match whose "
        "interfaces have appeared in best-match. ",
    )
