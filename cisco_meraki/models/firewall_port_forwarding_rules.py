"""
Meraki Appliance Firewall Port Forwarding Rules
"""


from pydantic import BaseModel


class PortForwardRule(BaseModel):
    """
    PortForwardRule
    """

    lanIp: str
    localPort: str
    name: str
    protocol: str
    publicPort: str
    uplink: str
    allowedIps: list[str]


class PortForwardingRules(BaseModel):
    """
    PortForwardingRules
    """

    rules: list[PortForwardRule]


class PortForwardingCharacteristics(PortForwardingRules):
    """
    PortForwardingCharacteristics
    """

    uuid: str
