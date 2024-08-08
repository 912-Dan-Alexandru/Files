"""
Device Swicth Ports Statuses pydantic model
"""
from typing import List, Optional

from pydantic import BaseModel


class UsageInKb(BaseModel):
    """
    UsageInKb pydantic model
    """

    total: Optional[int] = None
    sent: Optional[int] = None
    recv: Optional[int] = None


class Cdp(BaseModel):
    """
    Cdp pydantic model
    """

    systemName: Optional[str] = None
    platform: Optional[str] = None
    devideId: Optional[str] = None
    portId: Optional[str] = None
    nativeVlan: Optional[int] = None
    address: Optional[str] = None
    managementAddress: Optional[str] = None
    version: Optional[str] = None
    vtpManagementDomain: Optional[str] = None
    capabilities: Optional[str] = None


class Lldp(BaseModel):
    """
    _Lldp pydantic model
    """

    systemName: Optional[str] = None
    systemDescription: Optional[str] = None
    portId: Optional[str] = None
    portDescription: Optional[str] = None
    chassisId: Optional[str] = None
    managementVlan: Optional[int] = None
    portVlan: Optional[int] = None
    managementAddress: Optional[str] = None
    systemCapabilities: Optional[str] = None


class TrafficInKbps(BaseModel):
    """
    Traffic In Kbps pydantic model
    """

    total: Optional[int] = None
    sent: Optional[int] = None
    recv: Optional[int] = None


class ConfigOverrides(BaseModel):
    """
    Config Overrides pydantic model
    """

    type: Optional[str] = None
    allowedVlans: Optional[str] = None
    vlan: Optional[int] = None
    voiceVlan: Optional[int] = None


class SecurePort(BaseModel):
    """
    Secure Port pydantic model
    """

    enabled: Optional[bool] = None
    active: Optional[bool] = None
    authenticationStatus: Optional[str] = None
    configOverrides: Optional[ConfigOverrides] = None


class DeviceSwitchPortsStatuses(BaseModel):
    """
    Device Swicth Ports Statuses pydantic model
    """

    portId: Optional[str] = None
    enabled: Optional[bool] = None
    status: Optional[str] = None
    isUpLink: Optional[bool] = None
    errors: Optional[List[str]] = None
    warnings: Optional[List[str]] = None
    speed: Optional[str] = None
    duplex: Optional[str] = None
    usageInKb: Optional[UsageInKb] = None
    cdp: Optional[Cdp] = None
    lldp: Optional[Lldp] = None
    clientCount: Optional[int] = None
    powerUsageInWh: Optional[int] = None
    trafficInKbps: Optional[TrafficInKbps] = None
    securePort: Optional[SecurePort] = None
