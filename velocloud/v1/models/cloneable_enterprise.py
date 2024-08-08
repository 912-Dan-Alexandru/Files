"""
Pydantic Model
Velocloud V1 Cloneable Enterprise
"""

from __future__ import annotations
from typing import List

from pydantic import BaseModel


class SDWAN(BaseModel):
    """
    Velocloud Cloneable Enterprise Service License SDWAN field Model
    """

    enabled: bool


class CWS(BaseModel):
    """
    Velocloud Cloneable Enterprise Service License CWS field Model
    """

    enabled: bool
    licenseEdition: str


class ZTNAD(BaseModel):
    """
    Velocloud Cloneable Enterprise Service License ZTNAD field Model
    """

    enabled: bool
    maxPops: int | None


class ENI(BaseModel):
    """
    Velocloud Cloneable Enterprise Service License ENI field Model
    """

    enabled: bool


class ServiceLicenses(BaseModel):
    """
    Velocloud Cloneable Enterprise Service License field Model
    """

    SDWAN: SDWAN
    CWS: CWS
    ZTNAD: ZTNAD
    ENI: ENI


class CloneableEnterprise(BaseModel):
    """
    Velocloud Cloneable Enterprise Model
    """

    id: int
    name: str
    gatewayPoolId: int
    endpointPkiMode: str
    configurationId: int
    enableEnterpriseDelegationToOperator: bool
    enableEnterpriseUserManagementDelegationToOperator: bool
    enableEnterpriseDelegationToProxy: bool
    delegateEdgeImageManagementToEnterprise: bool
    assignedOperatorProfileConfigurationIds: List
    enableExportRestriction: bool
    edgeLicenseIds: List[int]
    serviceLicenses: ServiceLicenses
