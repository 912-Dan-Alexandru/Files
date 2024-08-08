"""
Velocloud API V1 Edge
"""

from enum import Enum

from pydantic import BaseModel

from .common import VeloBinary, VeloSite, VeloSiteAddress


class ConfigModuleName(Enum):
    """
    Velocloud Operator Configuation Module Name modele
    """

    IMAGE_UPDATE = "imageUpdate"
    CONTROL_PLANE = "controlPlane"
    MANAGEMENT_PLANE = "managementPlane"
    FIREWALL = "firewall"
    QOS = "QOS"
    DEVICE_SETTINGS = "deviceSettings"
    WAN = "WAN"
    META_DATA = "metaData"
    PROPERTIES = "properties"
    ANALYTICS_SETTINGS = "analyticsSettings"
    ATP_METADATA = "atpMetadata"


class ConfigModuleType(Enum):
    """
    Velocloud Operator Configuation Module Type Model
    """

    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class LicenseEdition(Enum):
    """
    License Edition enum
    """

    STANDARD = "STANDARD"
    ADVANCED = "ADVANCED"


class AnalyticsCapability(Enum):
    """
    Analytics Capability enum
    """

    NONE = "NONE"
    APPLICATION_BRANCH = "APPLICATION_BRANCH"


class AnalyticsConfiguration(BaseModel):
    """
    Analytics Configuration Model
    """

    analyticsCapability: AnalyticsCapability
    analyticsEdgeLimit: int
    analyticsSelfHealing: bool


class Module(BaseModel):
    """
    Velocloud Operator Configuation Module
    """

    created: str | None = None
    effective: str | None = None
    modified: str | None = None
    id: int | None = None
    name: ConfigModuleName
    type: ConfigModuleType | None = None
    description: str | None = None
    configurationId: int | None = None
    data: dict = {}
    schemaVersion: str | None = None
    version: str | None = None
    metadata: dict | None = None
    refs: dict | None = None


class BastionState(Enum):
    """
    Velocloud Bastion State
    """

    UNCONFIGURED = "UNCONFIGURED"
    STAGE_REQUESTED = "STAGE_REQUESTED"
    UNSTAGE_REQUESTED = "UNSTAGE_REQUESTED"
    STAGED = "STAGED"
    UNSTAGED = "UNSTAGED"


class VeloConfigurationTypeV1(Enum):
    """
    Configuation Type list
    """

    NETWORK_BASED = "NETWORK_BASED"
    SEGMENT_BASED = "SEGMENT_BASED"


class VeloSpecificOperatorConfigurationV1(BaseModel):
    """
    Velocloud Operator Configuation
    """

    configurationType: VeloConfigurationTypeV1 | None = None
    bastionState: BastionState | None = None
    created: str | None = None
    description: str | None = None
    edgeCount: int | None = 0
    effective: str | None = None
    id: int | None = None
    logicalId: str | None = None
    modified: str | None = None
    modules: list[Module] = []
    name: str | None = None
    schemaVersion: str | None = None
    version: str | None = None
    isStaging: VeloBinary | None = None
    configurationAssociationId: int | None = None
    isTemplate: int | None = None
    configurationId: int | None = None


class VeloDataType(Enum):
    """
    Data Types from Velocloud
    """

    STRING = "STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    JSON = "JSON"
    DATE = "DATE"
    DATETIME = "DATETIME"


class VeloEnterprisePropertyV1(BaseModel):
    """
    Velocloud Enterprise Property model
    """

    id: int
    enterpriseId: int
    created: str
    name: str
    value: str
    isPassword: bool
    dataType: VeloDataType
    description: str | None = None
    modified: str


class User(BaseModel):
    """
    Contact for Customer
    """

    email: str | None = None
    password: str | None = None
    password2: str | None = None
    username: str | None = None


class VeloEnterpriseEdgeRefV1(VeloSite):
    """
    Edge Reference part of Enterprise
    """

    gatewayPoolId: int | None = None
    networkId: int | None = None
    returnData: bool | None = None
    user: User | None = None
    customInfo: str | None = None


class Licenses(BaseModel):
    """
    Licenses model
    """

    ids: list[int]


class BaseServiceLicenceDetails(BaseModel):
    """
    SDWAN and CWS Share enabled option only
    """

    enabled: bool | None = None


class ServiceLicenceZTNAD(BaseServiceLicenceDetails):
    """
    ZTNAD has a maxPops extra option
    """

    maxPops: int | None = None


class ServiceLicenceCWS(BaseServiceLicenceDetails):
    """
    CWS has a licenseEdition extra option
    """

    licenseEdition: LicenseEdition


