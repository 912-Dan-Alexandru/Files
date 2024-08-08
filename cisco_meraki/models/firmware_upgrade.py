"""
Firmware Upgrade Models
"""
from typing import Optional, List

from pydantic import BaseModel


class UpgradeWindow(BaseModel):
    """
    "dayOfWeek": "Mon",
    "hourOfDay": "4:00"
    """

    dayOfWeek: str
    hourOfDay: str


class Version(BaseModel):
    """
    Common Firmware information
    """

    id: Optional[str] = None
    firmware: Optional[str] = None
    shortName: Optional[str] = None
    releaseType: Optional[str] = None
    releaseDate: Optional[str] = None


class NextUpgrade(BaseModel):
    """
    Next Upgrade
    """

    time: Optional[str] = None
    toVersion: Optional[Version] = None


class LastUpgrade(NextUpgrade):
    """
    Last Upgrade
    """

    fromVersion: Optional[Version] = None


class BaseProduct(BaseModel):
    """
    Each Product Type has the same Firmware details section
    """

    currentVersion: Version
    lastUpgrade: LastUpgrade
    nextUpgrade: NextUpgrade
    availableVersions: List[Version]
    participateInNextBetaRelease: bool


class GETProducts(BaseModel):
    """
    Each Product available for a Network
    When getting the organisation networks, the `productTypes` defines what appears
    """

    wireless: Optional[BaseProduct] = None
    appliance: Optional[BaseProduct] = None
    switch: Optional[BaseProduct] = None
    camera: Optional[BaseProduct] = None
    cellularGateway: Optional[BaseProduct] = None
    sensor: Optional[BaseProduct] = None
    cloudGateway: Optional[BaseProduct] = None


class PUTNextUpgrade(BaseModel):
    """
    PUTNextUpgrade
    """

    nextUpgrade: Optional[NextUpgrade] = None
    participateInNextBetaRelease: bool = False


class PUTProducts(BaseModel):
    """
    PUTproducts
    """

    wireless: Optional[PUTNextUpgrade] = None
    appliance: Optional[PUTNextUpgrade] = None
    switch: Optional[PUTNextUpgrade] = None
    camera: Optional[PUTNextUpgrade] = None
    cellularGateway: Optional[PUTNextUpgrade] = None
    sensor: Optional[PUTNextUpgrade] = None
    cloudGateway: Optional[PUTNextUpgrade] = None


class FirmwareUpgradeGET(BaseModel):
    """
    Top Level Model For Firmware Upgrades
    """

    upgradeWindow: UpgradeWindow
    timezone: str
    products: GETProducts


class FirmwareUpgradePUT(BaseModel):
    """
    FirmwareUpgradePUT
    """

    upgradeWindow: UpgradeWindow
    timezone: str
    products: PUTProducts


class FirmwareUpdateCharacteristics(FirmwareUpgradeGET):
    """
    FirmwareUpdateCharacteristics
    """

    uuid: str
