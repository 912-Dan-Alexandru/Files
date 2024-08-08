"""
Generated using datamodel-codegen
Meraki Network
"""

from enum import Enum
from typing import Any, TypeAlias

from pydantic import BaseModel, Field, create_model, validator

from common.models.characteristic import SpecificationCharacteristic


class ProductTypes(str, Enum):
    """
    Meraki Product Types
    """

    APPLIANCE = "appliance"
    CAMERA = "camera"
    CELLULAR_GATEWAY = "cellularGateway"
    SENSOR = "sensor"
    SWITCH = "switch"
    SYSTEMS_MANAGER = "systemsManager"
    WIRELESS = "wireless"
    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


class EnabledStatus(BaseModel):
    """
    EnabledStatus
    """

    enabled: bool


class NetworkBaseModel(BaseModel, use_enum_values=True):
    """
    Base Model for Meraki Networks
    """

    name: str | None = None
    tags: list[str] | None = None
    timeZone: str | None = None
    notes: str | None = None


class NetworkBase(NetworkBaseModel, use_enum_values=True):
    """
    Base Model for Meraki Networks
    """

    productTypes: list[ProductTypes]


class LocalStatusPageAuthenticationGET(BaseModel):
    """
    LocalStatusPageAuthenticationGET - only username and enabled is returned on GET
    """

    enabled: bool
    username: str | None


class LocalStatusPageAuthenticationPUT(BaseModel):
    """
    LocalStatusPageAuthenticationPUT - only password and enabled can be passed in PUT
    """

    enabled: bool | None
    password: str | None


class LocalStatusPageGET(BaseModel):
    """
    LocalStatusPageGET
    """

    authentication: LocalStatusPageAuthenticationGET


class LocalStatusPagePUT(BaseModel):
    """
    LocalStatusPagePUT
    """

    authentication: LocalStatusPageAuthenticationPUT


class NetworkSettingsGET(BaseModel):
    """
    NetworkSettingsGET
    """

    localStatusPage: LocalStatusPageGET


class NetworkSettingsPUT(BaseModel):
    """
    NetworkSettingsPUT
    """

    localStatusPage: LocalStatusPagePUT


class Network(NetworkBase):
    """
    Meraki Network Model
    """

    id: str
    enrollmentString: str | None = None
    url: str
    isBoundToConfigTemplate: bool
    configTemplateId: str | None = None
    organizationId: str
    type: str | None = None
    networkSettings: NetworkSettingsGET | None


class ApplianceRoutingMode(str, Enum):
    """LAN/VLAN mode for appliance routing"""

    ROUTED_LAN = "lan"
    ROUTED_VLAN = "vlan"
    PASSTHROUGH = "passthrough"


class NetworkCreate(NetworkBase):
    """
    Payload for organizations.create_network
    """

    copyFromNetworkId: str | None = None
    routingMode: ApplianceRoutingMode = Field(
        default=ApplianceRoutingMode.ROUTED_LAN,
        description="By default,"
        + "each Meraki network is created in ROUTED deployment mode"
        + " and Single LAN setup",
    )
    networkSettings: NetworkSettingsGET | None


class NetworkUpdate(NetworkBaseModel):
    """
    Payload for organizations.create_network
    """

    name: str | None = None
    enrollmentString: str | None = None


class NetworkBindingOptions(BaseModel):
    """options used while binding or unbinding"""

    retain_configuration: bool = Field(
        default=False,
        description="whether network configuration was retained upon unbinding action",
    )

    auto_bind_switch_profiles: bool = Field(
        default=False,
        description="whether switch profiles should automatically be bound as well",
    )


class NetworkBinding(BaseModel):
    """represents binding status between network and templates"""

    enabled: bool = Field(
        default=False, description="whether this network is bound or not to a template"
    )

    template: str | None = Field(
        default=None, description="template the network is currently bound to"
    )

    options: NetworkBindingOptions | None = Field(
        default=None,
        description="during binding or unbinding actions, options can be specified",
    )


class NetworkBindingRequest(BaseModel):
    """
    Payload to interpret requests to bind/unbind
    network to templates
    """

    binding: NetworkBinding | None = Field(
        default=None, description="binding configuration for the network"
    )


class Origin(BaseModel):
    """
    Origin
    """

    type: str
    interfaces: list[str]


