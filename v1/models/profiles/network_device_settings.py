"""
Velocloud network based configuration module for device settings
"""

# pylint: disable=missing-docstring
# pylint: disable=line-too-long
from __future__ import annotations
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Authentication(BaseModel):
    ref: str | None = None


class Window(BaseModel):
    day: int | None = None
    begin_hour: int | None = Field(None, alias="beginHour")
    end_hour: int | None = Field(None, alias="endHour")


class SoftwareUpdate(BaseModel):
    windowed: bool | None = None
    window: Window | None = None


class Radio(BaseModel):
    radio_id: int | None = Field(None, alias="radioId")
    is_enabled: bool | None = Field(None, alias="isEnabled")
    name: str | None = None
    band: str | None = None
    channel: str | None = None
    width: str | None = None
    mode: str | None = None


class RadioSettings(BaseModel):
    country: str | None = None
    radios: list[Radio] | None = None


class L2Settings(BaseModel):
    override_arp_timeout: bool | None = Field(None, alias="overrideARPTimeout")
    arp_stale_timeout_minutes: int | None = Field(None, alias="arpStaleTimeoutMinutes")
    arp_dead_timeout_minutes: int | None = Field(None, alias="arpDeadTimeoutMinutes")
    arp_cleanup_timeout_minutes: int | None = Field(
        None, alias="arpCleanupTimeoutMinutes"
    )
    neighbor_discovery_reachable_time: int | None = Field(
        None, alias="neighborDiscoveryReachableTime"
    )


class AdvancedConfiguration(BaseModel):
    disable_all_i_pv6_traffic: bool | None = Field(None, alias="disableAllIPv6Traffic")
    drop_routing_header_type_zero_packets: bool | None = Field(
        None, alias="dropRoutingHeaderTypeZeroPackets"
    )
    enforce_extension_header_validation: bool | None = Field(
        None, alias="enforceExtensionHeaderValidation"
    )
    enforce_extension_header_order_check: bool | None = Field(
        None, alias="enforceExtensionHeaderOrderCheck"
    )
    dropn_log_packets_for_rfc_reserved_fields: bool | None = Field(
        None, alias="dropnLogPacketsForRFCReservedFields"
    )


class IcmpV6Messages(BaseModel):
    disable_destination_unreachable: bool | None = Field(
        None, alias="disableDestinationUnreachable"
    )
    disable_time_exceeded: bool | None = Field(None, alias="disableTimeExceeded")
    disable_parameter_problem: bool | None = Field(
        None, alias="disableParameterProblem"
    )


class DeviceSettingsGlobalIPv6Settings(BaseModel):
    advanced_configuration: AdvancedConfiguration | None = Field(
        None, alias="advancedConfiguration"
    )
    icmp_v6_messages: IcmpV6Messages | None = Field(None, alias="icmpV6Messages")


class Collector(BaseModel):
    address: str | None = None
    port: int | None = None


class Netflow1(BaseModel):
    enabled: bool | None = None
    version: int | None = None
    collectors: list[Collector] | None = None


class Vqm1(BaseModel):
    enabled: bool | None = None
    protocol: str | None = None
    collectors: list[Collector] | None = None


class DeviceSettingsSnmpv2c(BaseModel):
    enabled: bool | None = None
    community: str | None = None
    community_list: list[str] | None = Field(None, alias="communityList")
    allowed_ip: list[str] | None = Field(None, alias="allowedIp")


class User(BaseModel):
    name: str | None = None
    passphrase: str | None = "null"
    auth_alg: str | None = Field(None, alias="authAlg")
    privacy: bool | None = None
    authentication: bool | None = None
    encr_alg: str | None = Field(None, alias="encrAlg")


class Snmpv31(BaseModel):
    enabled: bool | None = None
    users: list[User] | None = None


class Snmp2(BaseModel):
    port: int | None = None
    snmpv2c: DeviceSettingsSnmpv2c | None = None
    snmpv3: Snmpv31 | None = None


class MultiSourceQos1(BaseModel):
    enabled: bool | None = None
    high_ratio: int | None = Field(None, alias="highRatio")
    normal_ratio: int | None = Field(None, alias="normalRatio")
    low_ratio: int | None = Field(None, alias="lowRatio")
    max_cap_threshold: int | None = Field(None, alias="maxCapThreshold")
    min_cap_threshold: int | None = Field(None, alias="minCapThreshold")


class Addressing4(BaseModel):
    type: str | None = None
    cidr_prefix: int | None = Field(None, alias="cidrPrefix")
    cidr_ip: str | None = Field(None, alias="cidrIp")
    netmask: str | None = None
    gateway: str | None = None


class L2(BaseModel):
    autonegotiation: bool | None = None
    speed: str | None = None
    duplex: str | None = None
    mtu: int | None = Field(None, alias="MTU")
    los_detection: bool | None = Field(None, alias="losDetection")
    probe_interval: str | None = Field(None, alias="probeInterval")


class InboundRouteLearning(BaseModel):
    default_action: str | None = Field(None, alias="defaultAction")
    filters: list[dict[str, Any]] | None = None


class OutboundRouteAdvertisement(BaseModel):
    default_action: str | None = Field(None, alias="defaultAction")
    filters: list[dict[str, Any]] | None = None


