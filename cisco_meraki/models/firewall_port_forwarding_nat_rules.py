"""
Meraki Appliance Firewall Port Forwarding NAT Rules
"""
from enum import Enum

from pydantic import BaseModel, Field


class UplinkType(str, Enum):
    """
    Physical WAN interface
    """

    INTERNET_1 = "internet1"
    INTERNET_2 = "internet2"


class ProtocolType(str, Enum):
    """
    Network protocol type
    """

    TCP = "tcp"
    UDP = "udp"
    ICMP_PING = "icmp-ping"
    ANY = "any"


class AllowedInboundItem(BaseModel, use_enum_values=True):
    """
    Allowed inbound connections for 1:1 NAT mapping rules <OneToOneNatRules class>
    """

    protocol: ProtocolType = Field(
        ..., description="Either of the following: 'tcp', 'udp', 'icmp-ping' or 'any'"
    )
    destination_ports: list[str] = Field(
        ...,
        alias="destinationPorts",
        description="An array of ports or port ranges that will be forwarded to"
        " the host on the LAN",
    )
    allowed_ips: list[str] = Field(
        ...,
        alias="allowedIps",
        description="An array of ranges of WAN IP addresses that are allowed to"
        "make inbound connections on the specified ports or port ranges, or 'any'",
    )


class OneToOneNatRule(BaseModel, use_enum_values=True):
    """
    Rule model for configuring the 1:1 NAT forwarding rules
    """

    name: str | None = Field(
        description="A descriptive name for the rule", default=None
    )
    lan_ip: str = Field(
        ...,
        alias="lanIp",
        description="The IP address of the server "
        "or device that hosts the internal resource that you wish"
        " to make available on the WAN",
    )
    public_ip: str | None = Field(
        alias="publicIp",
        description="The IP address that"
        " will be used to access the internal "
        "resource from the WAN",
        default=None,
    )
    uplink: UplinkType | None = Field(
        description="The physical WAN interface on which the traffic will arrive"
    )
    allowed_inbound: list[AllowedInboundItem] | None = Field(
        description="The ports "
        "this mapping will provide access on, and the remote IPs that will be "
        "allowed access to the resource",
        alias="allowedInbound",
        default=None,
    )


class OneToOneNatRules(BaseModel):
    """
    1:1 NAT mapping rules for an MX network
    """

    rules: list[OneToOneNatRule] = Field(description="An array of 1:1 NAT rules")


class PortRule(BaseModel):
    """
    Single port forwarding rule for 1:Many NAT mapping rules <OneToManyNatRule class>
    """

    name: str = Field(..., description="A description of the rule")
    protocol: ProtocolType = Field(description="Protocol type")
    public_port: str = Field(
        ...,
        alias="publicPort",
        description="Destination port of the traffic that is arriving on the WAN",
    )
    local_ip: str = Field(
        ...,
        alias="localIp",
        description="Local IP address to which traffic will be forwarded",
    )
    local_port: str = Field(
        ...,
        alias="localPort",
        description="Destination port of the forwarded traffic that will be"
        " sent from the MX to the specified host on the LAN. If you simply"
        " wish to forward the traffic without translating the port, this"
        " should be the same as the Public port",
    )
    allowed_ips: list[str] = Field(
        ...,
        alias="allowedIps",
        description="Remote IP addresses or ranges that are permitted to"
        " access the internal resource via this port forwarding rule, or 'any'",
    )


class OneToManyNatRule(BaseModel):
    """
    Rule model for configuring the 1:Many NAT forwarding rules
    """

    public_ip: str = Field(
        ...,
        alias="publicIp",
        description="The IP address that will be used to access"
        " the internal resource from the WAN",
    )
    uplink: UplinkType = Field(
        description="The physical WAN "
        "interface on which the traffic will arrive "
        "('internet1' or, if available, 'internet2')"
    )
    port_rules: list[PortRule] | None = Field(
        alias="portRules",
        description="An array of associated forwarding rules",
        default=None,
    )


class OneToManyNatRules(BaseModel):
    """
    1:Many NAT mapping rules for an MX network
    """

    rules: list[OneToManyNatRule] = Field(description="An array of 1:Many NAT rules")


class PortForwardingOneToManyNatRulesCharacteristics(OneToManyNatRules):
    """
    OneToManyNatRules model characteristics
    """

    uuid: str


class PortForwardingOneToOneNatRulesCharacteristics(OneToOneNatRules):
    """
    OneToOneNatRules model characteristics
    """

    uuid: str
