"""
Common Velocloud V1 Models
"""

from enum import Enum

from pydantic import BaseModel


class ResponseMetadata(BaseModel):
    """
    Response Metadata as seen in Alerts API
    """

    limit: int
    more: bool


class VeloSiteAddress(BaseModel):
    """
    Velocloud Site address shared model
    """

    contactName: str | None = None
    contactPhone: str | None = None
    contactMobile: str | None = None
    contactEmail: str | None = None
    streetAddress: str | None = None
    streetAddress2: str | None = None
    city: str | None = None
    state: str | None = None
    postalCode: str | None = None
    country: str | None = None
    lat: int | None = None
    lon: int | None = None
    timezone: str | None = None
    locale: str | None = None


class VeloSite(VeloSiteAddress):
    """
    Velocloud API V1 Site
    """

    id: int | None = None
    created: str | None = None
    name: str | None = None
    logicalId: str | None = None
    shippingSameAsLocation: int | None = None
    shippingContactName: str | None = None
    shippingAddress: str | None = None
    shippingAddress2: str | None = None
    shippingCity: str | None = None
    shippingState: str | None = None
    shippingCountry: str | None = None
    shippingPostalCode: str | None = None
    modified: str | None = None


class VeloLink(BaseModel):
    """
    Link?
    """

    id: int | None = None
    created: str | None = None
    edgeId: int | None = None
    logicalId: str | None = None
    internalId: str | None = None
    interface: str | None = None
    macAddress: str | None = None
    ipAddress: str | None = None
    ipV6Address: str | None = None
    netmask: str | None = None
    networkSide: str | None = None
    networkType: str | None = None
    displayName: str | None = None
    isp: str | None = None
    org: str | None = None
    lat: int | None = None
    lon: int | None = None
    lastActive: str | None = None
    state: str | None = None
    backupState: str | None = None
    linkMode: str | None = None
    vpnState: str | None = None
    lastEvent: str | None = None
    lastEventState: str | None = None
    alertsEnabled: int | None = None
    operatorAlertsEnabled: int | None = None
    serviceState: str | None = None
    modified: str | None = None
    serviceGroups: list[str] | None = None


class VeloBinary(Enum):
    """
    Velocloud bool values model
    """

    # ruff: noqa: E741
    Z = 0
    O = 1
