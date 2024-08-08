"""
Velocloud profile business policy settings section
"""
# pylint: disable=missing-docstring

from __future__ import annotations
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from common.southbound.velocloud.v1.models.profiles.firewall import (
    DRuleType,
    IpVersion,
    SRuleType,
)


class MetdataType(str, Enum):
    REGULAR = "REGULAR"
    CDE = "CDE"
    PRIVATE = "PRIVATE"


class ConfigurationModuleSegmentMetadata(BaseModel):
    name: str | None = None
    segment_id: int | None = Field(None, alias="segmentId")
    segment_logical_id: str | None = Field(None, alias="segmentLogicalId")
    type: MetdataType | None = None


class ServiceRateLimit(BaseModel):
    enabled: bool
    input_type: str | None = Field(None, alias="inputType")
    value: int | None = None


class RouteActionObject(BaseModel):
    interface: str | None = None
    link_internal_logical_id: str | None = Field(None, alias="linkInternalLogicalId")
    link_policy: str | None = Field(None, alias="linkPolicy")
    route_cfg: dict[str, Any] | None = Field(None, alias="routeCfg")
    route_policy: str | None = Field(None, alias="routePolicy")
    service_group: str | None = Field(None, alias="serviceGroup")
    vlan_id: int | None = Field(None, alias="vlanId")
    wanlink: str | None = None
    link_cos_logical_id: str | None = Field(None, alias="linkCosLogicalId")
    link_outer_dscp_tag: str | None = Field(None, alias="linkOuterDscpTag")
    link_inner_dscp_tag: str | None = Field(None, alias="linkInnerDscpTag")


class NatIpVersion(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"
    I_PV4V6 = "IPv4v6"


class NatObject(BaseModel):
    source_ip: str | None = Field(None, alias="sourceIp")
    dest_ip: str | None = Field(None, alias="destIp")


class Action3(BaseModel):
    route_type: str | None = Field(None, alias="routeType")
    allow_conditional_bh: bool | None = Field(None, alias="allowConditionalBh")
    user_disable_conditional_bh: bool | None = Field(
        None, alias="userDisableConditionalBh"
    )
    edge2_edge_route_action: RouteActionObject | None = Field(
        None, alias="edge2EdgeRouteAction"
    )
    edge2_data_center_route_action: RouteActionObject | None = Field(
        None, alias="edge2DataCenterRouteAction"
    )
    edge2_cloud_route_action: RouteActionObject | None = Field(
        None, alias="edge2CloudRouteAction"
    )
    qo_s: dict[str, Any] | None = Field(None, alias="QoS")
    sla: dict[str, Any] | None = None
    nat: NatObject | None = None
    nat_ip_version: NatIpVersion | None = Field(None, alias="natIpVersion")
    """
    NatIp Version same as ipVersion
    """
    nat_v6: NatObject | None = Field(None, alias="natV6")


class Match(BaseModel):
    appid: int | None = None
    classid: int | None = None
    dscp: int | None = Field(
        None,
        description="Integer ID indicating DSCP"
        "classification, where mappings are as follows:"
        " [EF:46,VA:44,AF11:10,"
        "AF12:12,AF13:14,AF21:18,AF22:20,AF23:22,AF31:26,AF32:28,AF33:30,AF41:34,"
        "AF42:36,AF43:38,CS0:0,CS1:8,CS2:16,CS3:24,CS4:32,CS5:40,CS6:48,CS7:56]",
    )

    ip_version: IpVersion | None = Field(
        None, alias="ipVersion", description="Ip Version /Addressing Version"
    )
    sip: str | None = None
    sip_v6: str | None = Field(None, alias="sipV6", description="Source IPv6 address")

    sport_high: int | None = None
    sport_low: int | None = None
    s_address_group: str | None = Field(
        None, alias="sAddressGroup", description="Source address group reference"
    )
    s_port_group: str | None = Field(
        None, alias="sPortGroup", description="Source port group reference"
    )
    ssm: str | None = None
    svlan: int | None = None
    s_interface: str | None = Field(None, alias="sInterface")
    os_version: int | None = Field(
        None,
        description="Index corresponding"
        " to the OS in the array: [OTHER,WINDOWS,LINUX,MACOS,IOS,ANDROID,EDGE]",
    )
    hostname: str | None = None
    dip: str | None = None
    dip_v6: str | None = Field(
        None, alias="dipV6", description="Destination IPv6 address"
    )
    dport_low: int | None = None
    dport_high: int | None = None
    d_address_group: str | None = Field(
        None, alias="dAddressGroup", description="Destination address group reference"
    )
    d_port_group: str | None = Field(
        None, alias="dPortGroup", description="Destination port group reference"
    )
    dsm: str | None = None
    dvlan: int | None = None
    proto: int | None = None
    s_rule_type: SRuleType | None = None
    d_rule_type: DRuleType | None = None


class QOSBusinessRules(BaseModel):
    name: str | None = None
    match: Match | None = None
    action: Action3 | None = None
    rule_logical_id: str | None = Field(None, alias="ruleLogicalId")
    """
    Globally unique identifier for the policy rule
    """


class WebProxy(BaseModel):
    providers: list[dict[str, Any]] | None = None


class CosMappingValue(BaseModel):
    value: int | None = None
    ratelimit: bool | None = None


class CosMapping(BaseModel):
    high: CosMappingValue | None = None
    normal: CosMappingValue | None = None
    low: CosMappingValue | None = None


class CosMappingModel(BaseModel):
    ls_input_type: str | None = Field(None, alias="lsInputType")
    bulk: CosMapping | None = None
    realtime: CosMapping | None = None
    transactional: CosMapping | None = None


class QOSSegments(BaseModel):
    rules: list[QOSBusinessRules]
    defaults: list[QOSBusinessRules] | None = None
    web_proxy: WebProxy = Field(..., alias="webProxy")
    cos_mapping: CosMappingModel | None = Field(None, alias="cosMapping")
    segment: ConfigurationModuleSegmentMetadata


class QoeMappingValue(BaseModel):
    yellow: float
    red: float


class QoeMappingType(BaseModel):
    latency: QoeMappingValue


class QoeObject(BaseModel):
    voice: QoeMappingType
    video: QoeMappingType
    trans: QoeMappingType


class QOSData(BaseModel):
    service_rate_limit: ServiceRateLimit = Field(alias="serviceRateLimit")
    segments: list[QOSSegments]
    qoe: QoeObject | None


class QOSRefs(BaseModel):
    device_settings_back_haul_edge: dict[str, Any] | None = Field(
        None, alias="deviceSettings:backHaulEdge"
    )
    device_settings_data_center: dict[str, Any] | None = Field(
        None, alias="deviceSettings:dataCenter"
    )
