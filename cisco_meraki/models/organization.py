"""
Generated using datamodel-codegen
Meraki Organization
"""
from enum import Enum
from typing import Any

from pydantic import BaseModel, Extra, Field


class Api(BaseModel):
    """
    Whether API access is enabled
    """

    enabled: bool


class Licensing(BaseModel):
    """
    Organization licensing model.
    Can be 'co-term', 'per-device', or 'subscription'.
    """

    model: str


class Region(BaseModel):
    """
    Name of region
    """

    name: str


class Cloud(BaseModel):
    """
    Region Info
    """

    region: Region


class Detail(BaseModel):
    """
    KEY/VALUE format model used for the Meraki organization management
    details representation.
    """

    name: str
    value: str


class Management(BaseModel):
    """
    Model containing the information about the Meraki
    organization's management system.
    """

    details: list[Detail]


class BasicOrganizationInfo(BaseModel):
    """
    Model containing the very basic information/details about
    a Meraki Organization. The most important one is the organization's
    name. The model's properties are the only necessary parameters used
    for the creation of a Meraki organization.
    The complete model instead, is the ref: "Organization" class used for GET/UPDATE
    operations that contain additional information, like "id", "url", etc.
    """

    name: str = Field(default=None)
    management: Management | None = Field(
        description="Information about the organization's management system",
        default=None,
    )

    class Config:
        # pylint: disable=too-few-public-methods
        """
        Don't allow extra properties
        """

        extra = Extra.forbid


class CloneOrganization(BaseModel):
    """
    Clone from a active Meraki organization when creating a new one.
    """

    clone: bool = Field(
        default=False,
        description="Either to clone or not when creating a new organization",
    )
    original_org_id: str | None = Field(
        default=None,
        description="ID of the Meraki Organization that will be used for cloning",
    )


class OrganizationUpdate(BasicOrganizationInfo):
    """
    Model representing the Meraki organization properties when
    updating via API, where all updatable properties can be optional.
    """

    name: str | None = Field(default=None)
    api: Api | None = Field(default=None)
    management: Management | None = Field(
        description="Information about the organization's management system",
        default=None,
    )

    class Config:
        # pylint: disable=too-few-public-methods
        """
        Don't allow extra properties
        """

        extra = Extra.forbid


class Organization(BasicOrganizationInfo):
    """
    A Meraki organization.
    """

    id: str
    url: str
    api: Api
    licensing: Licensing
    cloud: Cloud
    samlConsumerUrl: Any | None = None
    samlConsumerUrls: list | None = None


class OrganizationInventoryDevice(BaseModel):
    """
    A single device from the inventory of an organization
    """

    orderNumber: str | None = None
    claimedAt: str
    licenseExpirationDate: str | None = None


class Components(BaseModel):
    """
    Components model for OrganizationDevicesStatuses `components` field
    """

    powerSupplies: list[Any] | None = None


class OrganizationDevicesStatuses(BaseModel):
    """
    OrganizationDevicesStatuses model
    """

    name: str | None = None
    serial: str | None = None
    mac: str | None = None
    publicIp: str | None = None
    networkId: str | None = None
    status: str | None = None
    lastReportedAt: str | None = None
    productType: str | None = None
    components: Components | None = None
    model: str | None = None
    tags: list[str] | None = None
    usingCellularFailover: bool | None = None
    wan1Ip: str | None = None
    wan1Gateway: str | None = None
    wan1IpType: str | None = None
    wan1PrimaryDns: str | None = None
    wan1SecondaryDns: str | None = None
    wan2Ip: str | None = None
    configurationUpdatedAt: str | None = None


class HighAvailability(BaseModel):
    """
    High Availability model (seen on allocated Security Appliance and Cellular Gateway)
    """

    enabled: bool | None = None
    role: str | None = None


class SignalStat(BaseModel):
    """
    Signal Stat Resource pydantic model
    """

    rsrp: str | None = None
    rsrq: str | None = None


class Uplink(BaseModel):
    """
    Uplink model
    """

    interface: str | None = None
    status: str | None = None
    ip: str | None = None
    gateway: str | None = None
    publicIp: str | None = None
    primaryDns: str | None = None
    secondaryDns: str | None = None
    ipAssignedBy: str | None = None
    provider: str | None = None
    signalStat: SignalStat | None = None
    model: str | None = None
    connectionType: str | None = None
    apn: str | None = None
    dns1: str | None = None
    dns2: str | None = None
    signalType: str | None = None
    iccid: str | None = None


class OrganizationUplinksStatuses(BaseModel):
    """
    Organization Uplinks Statuses model
    """

    networkId: str | None = None
    serial: str | None = None
    model: str | None = None
    highAvailability: HighAvailability | None = None
    lastReportedAt: str | None = None
    uplinks: list[Uplink] | None = None


class LicenseMode(str, Enum):
    """
    Meraki license mode enumeration
    """

    RENEW = "renew"
    ADD_DEVICES = "addDevices"


class LicenseModel(BaseModel):
    """
    Model for representing a Meraki license.

    Attributes:
    - key (str): The key of the license.
    - mode (LicenseMode): The mode of the license, either 'renew' or 'addDevices'.
    """

    key: str = Field(description="The key of the license")
    mode: LicenseMode = Field(
        default=LicenseMode.ADD_DEVICES,
        description="co-term licensing only: either 'renew' or 'addDevices'. "
        "'addDevices' will increase the license limit, while 'renew' will extend "
        "the amount of time until expiration. Defaults to 'addDevices'. "
        "All licenses must be claimed with the same mode, and at most one renewal "
        "can be claimed at a time. Does not apply to organizations using per-device "
        "licensing model.",
    )


class InventoryDeviceSerials(BaseModel):
    """
    Model representing a list of devices serial numbers
    """

    serials: list[str] = Field(
        description="The serials of the devices that should be claimed or removed"
        "from inventory"
    )


class InventoryItem(InventoryDeviceSerials):
    """
    Model for representing the payload that can be sent to claim
    a device/license/order into organization inventory.

    Attributes:
    - orders (list[str]): list of orders.
    - serials (list[str]): list of serials.
    - licenses (list[LicenseModel]): list of LicenseModel instances representing
    licenses.
    """

    order_numbers: list[str] | None = Field(
        description="The numbers of the orders that should be claimed. Add orders.",
        alias="orders",
        default=None,
    )
    licenses: list[LicenseModel] | None = Field(
        description="The licenses that should be claimed.", default=None
    )


class SnortSignature(BaseModel):
    """
    SNORT signature definition
    """

    ruleId: str
    message: str | None = None

    def __lt__(self, other):
        return self.ruleId < other.ruleId


class OrganizationIntrusionRules(BaseModel):
    """
    Contains a list of specific SNORT signatures allowed
    """

    allowedRules: list[SnortSignature]