class PrefixAssignments(BaseModel):
    """
    Base Prefix Assignments
    """

    enabled: bool | None = None
    disabled: bool | None = None
    staticApplianceIp6: str | None = None
    staticPrefix: str | None = None
    autonomous: bool | None = None
    origin: Origin | None = None


class IPv6Lan(BaseModel):
    """
    IPv6Lan
    """

    enabled: bool
    prefixAssignments: list[PrefixAssignments] | None


class IPv6VLANs(BaseModel):
    """
    IPv6VLANs
    """

    enabled: bool
    prefixAssignments: list[PrefixAssignments] | None = None


class MacMapping(BaseModel):
    """
    MacMapping
    """

    ip: str
    name: str


class HarlockMacMapping(BaseModel):
    """
    HarlockMacMapping
    """

    mac_address: str
    ip: str
    name: str


class DhcpOption(BaseModel):
    """
    DhcpOption
    """

    code: str
    type: str
    value: str


class ReservedIpRange(BaseModel):
    """
    ReservedIpRange
    """

    start: str
    end: str
    comment: str


class DhcpHandling(str, Enum):
    """
    DhcpHandling values
    """

    NOT_RESPOND = "Do not respond to DHCP requests"
    RUN_DHCP = "Run a DHCP server"
    RELAY_DHCP = "Relay DHCP to another server"


class VlanDhcp(BaseModel):
    """
    VlanDhcp
    """

    dhcpBootFilename: str | None = None
    dhcpBootNextServer: str | None = None
    dhcpHandling: DhcpHandling | None = None
    dhcpLeaseTime: str | None = None
    dhcpBootOptionsEnabled: bool | None = None
    dhcpRelayServerIps: list[str] | None = None
    dhcpOptions: list[DhcpOption] | None = None


FixedIpAssignmentsMeraki: TypeAlias = dict[str, MacMapping]
FixedIpAssignmentsHarlock: TypeAlias = list[HarlockMacMapping]


class BaseVlan(BaseModel):
    """
    BaseVlan
    """

    id: str
    name: str
    mask: int | None = None
    applianceIp: str
    cidr: str | None = None
    groupPolicyId: str | None = None
    subnet: str | None = None
    templateVlanType: str | None = None
    vpnNatSubnet: str | None = None
    dnsNameservers: str
    ipv6: IPv6VLANs | None = None
    reservedIpRanges: list[ReservedIpRange] | None = None


class SingleLan(BaseModel):
    """
    Single Lan Model
    """

    appliance_ip: str | None = Field(alias="applianceIp", default=None)
    subnet: str | None = None
    ipv6: IPv6Lan | None = None
    mandatory_dhcp: EnabledStatus | None = Field(alias="mandatoryDhcp", default=None)


class VLANGetResponse(BaseVlan, VlanDhcp):
    """
    VLANGetResponse
    """

    fixedIpAssignments: FixedIpAssignmentsMeraki | None = None


class PortUpdate(BaseModel):
    """
    PortUpdate
    """

    enabled: bool | None = None
    type: str | None = None
    dropUntaggedTraffic: bool | None = None
    vlan: int | None = None
    allowedVlans: str | None = None
    accessPolicy: str | None = None


class PortGetResponse(PortUpdate):
    """
    PortsGetResponse
    """

    number: int


class NetworkApplianceVlansSettings(BaseModel):
    """
    NetworkApplianceVlansSettings
    """

    vlansEnabled: bool


class VlanHarlockCharacteristics(BaseVlan):
    """
    VlanCharacteristics
    """

    uuid: str
    dhcp: VlanDhcp | None = None
    fixedIpAssignments: FixedIpAssignmentsHarlock | None = None


class PortCharacteristics(PortGetResponse):
    """
    PortCharacteristics
    """

    uuid: str


class CreateVlan(BaseModel):
    """
    CreateVlan
    """

    id: str
    name: str
    subnet: str
    applianceIp: str
    groupPolicyId: str | None = None
    mask: str | None = None
    cidr: str | None = None
    templateVlanType: str | None = None
    ipv6: IPv6VLANs | None = None


class CreateVlanResponse(BaseVlan):
    """
    CreateVlanResponse
    """

    dhcpHandling: str | None = None
    dhcpLeaseTime: str | None = None
    dhcpBootOptionsEnabled: bool | None = None
    dhcpOptions: list | None = None
    interfaceId: str | None = None
    fixedIpAssignments: FixedIpAssignmentsMeraki | None = None


