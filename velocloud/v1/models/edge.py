"""
Velocloud API V1 Enterprise
"""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from .common import VeloSite, VeloLink


class EdgeCertificate(BaseModel):
    """
    Certificate Information
    """

    id: Optional[int] = None
    created: Optional[str] = None
    csrId: Optional[int] = None
    edgeId: Optional[int] = None
    enterpriseId: Optional[int] = None
    certificate: Optional[str] = None
    serialNumber: Optional[str] = None
    subjectKeyId: Optional[str] = None
    fingerPrint: Optional[str] = None
    fingerPrint256: Optional[str] = None
    validFrom: Optional[str] = None
    validTo: Optional[str] = None


class EdgeConfigModule(BaseModel):
    """
    Enterprise modules have edgeSpecificData key
    Operator might not
    """

    edgeSpecificData: Dict[str, Any]
    isEdgeSpecific: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None


class VeloConfigurationV1(BaseModel):
    """
    Can be either operator or Enterprise
    """

    id: Optional[int] = None
    modules: List[EdgeConfigModule]
    name: Optional[str] = None


class EdgeConfigModuleData(BaseModel):
    """
    When doing /edge/getEdge
    """

    configurationId: Optional[int] = None
    created: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    description: Optional[str] = None
    effective: Optional[str] = None
    id: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None
    modified: Optional[str] = None
    name: Optional[str] = None
    refs: Optional[Dict[str, Any]] = None
    schemaVersion: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None


class EnterpriseConfiguration(BaseModel):
    """
    Enterprise Configurations
    """

    operator: Optional[VeloConfigurationV1] = None
    enterprise: Optional[VeloConfigurationV1] = None
    bastionState: Optional[str] = None
    configurationType: Optional[str] = None
    created: Optional[str] = None
    description: Optional[str] = None
    edgeCount: Optional[int] = 0
    effective: Optional[str] = None
    id: Optional[int] = None
    isStaging: Optional[int] = None
    logicalId: Optional[str] = None
    modified: Optional[str] = None
    modules: Optional[List[EdgeConfigModuleData]] = None
    name: Optional[str] = None
    schemaVersion: Optional[str] = None
    version: Optional[str] = None


class HighAvailability(BaseModel):
    """
    High Availability Information
    """

    type: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


class EdgeLicense(BaseModel):
    """
    Velocloud Licences
    """

    id: Optional[int] = None
    created: Optional[str] = None
    licenseId: Optional[int] = None
    sku: Optional[str] = None
    name: Optional[str] = None
    alias: Optional[str] = None
    detail: Optional[str] = None
    quota: Optional[str] = None
    termMonths: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    edition: Optional[str] = None
    bandwidthTier: Optional[str] = None
    active: Optional[int] = None
    modified: Optional[str] = None


class Edge(BaseModel):
    """
    Velocloud API V1 Enterprise
    """

    activationKey: str
    activationKeyExpires: str
    activationState: str
    activationTime: str
    alertsEnabled: int
    bastionState: str
    buildNumber: str
    created: str
    customInfo: str | None = None
    description: str | None = None
    deviceFamily: str
    deviceId: str | None = None
    dnsName: str | None = None
    edgeState: str
    edgeStateTime: str
    endpointPkiMode: str
    enterpriseId: int
    factorySoftwareVersion: str
    factoryBuildNumber: str
    haLastContact: str
    haPreviousState: str
    haSerialNumber: str | None = None
    haState: str
    id: int
    isLive: int
    lastContact: str
    logicalId: str
    modelNumber: str
    modified: str
    name: str
    operatorAlertsEnabled: int
    selfMacAddress: str
    serialNumber: str | None = None
    serviceState: str
    serviceUpSince: str
    siteId: int
    softwareUpdated: str
    softwareVersion: str
    systemUpSince: str
    certificates: List[EdgeCertificate] | None = None
    configuration: EnterpriseConfiguration | None = None
    ha: HighAvailability | None = None
    licenses: List[EdgeLicense] | None = None
    links: List[VeloLink] | None = None
    recentLinks: List[VeloLink] | None = None
    site: VeloSite | None = None
    isHub: bool | None = None
    isSoftwareVersionSupportedByVco: bool | None = None


class EdgeModule(BaseModel):
    """
    Veloclound Operator and Enterprise modules model
    """

    edgeSpecificData: Optional[dict] = None
    isEdgeSpecific: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None


class VeloEnterpriseOperatorV1(BaseModel):
    """
    Veloclound Operator or Enterprise model
    """

    id: Optional[int] = None
    modules: Optional[List[EdgeModule]] = None
    name: Optional[str] = None


class EdgeConfig(BaseModel):
    """
    Velocloud Enterprise Edges configuration
    """

    operator: Optional[VeloEnterpriseOperatorV1] = None
    enterprise: Optional[VeloEnterpriseOperatorV1] = None


class EnterpriseEdge(Edge):
    """
    Velocloud Enterprise Edges
    """

    configuration: Optional[EdgeConfig] = None
    license: Optional[List[EdgeLicense]] = None
    isSoftwareVersionSupportedByVco: Optional[bool] = None
    isHub: Optional[bool] = None
    enterpriseId: Optional[int] = None


class EdgeProvisionResponse(BaseModel):
    """
    Velo Edge/EdgeProvision response model
    """

    id: int
    activationKey: str
    logicalId: str
