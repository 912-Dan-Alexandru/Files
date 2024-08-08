"""
Meraki Firewall Rules
"""

from enum import Enum

from pydantic import BaseModel, Field


class FirewallRule(BaseModel):
    """
    Model to handle a single Layer 3 and Cellular Firewall Rule
    """

    comment: str
    policy: str
    protocol: str
    destPort: str
    destCidr: str
    srcPort: str
    srcCidr: str
    syslogEnabled: bool


class NetworkFirewallRules(BaseModel):
    """
    Model to handle a collection Layer 3 and Cellular Firewall Rules
    """

    rules: list[FirewallRule] = Field(default_factory=list)
    syslogDefaultRule: bool | None = None


class Layer7FirewallRuleType(str, Enum):
    """
    Model to handle the allowed types of a Layer 7 Firewall Rule
    """

    APPLICATION = "application"
    APPLICATION_CATAGORY = "applicationCatagory"
    HOST = "host"
    PORT = "port"
    IP_RANGE = "ipRange"


class Layer7FirewallRule(BaseModel):
    """
    Model to handle a single layer 7 firewall rule
    """

    policy: str
    type: str
    value: str | list | dict


class Layer7FirewallRules(BaseModel):
    """
    Model to handle a collection Layer 7 Firewall Rules
    """

    rules: list[Layer7FirewallRule] = Field(default_factory=list)