vlan_value_type_dict = {
    "string": str,
    "integer": int,
    "VlanDhcp": VlanDhcp,
    "FixedIpAssignments": FixedIpAssignmentsMeraki,
    "IPv6VLANs": IPv6VLANs,
    "ReservedIpRanges": list[ReservedIpRange],
}


class ModifyVlan(VlanDhcp):
    """
    VLANModify
    """

    id: str | None = None
    name: str | None = None
    applianceIp: str | None = None
    subnet: str | None = None
    groupPolicyId: str | None = None
    mask: str | None = None
    cidr: str | None = None
    templateVlanType: str | None = None
    vpnNatSubnet: str | None = None
    dnsNameservers: str | None = None
    ipv6: IPv6VLANs | None = None
    reservedIpRanges: list[ReservedIpRange] | None = None
    fixedIpAssignments: FixedIpAssignmentsMeraki | None = None


class CharacteristicBase(BaseModel):
    """
    CharacteristicBase
    """

    uuid: str


def build_model_char(
    model_name: str,
    chars: list[SpecificationCharacteristic] | None,
    value_type_dict: dict | None,
    base_model: type[BaseModel] | type[CharacteristicBase] = CharacteristicBase,
):
    """
    Function that builds a model dynamically from a given specCharacteristic list
    """
    if chars is None:
        chars = []
    if value_type_dict is None:
        value_type_dict = {}
    field_definitions: Any = {}
    for char in chars:
        value_type_char = getattr(char, "valueType", "")
        not_optional = char.minCardinality
        value_type_value = value_type_dict.get(value_type_char, str)
        value_type = value_type_value if not_optional else value_type_value | None
        field = Field(default=None, alias=char.name, value_type=value_type_char)
        field_definitions[char.name] = (value_type, field)

    return create_model(model_name, __base__=base_model, **field_definitions)


class StaticRouteBase(BaseModel):
    """
    Meraki Static Route Model
    Meraki Static Route Base
    """

    name: str
    subnet: str
    gatewayIp: str
    gatewayVlanId: int | None


class StaticRouteCreate(StaticRouteBase):
    """
    Meraki Static Route Create
    """


class StaticRouteGet(StaticRouteBase):
    """
    Extension of Static Routes
    Meraki Static Route Get
    """

    id: str
    networkId: str
    enabled: bool
    fixedIpAssignments: dict[str, MacMapping]
    reservedIpRanges: list[ReservedIpRange]


class StaticRouteUpdate(BaseModel):
    """
    Meraki Static Route Update
    """

    name: str | None
    subnet: str | None
    gatewayIp: str | None
    gatewayVlanId: int | None
    enabled: bool | None
    reservedIpRanges: list[ReservedIpRange] | None
    fixedIpAssignments: FixedIpAssignmentsMeraki | None = None


class StaticRouteCharacteristics(StaticRouteBase):
    """
    Extension of Static Routes
    """

    enabled: bool | None = None
    fixedIpAssignments: FixedIpAssignmentsHarlock | None = None
    reservedIpRanges: list[dict[str, str]] | None = None


class RadiusServerWithoutSecret(BaseModel):
    """
    RadiusServerWithoutSecret
    """

    host: str
    port: int


class RadiusServer(RadiusServerWithoutSecret):
    """
    RadiusServer
    """

    secret: str


class BaseApplianceSSID(BaseModel):
    """
    BaseApplianceSSID
    """

    number: int | None = None
    name: str | None = None
    enabled: bool | None = None
    defaultVlanId: int | None = None
    authMode: str | None = None
    encryptionMode: str | None = None
    wpaEncryptionMode: str | None = None
    visible: bool | None = None
    psk: str | None = None


class ApplianceSSIDGetResponses(BaseApplianceSSID):
    """
    ApplianceSSIDGetResponses
    """

    radiusServers: list[RadiusServerWithoutSecret] | None = None


class DhcpEnforcedDeauthentication(BaseModel):
    """
    DhcpEnforcedDeauthentication
    """

    enabled: bool


class ApplianceSSIDUpdateInput(BaseApplianceSSID):
    """
    ApplianceSSIDUpdateInput
    """

    radiusServers: list[RadiusServer] | None = None
    dhcpEnforcedDeauthentication: DhcpEnforcedDeauthentication | None = None