class Ospf3(BaseModel):
    enabled: bool | None = None
    area: str | None = None
    authentication: bool | None = None
    auth_id: int | None = Field(None, alias="authId")
    auth_passphrase: str | None = Field(None, alias="authPassphrase")
    hello_timer: int | None = Field(None, alias="helloTimer")
    dead_timer: int | None = Field(None, alias="deadTimer")
    mode: str | None = None
    md5_authentication: bool | None = Field(None, alias="md5Authentication")
    cost: int | None = None
    mtu: int | None = Field(None, alias="MTU")
    passive: bool | None = None
    inbound_route_learning: InboundRouteLearning | None = Field(
        None, alias="inboundRouteLearning"
    )
    outbound_route_advertisement: OutboundRouteAdvertisement | None = Field(
        None, alias="outboundRouteAdvertisement"
    )


class Rpf(str, Enum):
    SPECIFIC = "SPECIFIC"
    LOOSE = "LOOSE"
    DISABLED = "DISABLED"


class RoutedInterface1(BaseModel):
    name: str | None = None
    disabled: bool | None = None
    addressing: Addressing4 | None = None
    wan_overlay: str | None = Field(None, alias="wanOverlay")
    nat_direct: bool | None = Field(None, alias="natDirect")
    ospf: Ospf3 | None = None
    vlan_id: int | None = Field(None, alias="vlanId")
    l2: L2 | None = None
    underlay_accounting: bool | None = Field(True, alias="underlayAccounting")
    trusted: bool | None = None
    rpf: Rpf | None = None


class Interface(BaseModel):
    space: str | None = None
    name: str | None = None
    type: str | None = None
    cwp: bool | None = None
    port_mode: str | None = Field(None, alias="portMode")
    untagged_vlan: str | None = Field(None, alias="untaggedVlan")
    disabled: bool | None = None
    l2: L2 | None = None
    vlan_ids: list[int] | None = Field(None, alias="vlanIds")


class Lan2(BaseModel):
    interfaces: list[Interface] | None = None


class Virtual(BaseModel):
    routed_interfaces: list[RoutedInterface1] | None = Field(
        None, alias="routedInterfaces"
    )
    lan: Lan2 | None = None


class Models(BaseModel):
    virtual: Virtual | None = None


class LogicalidReference(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")


class Type15(str, Enum):
    EDGE_HUB = "edgeHub"
    EDGE_HUB_CLUSTER = "edgeHubCluster"


class DeviceSettingsVpnHub(LogicalidReference):
    name: str | None = None
    type: Type15 | None = None


class EdgeToEdgeHub(BaseModel):
    enabled: bool | None = None
    ref: str | None = None
    vpn_hubs: list[DeviceSettingsVpnHub] | None = Field(None, alias="vpnHubs")


class Dynamic1(BaseModel):
    enabled: bool | None = None
    type: str | None = None
    timeout: int | None = None


class EdgeToEdgeDetail1(BaseModel):
    use_cloud_gateway: bool | None = Field(None, alias="useCloudGateway")
    encryption_protocol: str | None = Field(None, alias="encryptionProtocol")
    dynamic: Dynamic1 | None = None
    vpn_hubs: list[DeviceSettingsVpnHub] | None = Field(None, alias="vpnHubs")
    auto_select_vpn_hubs: bool | None = Field(None, alias="autoSelectVpnHubs")


class Vpn1(BaseModel):
    enabled: bool | None = None
    edge_to_data_center: bool | None = Field(None, alias="edgeToDataCenter")
    ref: str | None = None
    edge_to_edge_hub: EdgeToEdgeHub | None = Field(None, alias="edgeToEdgeHub")
    edge_to_edge: bool | None = Field(None, alias="edgeToEdge")
    edge_to_edge_detail: EdgeToEdgeDetail1 | None = Field(
        None, alias="edgeToEdgeDetail"
    )
    conditional_backhaul: bool | None = Field(None, alias="conditionalBackhaul")
    back_haul_edges: list[DeviceSettingsVpnHub] | None = Field(
        None, alias="backHaulEdges"
    )


class Ospf2(BaseModel):
    enabled: bool | None = None
    areas: list[Area] | None = None


class Bgp2(BaseModel):
    enabled: bool | None = None
    asn: str | None = None
    neighbors: list[dict[str, Any]] | None = None


class Allocation(BaseModel):
    ref: str | None = None
    assignable_vlans: list[int] | None = Field(None, alias="assignableVlans")
    management_vlans: list[int] | None = Field(None, alias="managementVlans")


class Lan1(BaseModel):
    allocation: Allocation | None = None


class Area(BaseModel):
    id: int | None = None
    name: str | None = None
    type: str | None = None


class PrimaryProvider(BaseModel):
    ref: str | None = None


class BackupProvider(BaseModel):
    ref: str | None = None


class PrivateProviders(BaseModel):
    ref: str | None = None


class Dns2(BaseModel):
    primary_provider: PrimaryProvider | None = Field(None, alias="primaryProvider")
    backup_provider: BackupProvider | None = Field(None, alias="backupProvider")
    private_providers: PrivateProviders | None = Field(None, alias="privateProviders")


class DeviceSettingsData(BaseModel):
    authentication: Authentication | None = None
    bgp: Bgp2 | None = None
    dns: Dns2 | None = None
    global_i_pv6_settings: DeviceSettingsGlobalIPv6Settings | None = Field(
        None, alias="globalIPv6Settings"
    )
    l2_settings: L2Settings | None = Field(None, alias="l2Settings")
    lan: Lan1 | None = None
    models: Models | None = None
    multi_source_qos: MultiSourceQos1 | None = Field(None, alias="multiSourceQos")
    netflow: Netflow1 | None = None
    ospf: Ospf2 | None = None
    radio_settings: RadioSettings | None = Field(None, alias="radioSettings")
    snmp: Snmp2 | None = None
    software_update: SoftwareUpdate | None = Field(None, alias="softwareUpdate")
    vpn: Vpn1
    vqm: Vqm1
