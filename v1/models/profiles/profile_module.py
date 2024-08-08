"""
Velocloud V1 Profile/configuration module
"""
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
from __future__ import annotations
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address
from typing import Any

from pydantic import BaseModel, Extra, Field, constr

from common.southbound.velocloud.v1.models.profiles.business_policy import QOSData
from common.southbound.velocloud.v1.models.profiles.common_modules_entities import (
    Cloud,
    NvsFromEdgeSiteData,
)
from common.southbound.velocloud.v1.models.profiles.edge_device_settings import (
    EdgeDeviceSettingsData,
)
from common.southbound.velocloud.v1.models.profiles.firewall import FirewallData
from common.southbound.velocloud.v1.models.profiles.network_device_settings import (
    DeviceSettingsData,
)
from common.southbound.velocloud.v1.models.profiles.segment_device_settings import (
    SegmentBasedDeviceSettingsData,
)


class Name(str, Enum):
    """
    Module name
    """

    IMAGE_UPDATE = "imageUpdate"
    CONTROL_PLANE = "controlPlane"
    MANAGEMENT_PLANE = "managementPlane"
    FIREWALL = "firewall"
    QOS = "QOS"
    DEVICE_SETTINGS = "deviceSettings"
    WAN = "WAN"
    META_DATA = "metaData"
    PROPERTIES = "properties"
    ANALYTICS_SETTINGS = "analyticsSettings"
    ATP_METADATA = "atpMetadata"


class Type(str, Enum):

    """
    Module type
    """

    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class ConfigurationModule(BaseModel):
    """
    Profile/configuration module
    """

    configuration_id: int | None = Field(None, alias="configurationId")
    created: datetime | None = None
    data: (
        ManagementPlaneData
        | AnalyticsSettingsData
        | WANData
        | MetadataData
        | AtpmetadataData
        | ImageUpdateData
        | ControlPlaneData
        | DeviceSettingsData
        | EdgeDeviceSettingsData
        | FirewallData
        | QOSData
        | SegmentBasedDeviceSettingsData
        | dict[str, Any]
    ) = {}
    description: str | None = None
    effective: str | None = None
    enterprise_logical_id: str | None = Field(None, alias="enterpriseLogicalId")
    id: int | None = None
    metadata: dict[str, Any] | None = None
    modified: str | None = None
    name: Name
    refs: dict[str, Any] | None = None
    schema_version: str | None = Field(None, alias="schemaVersion")
    type: Type | None = None
    version: str | None = None


class PrimaryDetail2(BaseModel):
    ip_v4: str | None = Field(None, alias="ipV4")
    ip_v6: str | None = Field(None, alias="ipV6")
    fqdn: str | None = None


class SecondaryDetail1(BaseModel):
    ip_v4: str | None = Field(None, alias="ipV4")
    ip_v6: str | None = Field(None, alias="ipV6")
    fqdn: str | None = None


class ManagementPlaneProxy(BaseModel):
    primary: str | None = None
    secondary: str | None = None
    primary_detail: PrimaryDetail2 | None = Field(None, alias="primaryDetail")
    secondary_detail: SecondaryDetail1 | None = Field(None, alias="secondaryDetail")


class ManagementPlaneData(BaseModel):
    heart_beat_seconds: int = Field(..., alias="heartBeatSeconds")
    management_plane_proxy: ManagementPlaneProxy = Field(
        ..., alias="managementPlaneProxy"
    )
    stats_upload_seconds: int = Field(..., alias="statsUploadSeconds")
    time_slice_seconds: int = Field(..., alias="timeSliceSeconds")


class ManagementPlane(ConfigurationModule):
    data: ManagementPlaneData


class AnalyticsEndpoint(BaseModel):
    host: str | None = None
    cert: str | None = None
    is_dynamic_ip: bool | None = Field(None, alias="isDynamicIP")


class ConfigEndpoint(BaseModel):
    host: str | None = None
    cert: str | None = None