class VeloEnterpriseServiceLicensesV1(BaseModel):
    """
    Service Licences
    """

    SDWAN: BaseServiceLicenceDetails
    CWS: ServiceLicenceCWS | None = None
    ZTNAD: ServiceLicenceZTNAD | None = None
    PICS: BaseServiceLicenceDetails | None = None
    MCS: BaseServiceLicenceDetails | None = None
    P5G: BaseServiceLicenceDetails | None = None


class VeloEdgeEnterpriseRefV1(BaseModel):
    """
    Velocloud Edge data in Enterprise data model
    """

    activationState: str | None = None
    buildNumber: str | None = None
    modelNumber: str | None = None
    name: str | None = None
    id: int | None = None
    lastContact: str | None = None
    logicalId: str | None = None
    softwareVersion: str | None = None


class VeloEnterpriseConfigurationV1(VeloSpecificOperatorConfigurationV1):
    """
    Velocloud Enterprise Configuration
    """

    edges: list[VeloEdgeEnterpriseRefV1] | None = None


class EnterpriseProxy(BaseModel):
    """
    Velocloud Enterprise Proxy MSP
    """

    id: int
    created: str
    networkId: int
    proxyType: str | None = None
    operateGateways: int | None = None
    logicalId: str
    name: str
    domain: str | int | None = None
    prefix: str | int | None = None
    description: str | int | None = None
    contactName: str | int | None = None
    contactPhone: str | int | None = None
    contactMobile: str | None = None
    contactEmail: str | int | None = None
    streetAddress: str | int | None = None
    streetAddress2: str | int | None = None
    city: str | int | None = None
    state: str | int | None = None
    postalCode: str | int | None = None
    country: str | int | None = None
    lat: float | None = None
    lon: float | None = None
    modified: str | None = None
    gatewayPoolIds: list[int] | None = None
    gatewayPoolId: int | None = None


class VeloEnterpriseV1(VeloSiteAddress):
    """
    Velocloud Enterprise V1
    """

    id: int
    created: str
    networkId: int
    gatewayPoolId: int
    alertsEnabled: int
    operatorAlertsEnabled: int
    endpointPkiMode: str
    name: str
    domain: str | None = None
    prefix: str | None = None
    logicalId: str
    accountNumber: str
    description: str | None = None
    modified: str
    bastionState: str
    edgeCount: int | None = None
    edges: list[VeloEnterpriseEdgeRefV1] | None = None
    serviceLicenses: VeloEnterpriseServiceLicensesV1 | None = None


class CloneEnterprise(EnterpriseProxy):
    """
    Velo enterprise/cloneEnterpriseV1 response model
    """

    proxyType: str | None = None
    alertsEnabled: int | None = None
    operatorAlertsEnabled: int | None = None
    endpointPkiMode: str | None = None
    accountNumber: str | None = None
    timezone: str | None = None
    locale: str | None = None
    bastionState: str | None = None
    gatewayPoolIds: list[int] | None = None


class UpdatableFields(VeloSiteAddress):
    """
    _update object with all the fields updatable
    """

    name: str | None = None
    gatewayPoolId: int | None = None


class UpdateVeloEnterpriseV1(BaseModel):
    """
    Update a Velocloud Enterprise Model
    """

    enterpriseId: int
    _update: UpdatableFields


class CreateEnterprise(VeloEnterpriseV1):
    """
    Create a Velocloud Enterprise Model
    """

    user: User
    enableEnterpriseDelegationToOperator: bool | None = None
    enableEnterpriseDelegationToProxy: bool | None = None
    enableEnterpriseUserManagementDelegationToOperator: bool | None = None
    delegateEdgeImageManagementToEnterprise: bool | None = None
    enableExportRestriction: bool | None = None
    assignedOperatorProfileConfigurationIds: list[int] | None = None
    configurationId: int
    licenses: Licenses | None = None
    serviceLicenses: VeloEnterpriseServiceLicensesV1
    analyticsConfiguration: AnalyticsConfiguration | None = None
    enterpriseProxyId: int | None = None


class DeleteEnterpriseResponse(BaseModel):
    """
    Velo enterprise/deleteEnterprise response model
    """

    rows: int


class InsertEnterpriseProxyEnterprise(DeleteEnterpriseResponse):
    """
    Velo enterpriseProxy/insertEnterpriseProxyEnterprise response model
    """

    id: int


class VeloEnterpriseProxyInsertEnterpriseProxyEnterprise(DeleteEnterpriseResponse):
    """
    Velo enterpriseProxy/insertEnterpriseProxyEnterprise response model
    """

    id: int