class ApplianceSSIDCharacteristics(ApplianceSSIDGetResponses):
    """
    ApplianceSSIDCharacteristics
    """

    uuid: str


class ClientTrackingMethod(str, Enum):
    """
    Allowed Client Tracking Modes
    """

    MAC_ADDRESS = "MAC address"
    IP_ADDRESS = "IP address"
    UNIQUE_CLIENT_IDENTIFIER = "Unique client identifier"


class DeploymentModes(str, Enum):
    """
    Allowed Deployment Modes
    """

    ROUTED = "routed"
    PASSTHROUGH = "passthrough"


class DynamicDns(BaseModel):
    """
    Dynamic DNS settings for a network
    """

    enabled: bool | None = None
    prefix: str | None = None
    url: str | None = None


class ApplianceSettingsBase(BaseModel):
    """
    Model to handle every parameter for Appliance Network Settings
    """

    deploymentMode: DeploymentModes | None = None
    clientTrackingMethod: ClientTrackingMethod | None = None
    dynamicDns: DynamicDns | None = None


class ApplianceSettingsCharacteristics(ApplianceSettingsBase):
    """
    ApplianceSettingsCharacteristics
    """

    uuid: str


class SpeedLimit(BaseModel):
    """
    SpeedLimit
    """

    limitUp: int | str | None = None
    limitDown: int | str | None = None

    @validator("*")
    def validate_input(cls, v):  # pylint: disable=no-self-argument, invalid-name
        """
        Allows an unlimited limit to be converted to and from str and None
        """
        if v is None:
            return "unlimited"
        if v == "unlimited":
            return None
        return v


class BandwidthLimits(BaseModel):
    """
    BandwidthLimits
    """

    wan1: SpeedLimit
    wan2: SpeedLimit | None = None
    cellular: SpeedLimit


class UplinkConfig(BaseModel):
    """
    UplinkConfig
    """

    bandwidthLimits: BandwidthLimits


class FailoverAndFailback(BaseModel):
    """
    FailoverAndFailback
    """

    immediate: EnabledStatus


class UplinkSelectionUpdate(BaseModel):
    """
    UplinkSelectionUpdate
    """

    default_uplink: str | None = Field(alias="defaultUplink", default=None)
    failover_and_failback: FailoverAndFailback | None = Field(
        alias="failoverAndFailback", default=None
    )
    load_balancing_enabled: bool | None = Field(
        alias="loadBalancingEnabled", default=None
    )
    active_active_auto_vpn_enabled: bool | None = Field(
        alias="activeActiveAutoVpnEnabled", default=None
    )


class UplinkSelection(UplinkSelectionUpdate):
    """
    UplinkSelectionUpdate
    """

    wanTrafficUplinkPreferences: list = Field(default=[])
    vpnTrafficUplinkPreferences: list = Field(default=[])


class Destination(BaseModel):
    """
    Uplink Stats Destination
    """

    ip: str
    description: str | None = None
    default: bool


class ApplianceConnectivityMonitoringDestinations(BaseModel):
    """
    ApplianceConnectivityMonitoringDestinations
    """

    destinations: list[Destination]


class ApplianceUplinkStatisticsCharacteristics(
    ApplianceConnectivityMonitoringDestinations
):
    """
    ApplianceUplinkStatisticsCharacteristics

    """

    uuid: str


class Hub(BaseModel):
    """
    Hub
    """

    hubId: str
    useDefaultRoute: bool


class Subnet(BaseModel):
    """
    Subnet
    """

    localSubnet: str
    useVpn: bool


class S2SVPNBase(BaseModel):
    """
    S2SVPNBase
    """

    hubs: list[Hub] | None = None
    subnets: list[Subnet] | None = None


class ResponseS2SVPN(S2SVPNBase):
    """
    ResponseS2SVPN
    """

    mode: str


class S2SVPNUpdateInput(S2SVPNBase):
    """
    S2SVPNUpdateInput
    """

    mode: str | None = None


class S2SVPNCharacteristics(ResponseS2SVPN):
    """
    S2SVPNCharacteristics
    """

    uuid: str


class AllowedUrl(BaseModel):
    """
    Base model representing the allowed URL format when configuring
    supported malware settings for an MX network
    """

    url: str
    comment: str