class AnalyticsSettingsData(BaseModel):
    mode: str
    company_id: str | None = Field(None, alias="companyId")
    company_secret: str | None = Field(None, alias="companySecret")
    enterprise_object_id: str | None = Field(None, alias="enterpriseObjectId")
    self_healing: bool | None = Field(None, alias="selfHealing")
    analytics_endpoint: AnalyticsEndpoint | None = Field(
        None, alias="analyticsEndpoint"
    )
    config_endpoint: ConfigEndpoint | None = Field(None, alias="configEndpoint")


class AnalyticsSettings(ConfigurationModule):
    data: AnalyticsSettingsData


class Discovery(str, Enum):
    DISABLED = "DISABLED"
    AUTO_DISCOVERED = "AUTO_DISCOVERED"
    USER_DEFINED = "USER_DEFINED"


class Mode3(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class Type23(str, Enum):
    WIRED = "WIRED"
    WIRELESS = "WIRELESS"


class AddressingVersion(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"
    I_PV4V6 = "IPv4v6"


class StaticSla(BaseModel):
    latency_ms: int | None = Field(None, alias="latencyMs")
    jitter_ms: int | None = Field(None, alias="jitterMs")
    loss_pct: int | None = Field(None, alias="lossPct")


class StaticSla1(BaseModel):
    latency_ms: int | None = Field(None, alias="latencyMs")
    jitter_ms: int | None = Field(None, alias="jitterMs")
    loss_pct: str | None = Field(None, alias="lossPct")


class ClassesOfServiceItem(BaseModel):
    id: str | None = None
    name: str | None = None
    dscp_tags: list[str] | None = Field(None, alias="dscpTags")
    static_sla: StaticSla1 | None = Field(None, alias="staticSLA")
    bandwidth_pct: int | None = Field(None, alias="bandwidthPct")
    bandwidth_guaranteed: bool | None = Field(None, alias="bandwidthGuaranteed")
    default_class_of_service: bool | None = Field(None, alias="defaultClassOfService")


class ClassesOfService(BaseModel):
    class_id: int | None = Field(None, alias="classId")
    classes_of_service: list[ClassesOfServiceItem] | None = Field(
        None, alias="classesOfService"
    )


class PrivateNetwork(BaseModel):
    id: int | None = None
    logical_id: str | None = Field(None, alias="logicalId")
    ref: constr(regex=r"wan:privateNetwork") | None = None


class Link1(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    internal_id: str | None = Field(None, alias="internalId")
    discovery: Discovery | None = None
    mode: Mode3 | None = None
    type: Type23 | None = None
    addressing_version: AddressingVersion | None = Field(
        None, alias="addressingVersion"
    )
    name: str | None = None
    isp: str | None = None
    public_ip_address: str | None = Field(None, alias="publicIpAddress")
    public_ip_address_v6: str | None = Field(None, alias="publicIpAddressV6")
    source_ip_address: str | None = Field(None, alias="sourceIpAddress")
    next_hop_ip_address: str | None = Field(None, alias="nextHopIpAddress")
    source_ip_address_v6: str | None = Field(None, alias="sourceIpAddressV6")
    next_hop_ip_address_v6: str | None = Field(None, alias="nextHopIpAddressV6")
    custom_vlan_id: bool | None = Field(None, alias="customVlanId")
    vlan_id: int | None = Field(None, alias="vlanId")
    enable8021_p: bool | None = Field(None, alias="enable8021P")
    priority8021_p: int | None = Field(None, alias="priority8021P")
    virtual_ip_address: str | None = Field(None, alias="virtualIpAddress")
    dynamic_bw_adjustment_enabled: bool | None = Field(
        None, alias="dynamicBwAdjustmentEnabled"
    )
    bw_measurement: str | None = Field(None, alias="bwMeasurement")
    upstream_mbps: str | None = Field(None, alias="upstreamMbps")
    downstream_mbps: str | None = Field(None, alias="downstreamMbps")
    backup_only: bool | None = Field(None, alias="backupOnly")
    hot_standby: bool | None = Field(None, alias="hotStandby")
    min_active_links: int | None = Field(None, alias="minActiveLinks")
    overhead_bytes: int | None = Field(None, alias="overheadBytes")
    udp_hole_punching: bool | None = Field(None, alias="udpHolePunching")
    mtu: int | None = Field(None, alias="MTU")
    pmtud_disabled: bool | None = Field(None, alias="pmtudDisabled")
    mpls_network: str | None = Field(None, alias="mplsNetwork")
    dscp_tag: str | None = Field(None, alias="dscpTag")
    static_sla_enabled: bool | None = Field(None, alias="staticSlaEnabled")
    classesof_service_enabled: bool | None = Field(
        None, alias="classesofServiceEnabled"
    )
    strict_ip_precedence: bool | None = Field(None, alias="strictIpPrecedence")
    encrypt_overlay: bool | None = Field(None, alias="encryptOverlay")
    static_sla: StaticSla | None = Field(None, alias="staticSLA")
    classes_of_service: ClassesOfService | None = Field(None, alias="classesOfService")
    interfaces: list[str] | None = None
    last_active: str | None = Field(None, alias="lastActive")
    private_network: PrivateNetwork | None = Field(None, alias="privateNetwork")


class Network3(BaseModel):
    mode: str | None = None
    type: str | None = None
    name: str | None = None
    logical_id: str | None = Field(None, alias="logicalId")
    interface: str | None = None
    internal_id: str | None = Field(None, alias="internalId")
    ip_address: str | None = Field(None, alias="ipAddress")
    isp: str | None = None
    last_active: int | None = Field(None, alias="lastActive")


class WANData(BaseModel):
    links: list[Link1]
    networks: list[Network3]


class PrivateNetworkRef(BaseModel):
    wan_private_network: dict[str, Any] | None = Field(None, alias="wan:privateNetwork")


class WanRefs(PrivateNetworkRef):
    pass


class WAN(ConfigurationModule):
    data: WANData
    refs: WanRefs | None = None


class Applications(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    type: str | None = None
    version: str | None = None


class MetadataData(BaseModel):
    applications: Applications


class MetaData2(ConfigurationModule):
    data: MetadataData


class IdpsSignature(BaseModel):
    auto_update: bool | None = Field(None, alias="autoUpdate")
    logical_id: str | None = Field(None, alias="logicalId")
    checksum: str | None = None
    checksum_type: str | None = Field(None, alias="checksumType")
    version: str | None = None


class AtpmetadataData(BaseModel):
    class Config:
        extra = Extra.forbid

    atp_update_enabled: bool = Field(alias="atpUpdateEnabled")
    idps_signature: IdpsSignature = Field(alias="idpsSignature")


class AtpMetadata(ConfigurationModule):
    data: AtpmetadataData


class ImageUpdateScheduledTime(BaseModel):
    day_of_week: int = Field(..., alias="dayOfWeek")
    specified: bool
    time_of_day_mins: int = Field(..., alias="timeOfDayMins")
    use_edge_time_zone: bool = Field(..., alias="useEdgeTimeZone")


class FirmwareImageUpdateData(BaseModel):
    build_number: str = Field(..., alias="buildNumber")
    profile_device_family: str = Field(..., alias="profileDeviceFamily")
    profile_version: str = Field(..., alias="profileVersion")
    software_package_id: int = Field(..., alias="softwarePackageId")
    software_package_name: str = Field(..., alias="softwarePackageName")
    version: str
    window_duration_mins: int = Field(..., alias="windowDurationMins")
    windowed: bool
    devicefamily: list[str]


class ImageUpdateData(BaseModel):
    build_number: str = Field(alias="buildNumber")
    profile_device_family: str = Field(alias="profileDeviceFamily")
    profile_version: str = Field(alias="profileVersion")
    scheduled_start_time: ImageUpdateScheduledTime | None = Field(
        None, alias="scheduledStartTime"
    )
    software_package_id: int = Field(..., alias="softwarePackageId")
    software_package_name: str = Field(..., alias="softwarePackageName")
    version: str
    window_duration_mins: int = Field(..., alias="windowDurationMins")
    windowed: bool
    devicefamily: list[str]
    modem_firmware: FirmwareImageUpdateData = Field(..., alias="modemFirmware")
    platform_firmware: FirmwareImageUpdateData = Field(..., alias="platformFirmware")
    factory_firmware: FirmwareImageUpdateData = Field(..., alias="factoryFirmware")


class ImageUpdate(ConfigurationModule):
    data: ImageUpdateData


class PrimaryDetail(BaseModel):
    name: str
    policy_id: str = Field(..., alias="policyId")


class CloudWebSecurityPolicy(BaseModel):
    logical_id: str = Field(..., alias="logicalId")
    primary_detail: PrimaryDetail | None = Field(None, alias="primaryDetail")


class PrimaryDetail1(BaseModel):
    ip_address: str = Field(..., alias="ipAddress")
    logical_id: str = Field(..., alias="logicalId")
    name: str


class SecondaryDetail(BaseModel):
    ip_address: str = Field(..., alias="ipAddress")
    logical_id: str = Field(..., alias="logicalId")
    name: str


class PrimaryCciDetail(BaseModel):
    ip_address: str = Field(..., alias="ipAddress")
    logical_id: str = Field(..., alias="logicalId")
    name: str
    ip_v6_address: str | None = Field(None, alias="ipV6Address")


class SecondaryCciDetail(BaseModel):
    ip_address: str = Field(..., alias="ipAddress")
    logical_id: str = Field(..., alias="logicalId")
    name: str
    ip_v6_address: str | None = Field(None, alias="ipV6Address")


class SuperDetail(BaseModel):
    ip_address: str | None = Field(None, alias="ipAddress")
    logical_id: str | None = Field(None, alias="logicalId")
    name: str | None = None


class GatewaySelection(BaseModel):
    mode: str | None = None
    primary: str | None = None
    primary_detail: PrimaryDetail1 | None = Field(None, alias="primaryDetail")
    secondary: str | None = None
    secondary_detail: SecondaryDetail | None = Field(None, alias="secondaryDetail")
    primary_cci: str | None = Field(None, alias="primaryCCI")
    primary_cci_detail: PrimaryCciDetail | None = Field(None, alias="primaryCCIDetail")
    secondary_cci: str | None = Field(None, alias="secondaryCCI")
    secondary_cci_detail: SecondaryCciDetail | None = Field(
        None, alias="secondaryCCIDetail"
    )
    super: str | None = None
    super_detail: SuperDetail | None = Field(None, alias="superDetail")


class BackHaulEdge(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    name: str | None = None


class DataCenterEdge(BaseModel):
    logical_id: str | None = Field(None, alias="logicalId")
    name: str | None = None


class Dynamic(BaseModel):
    enabled: bool | None = None
    timeout: int | None = None
    type: str | None = None


class ProfileIsolation(BaseModel):
    enabled: bool | None = None
    isolate_dynamic: bool | None = Field(None, alias="isolateDynamic")


class EdgeToEdgeDetail(BaseModel):
    dynamic: Dynamic | None = None
    encryption_protocol: str | None = Field(None, alias="encryptionProtocol")
    profile_isolation: ProfileIsolation | None = Field(None, alias="profileIsolation")
    use_cloud_gateway: bool | None = Field(None, alias="useCloudGateway")
    vpn_hubs: list[dict[str, Any]] | None = Field(None, alias="vpnHubs")
    auto_select_vpn_hubs: bool | None = Field(None, alias="autoSelectVpnHubs")


class EdgeToEdgeListItem(BaseModel):
    isolate_dynamic: int | None = Field(None, alias="isolateDynamic")
    logical_id: str | None = Field(None, alias="logicalId")
    name: str | None = None
    profile_logical_id: str | None = Field(None, alias="profileLogicalId")


class Vpn(BaseModel):
    conditional_backhaul: bool | None = Field(None, alias="conditionalBackhaul")
    back_haul_edges: list[BackHaulEdge] | None = Field(None, alias="backHaulEdges")
    data_center_edges: list[DataCenterEdge] | None = Field(
        None, alias="dataCenterEdges"
    )
    edge_to_data_center: bool | None = Field(None, alias="edgeToDataCenter")
    edge_to_edge: bool | None = Field(None, alias="edgeToEdge")
    edge_to_edge_detail: EdgeToEdgeDetail | None = Field(None, alias="edgeToEdgeDetail")
    edge_to_edge_list: list[EdgeToEdgeListItem] | None = Field(
        None, alias="edgeToEdgeList"
    )


class Provider(str, Enum):
    GENERIC_IK_EV2_ROUTER = "genericIKEv2Router"
    GENERIC_IK_EV1_ROUTER = "genericIKEv1Router"
    MICROSOFT_AZURE_VIRTUAL_WAN = "microsoftAzureVirtualWan"
    ZSCALER = "Zscaler"
    GENERIC_GRE = "genericGRE"
    AWS_TRANSIT_GATEWAY = "AWSTransitGateway"
    SSE = "sse"


class Type4(str, Enum):
    GENERIC_IK_EV2_ROUTER = "genericIKEv2Router"
    GENERIC_IK_EV1_ROUTER = "genericIKEv1Router"
    MICROSOFT_AZURE_VIRTUAL_WAN = "microsoftAzureVirtualWan"
    ZSCALER = "Zscaler"
    GENERIC_GRE = "genericGRE"
    AWS_TRANSIT_GATEWAY = "AWSTransitGateway"
    SSE = "sse"


class AddressFamily(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"
    I_PV4V6 = "IPv4v6"


class ProviderCategory(str, Enum):
    DATACENTER = "DATACENTER"
    CSS = "CSS"


class TunnelingProtocol(str, Enum):
    IPSEC = "IPSEC"
    GRE = "GRE"


class Bgp3(BaseModel):
    enabled: bool | None = None


class AuthenticationAlgorithm(str, Enum):
    ANY = "Any"
    MD5 = "MD5"
    SHA_1 = "SHA_1"
    SHA_256 = "SHA_256"


class EncryptionAlgorithm(str, Enum):
    ANY = "Any"
    AES_128_CBC = "AES_128_CBC"
    AES_192_CBC = "AES_192_CBC"
    AES_256_CBC = "AES_256_CBC"
    AES_128_GCM = "AES_128_GCM"
    AES_192_GCM = "AES_192_GCM"
    AES_256_GCM = "AES_256_GCM"
    NONE = "NONE"


class IkeIdType(str, Enum):
    IPV4_ADDR = "IPV4_ADDR"
    FQDN = "FQDN"
    USER_FQDN = "USER_FQDN"


class PeerIkeId(BaseModel):
    ike_id: str | None = Field(None, alias="ikeId")
    ike_id_type: IkeIdType | None = Field(None, alias="ikeIdType")


class Ikeprop1(BaseModel):
    dh_group: int | None = Field(None, alias="DHGroup")
    pfs: int | None = Field(None, alias="PFS")
    authentication_algorithm: AuthenticationAlgorithm | None = Field(
        None, alias="authenticationAlgorithm"
    )
    authentication_method: str | None = Field(None, alias="authenticationMethod")
    dpd_timeout_seconds: int | None = Field(None, alias="dpdTimeoutSeconds")
    encryption_algorithm: EncryptionAlgorithm | None = Field(
        None, alias="encryptionAlgorithm"
    )
    ikev1_main_mode: bool | None = Field(None, alias="ikev1MainMode")
    life_time_seconds: int | None = Field(None, alias="lifeTimeSeconds")
    peer_ike_id: PeerIkeId | None = Field(None, alias="peerIkeId")
    protocol_version: int | None = Field(None, alias="protocolVersion")


class IpsecTunnelType(str, Enum):
    ROUTE = "ROUTE"
    POLICY = "POLICY"


class Protocol4(str, Enum):
    ESP_AUTH = "ESP_AUTH"
    ESP_NULL = "ESP_NULL"


class Ipsecprop(BaseModel):
    authentication_algorithm: str | None = Field(None, alias="authenticationAlgorithm")
    encryption_algorithm: EncryptionAlgorithm | None = Field(
        None, alias="encryptionAlgorithm"
    )
    ipsec_tunnel_type: IpsecTunnelType | None = Field(None, alias="ipsecTunnelType")
    life_time_seconds: int | None = Field(None, alias="lifeTimeSeconds")
    re_key_timer: int | None = Field(None, alias="reKeyTimer")
    protocol: Protocol4 | None = None
    dpd_timeout_seconds: int | None = Field(None, alias="dpdTimeoutSeconds")
    dpd_type: str | None = Field(None, alias="dpdType")


class NvsFromEdgeServiceProviderServerConfig(BaseModel):
    ikeprop: Ikeprop1 | None = Field(None, alias="IKEPROP")
    ipsecprop: Ipsecprop | None = Field(None, alias="IPSECPROP")
    local_link_ip: str | None = Field(None, alias="localLinkIp")
    nvs_public_ip: str | None = Field(None, alias="nvsPublicIp")
    peer_link_ip: str | None = Field(None, alias="peerLinkIp")


class NvsFromEdgeServiceProviderSubnet(BaseModel):
    advertise: bool | None = None
    cidr_ip: IPv4Address | None = Field(None, alias="cidrIp")
    metric: int | None = None
    name: str | None = None
    cidr_prefix: str | None = Field(None, alias="cidrPrefix")
    net_mask: IPv4Address | None = Field(None, alias="netMask")


class SourceSubnets(BaseModel):
    subnets: list[NvsFromEdgeServiceProviderSubnet] | None = None


class PeerSubnets(BaseModel):
    always_reachable: bool | None = Field(None, alias="alwaysReachable")
    subnets: list[NvsFromEdgeServiceProviderSubnet] | None = None
    version: str | None = None


class VpnCredentialsWithlinks(BaseModel):
    use_all_public_wan_links: bool | None = Field(None, alias="useAllPublicWanLinks")
    links: list[NvsFromEdgeSiteData] | None = None


class Bgp(BaseModel):
    enabled: bool | None = None


class ControlPlaneDataNvsFromEdgeProvider(BaseModel):
    enabled: bool | None = None
    provider: Provider | None = None
    type: Type4 | None = None
    address_family: AddressFamily | None = Field(None, alias="addressFamily")
    automate_deployment: bool | None = Field(None, alias="automateDeployment")
    provider_category: ProviderCategory | None = Field(None, alias="providerCategory")
    routing_policy: str | None = Field(None, alias="routingPolicy")
    tunneling_protocol: TunnelingProtocol | None = Field(
        None, alias="tunnelingProtocol"
    )
    shared_ike_auth: bool | None = Field(None, alias="sharedIkeAuth")
    source_subnets: SourceSubnets | None = Field(None, alias="sourceSubnets")
    peer_subnets: PeerSubnets | None = Field(None, alias="peerSubnets")
    bgp: Bgp | None = None
    primary_server: NvsFromEdgeServiceProviderServerConfig | None = Field(
        None, alias="primaryServer"
    )
    backup_server: NvsFromEdgeServiceProviderServerConfig | None = Field(
        None, alias="backupServer"
    )
    keep_backup_server_connected: bool | None = Field(
        None, alias="keepBackupServerConnected"
    )
    version: str | None = None
    vpn_credentials_withlinks: VpnCredentialsWithlinks | None = Field(
        None, alias="vpnCredentialsWithlinks"
    )


class NvsFromEdge(BaseModel):
    enabled: bool | None = None
    providers: list[ControlPlaneDataNvsFromEdgeProvider] | None = None


class IpsecGatewayDetail(BaseModel):
    enabled: bool | None = None
    strict_host_check: bool | None = Field(None, alias="strictHostCheck")
    strict_host_check_dn: str | None = Field(None, alias="strictHostCheckDN")


class Vendor1(str, Enum):
    ZSCALER_MT_GRE = "zscalerMtGRE"


class CciItem(BaseModel):
    vendor: Vendor1 | None = None
    provider_logical_id: str | None = Field(None, alias="providerLogicalId")
    cloud: Cloud | None = None
    location_id: int | None = Field(None, alias="locationId")
    user_fqdn: str | None = Field(None, alias="userFqdn")
    user_psk: str | None = Field(None, alias="userPsk")


class ControlPlaneData(BaseModel):
    cloud_web_security_policies: list[CloudWebSecurityPolicy] | None = Field(
        None, alias="cloudWebSecurityPolicies"
    )
    gateway_selection: GatewaySelection = Field(alias="gatewaySelection")
    vpn: Vpn | None = None
    nvs_from_edge: NvsFromEdge | None = Field(None, alias="nvsFromEdge")
    ipsec_gateway_detail: dict[str, IpsecGatewayDetail] = Field(
        alias="ipsecGatewayDetail"
    )
    cci: list[CciItem] | None = None


class ControlPlane(ConfigurationModule):
    data: ControlPlaneData


class DeviceSettingsRefs(BaseModel):
    device_settings_authentication: dict[str, Any] | None = Field(
        None, alias="deviceSettings:authentication"
    )
    device_settings_css_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:css:provider"
    )
    device_settings_secure_access_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:secureAccess:provider"
    )
    device_settings_css_site: dict[str, Any] | None = Field(
        None, alias="deviceSettings:css:site"
    )
    device_settings_edge_direct_nvs_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:edgeDirectNvs:provider"
    )
    device_settings_edge_direct_nvs_site: dict[str, Any] | None = Field(
        None, alias="deviceSettings:edgeDirectNvs:site"
    )
    device_settings_zscaler_iaas_subscription: dict[str, Any] | None = Field(
        None, alias="deviceSettings:zscaler:iaasSubscription"
    )
    device_settings_zscaler_mtgre_site: dict[str, Any] | None = Field(
        None, alias="deviceSettings:zscaler:mtgreSite"
    )
    device_settings_zscaler_location: dict[str, Any] | None = Field(
        None, alias="deviceSettings:zscaler:location"
    )
    device_settings_zscaler_sub_location: dict[str, Any] | None = Field(
        None, alias="deviceSettings:zscaler:subLocation"
    )
    device_settings_dns_backup_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:dns:backupProvider"
    )
    device_settings_dns_primary_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:dns:primaryProvider"
    )
    device_settings_dns_private_providers: dict[str, Any] | None = Field(
        None, alias="deviceSettings:dns:privateProviders"
    )
    device_settings_hand_off_gateways_gateways: dict[str, Any] | None = Field(
        None, alias="deviceSettings:handOffGateways:gateways"
    )
    device_settings_lan_allocation: dict[str, Any] | None = Field(
        None, alias="deviceSettings:lan:allocation"
    )
    device_settings_security_vnf_license: dict[str, Any] | None = Field(
        None, alias="deviceSettings:securityVnf:license"
    )
    device_settings_security_vnf_service: dict[str, Any] | None = Field(
        None, alias="deviceSettings:securityVnf:service"
    )
    device_settings_segment: dict[str, Any] | None = Field(
        None, alias="deviceSettings:segment"
    )
    device_settings_segment_netflow_collectors: dict[str, Any] | None = Field(
        None, alias="deviceSettings:segment:netflowCollectors"
    )
    device_settings_segment_netflow_filters: dict[str, Any] | None = Field(
        None, alias="deviceSettings:segment:netflowFilters"
    )
    device_settings_tacacs: dict[str, Any] | None = Field(
        None, alias="deviceSettings:tacacs"
    )
    device_settings_vnfs_edge: dict[str, Any] | None = Field(
        None, alias="deviceSettings:vnfs:edge"
    )
    device_settings_vnfs_vnf_image: dict[str, Any] | None = Field(
        None, alias="deviceSettings:vnfs:vnfImage"
    )
    device_settings_vpn_data_center: dict[str, Any] | None = Field(
        None, alias="deviceSettings:vpn:dataCenter"
    )
    device_settings_vpn_edge_hub: dict[str, Any] | None = Field(
        None, alias="deviceSettings:vpn:edgeHub"
    )
    device_settings_vpn_edge_hub_cluster: dict[str, Any] | None = Field(
        None, alias="deviceSettings:vpn:edgeHubCluster"
    )
    device_settings_web_proxy_provider: dict[str, Any] | None = Field(
        None, alias="deviceSettings:webProxy:provider"
    )


ConfigurationModule.update_forward_refs()
