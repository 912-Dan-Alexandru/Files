"""
Appliance pydantic model
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from common.southbound.cisco_meraki.models.network import BandwidthLimits


class HighAvailability(BaseModel):
    """
    High Availability model (seen on allocated Security Appliance and Cellular Gateway)
    """

    enabled: bool | None = None
    role: str | None = None


class ApplianceUplink(BaseModel):
    """
    Uplink of Organization Appliance Uplinks Statuses model
    """

    interface: str | None = None
    status: str | None = None
    ip: str | None = None
    gateway: str | None = None
    publicIp: str | None = None
    primaryDns: str | None = None
    secondaryDns: str | None = None
    ipAssignedBy: str | None = None


class OrganizationApplianceUplinksStatuses(BaseModel):
    """
    Organization Appliance Uplinks Statuses model
    """

    networkId: str | None = None
    serial: str | None = None
    model: str | None = None
    highAvailability: HighAvailability | None = None
    lastReportedAt: str | None = None
    uplinks: list[ApplianceUplink] | None = None


class UsageSummary(BaseModel):
    """
    UsageSummary pydantic model
    """

    receivedInKilobytes: str | None = None
    sentInKilobytes: str | None = None


class LatencySummary(BaseModel):
    """
    LatencySummary
    """

    senderUplink: str | None = None
    receiverUplink: str | None = None
    avgLatencyMs: float | None = None
    minLatencyMs: int | None = None
    maxLatencyMs: int | None = None


class LossPercentageSummary(BaseModel):
    """
    LossPercentageSummary
    """

    senderUplink: str | None = None
    receiverUplink: str | None = None
    avgLossPercentage: float | None = None
    minLossPercentage: int | None = None
    maxLossPercentage: int | None = None


class JitterSummary(BaseModel):
    """
    JitterSummary
    """

    senderUplink: str | None = None
    receiverUplink: str | None = None
    avgJitter: float | None = None
    minJitter: int | None = None
    maxJitter: int | None = None


class MosSummary(BaseModel):
    """
    MosSummary
    """

    senderUplink: str | None = None
    receiverUplink: str | None = None
    avgMos: float | None = None
    minMos: float | None = None
    maxMos: float | None = None


class MerakiVpnPeer(BaseModel):
    """
    MerakiVpnPeer
    """

    networkId: str | None = None
    networkName: str | None = None
    usageSummary: UsageSummary | None = None
    latencySummaries: list[LatencySummary] | None = None
    lossPercentageSummaries: list[LossPercentageSummary] | None = None
    jitterSummaries: list[JitterSummary] | None = None
    mosSummaries: list[MosSummary] | None = None


class OrganizationApplianceVpnStats(BaseModel):
    """
    OrganizationApplianceVpnStats
    """

    networkId: str | None = None
    networkName: str | None = None
    merakiVpnPeers: list[MerakiVpnPeer]


class ByUplink(BaseModel):
    """
    ByUplink BaseModel
    """

    serial: str | None = None
    interface: str | None = None
    sent: int | None = None
    received: int | None = None


class OrganizationApplianceUplinksUsageByNetwork(BaseModel):
    """
    OrganizationApplianceUplinksUsageByNetwork
    """

    networkId: str | None = None
    name: str | None = None
    byUplink: list[ByUplink]


class SecurityIntrusionMode(str, Enum):
    """possible ways of security intrusion"""

    DISABLED = "disabled"
    DETECTION = "detection"
    PREVENTION = "prevention"


class SecurityIntrusionRulesets(str, Enum):
    """possible rule sets of security intrusion"""

    CONNECTIVITY = "connectivity"
    BALANCED = "balanced"
    SECURITY = "security"


class SecurityIntrusionProtectedNetworks(BaseModel):
    """
    Security Intrusion Protected Networks
    """

    use_default: bool = Field(default=True, alias="useDefault")
    included_cidr: list[str] | None = Field(default=None, alias="includedCidr")
    excluded_cidr: list[str] | None = Field(default=None, alias="excludedCidr")


class SecurityIntrusionModel(BaseModel):
    """
    Security Intrusion Response
    """

    mode: SecurityIntrusionMode = SecurityIntrusionMode.DISABLED
    ids_rulesets: SecurityIntrusionRulesets | None = Field(
        default=None, alias="idsRulesets"
    )
    protected_networks: SecurityIntrusionProtectedNetworks | None = Field(
        default=None, alias="protectedNetworks"
    )


class TimeSeries(BaseModel):
    """
    Time series output
    """

    ts: str | None
    loss_percent: float | None = Field(alias="lossPercent")
    latency_ms: float | None = Field(alias="latencyMs")


class UplinksLossAndLatency(BaseModel):
    """
    Organization Device output
    """

    serial: str | None
    network_id: str | None = Field(default=None, alias="networkId")
    uplink: str | None
    ip: str | None
    time_series: list[TimeSeries] | None = Field(default=None, alias="timeSeries")


class Immediate(BaseModel):
    """
    Immediate output
    """

    enabled: bool | None


class FailoverAndFailback(BaseModel):
    """
    Failover and Failback output
    """

    immediate: Immediate | None


class PerformanceClass(BaseModel):
    """
    Performance Class output
    """

    builtinPerformanceClassName: str | None
    customPerformanceClassId: str | None
    type_performance: str | None = Field(default=None, alias="type")


class Destination(BaseModel):
    """
    Destination output
    """

    host: int | None
    vlan: int | None
    cidr: str | None
    fqdn: str | None
    network: str | None
    port: str | None


class Source(BaseModel):
    """
    Source output
    """

    host: int | None
    vlan: int | None
    cidr: str | None
    network: str | None
    port: str | None


class Value(BaseModel):
    """
    Value output
    """

    id: str | None
    protocol: str | None
    destination: Destination
    source: Source


class TrafficFilters(BaseModel):
    """
    Traffic output
    """

    type_filters: str | None = Field(default=None, alias="type")
    value = Value


class VpnTrafficUplinkPreferences(BaseModel):
    """
    Vpn Traffic uplink preferences
    """

    failOverCriterion: str | None
    preferredUplink: str | None
    performanceClass: PerformanceClass | None = None
    trafficFilters: list[TrafficFilters] | list = []


class WanTrafficUplinkPreferences(BaseModel):
    """
    Wan Traffic Uplink Preferences
    """

    preferredUplink: str | None
    trafficFilters: str | None


class TrafficShapingUplinkSelection(BaseModel):
    """
    Traffic Shaping Uplink Selection output
    """

    defaultUplink: str | None
    activeActiveAutoVpnEnabled: bool | None
    loadBalancingEnabled: bool | None
    failoverAndFailback: FailoverAndFailback
    vpnTrafficUplinkPreferences: list[VpnTrafficUplinkPreferences] | list = []
    wanTrafficUplinkPreferences: list[WanTrafficUplinkPreferences] | list = []


class TrafficShapingUplinkBandwidth(BaseModel):
    """
    Traffic Shaping Uplink Bandwidth output
    REF: https://developer.cisco.com/meraki/api-v1/
    get-network-appliance-traffic-shaping-uplink-bandwidth/
    """

    bandwidthLimits: BandwidthLimits


class TrafficInKbps(BaseModel):
    """
    Traffic In Kbps per port
    """

    total: float
    sent: float
    recv: float


class OrganizationSwitchPorts(BaseModel):
    """
    Organization Switch Ports Data
    """

    portId: str
    enabled: bool
    status: str
    isUplink: bool
    errors: list
    warnings: list
    speed: str
    duplex: str
    usageInKb: Any
    cdp: Any | None = None
    lldp: Any | None = None
    clientCount: int
    powerUsageInWh: float
    trafficInKbps: TrafficInKbps
    securePort: Any
    spanningTree: Any
    poe: Any


class OrganizationSwitchNetwork(BaseModel):
    """
    Organization Switch Network Data
    """

    id: str
    name: str


class OrganizationSwitchPortsBySwitch(BaseModel):
    """
    Organization Switch Ports Statuses By Switch
    REF: https://developer.cisco.com/meraki/api-v1/
    get-organization-switch-ports-statuses-by-switch/
    """

    name: str
    serial: str
    mac: str
    network: OrganizationSwitchNetwork
    model: str
    ports: list[OrganizationSwitchPorts]