class MalwareProtectionMode(str, Enum):
    """
    Possible options for enabling malware setting for an MX network
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


class AllowedFile(BaseModel):
    """
    Base model representing the allowed file type extensions format when configuring
    supported malware settings for an MX network
    """

    sha256: str
    comment: str


class NetworkApplianceMalwareProtection(BaseModel, use_enum_values=True):
    """
    Base model representing the supported malware settings for an MX network
    """

    mode: MalwareProtectionMode = Field(
        description="Set mode to 'enabled' to enable malware prevention,"
        " otherwise 'disabled'",
        default=MalwareProtectionMode.DISABLED,
    )
    allowed_urls: list[AllowedUrl] | None = Field(
        description="The urls that should be permitted by the malware "
        "detection engine. If omitted, the current config will remain"
        " unchanged. This is available only if your network supports AMP"
        " allow listing",
        alias="allowedUrls",
        default=None,
    )
    allowed_files: list[AllowedFile] | None = Field(
        description="The sha256 digests of files that should be permitted "
        "by the malware detection engine. If omitted, the current config "
        "will remain unchanged. This is available only if your network "
        "supports AMP allow listing",
        alias="allowedFiles",
        default=None,
    )


class NetworkApplianceMalwareProtectionSettingsCharacteristics(
    NetworkApplianceMalwareProtection
):
    """
    NetworkApplianceSecurityMalwareProtection Service characteristics
    """

    uuid: str


class NetworkSwitchStpBridgePriorities(BaseModel):
    """
    Base model representing the network switch stp bridge priorities
    """

    switches: list[str] | None = Field(
        default=None, description="List of switch serial numbers"
    )
    stacks: list[str] | None = Field(default=None, description="List of stack IDs")
    switchProfiles: list[str] | None = Field(
        default=None, description="List of switch template IDs"
    )
    stpPriority: int = Field(
        ..., description="STP priority for switch, stacks, or switch templates"
    )


class NetworkSwitchStp(BaseModel):
    """
    Base model representing the network switch stp
    """

    rstpEnabled: bool = Field(
        ..., description="The spanning tree protocol status in network"
    )
    stpBridgePriority: list[NetworkSwitchStpBridgePriorities] | None = Field(
        default=[],
        description="STP bridge priority for switches/stacks or switch templates. \
            An empty array will clear the STP bridge priority settings.",
    )


class UpdateNetworkSwitchStpBridgePriorities(NetworkSwitchStpBridgePriorities):
    """
    Base model representing the update network switch stp bridge priorities
    """

    stpPriority: int | None = None


class UpdateNetworkSwitchStp(BaseModel):
    """
    Base model representing the update network switch stp
    """

    rstpEnabled: bool | None = None
    stpBridgePriority: UpdateNetworkSwitchStpBridgePriorities | None = None


class NetworkSwitchSettingsPowerExceptionPowerType(str, Enum):
    """
    Enum for Power Type
    """

    COMBINED = "combined"
    REDUNDANT = "redundant"
    USENETWORKSETTING = "useNetworkSetting"


class NetworkSwitchSettingsPowerException(BaseModel):
    """
    Power Exception Model
    """

    serial: str = Field(..., description="Serial number of the switch")
    powerType: NetworkSwitchSettingsPowerExceptionPowerType = Field(
        ..., description="Per switch exception (combined, redundant, useNetworkSetting)"
    )


class NetworkSwitchSettings(BaseModel):
    """
    Base model representing the network switch settings
    """

    vlan: int = Field(..., description="Management VLAN")
    useCombinedPower: bool | None = Field(
        default=None,
        description="The use Combined Power as the default behavior of \
            secondary power supplies on supported devices.",
    )
    powerExceptions: list[NetworkSwitchSettingsPowerException] | None = Field(
        default=None,
        description="Exceptions on a per switch basis to 'useCombinedPower'",
    )
    macBlocklist: EnabledStatus = Field(
        ..., description="Enable MAC blocklist for switches in the network"
    )
    uplinkClientSampling: EnabledStatus = Field(
        ..., description="Enable client sampling on uplink"
    )


class UpdateNetworkSwitchSettings(NetworkSwitchSettings):
    """
    Base model representing the update network switch settings model
    """

    vlan: int | None = None
    useCombinedPower: bool | None = None
    macBlocklist: EnabledStatus | None = None
    uplinkClientSampling: EnabledStatus | None = None
