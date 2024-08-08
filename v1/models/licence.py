"""
Velocloud V1 License models
"""

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Detail(BaseModel):
    """
    License Detail model
    """

    regions: Optional[List[str]] = None
    addOns: Optional[List] = None


class Licence(BaseModel):
    """
    Velocloud License model
    """

    id: Optional[int] = None
    created: Optional[str] = None
    licenseId: Optional[int] = None
    logicalId: Optional[str] = None
    sku: Optional[str] = None
    name: Optional[str] = None
    alias: Optional[str] = None
    detail: Optional[Detail] = None
    quota: Optional[Any] = None
    termMonths: Optional[int] = None
    start: Optional[str] = None
    end: Optional[str] = None
    edition: Optional[str] = None
    bandwidthTier: Optional[str] = None
    active: Optional[int] = None
    modified: Optional[str] = None


class EnterpriseProxyLicense(Licence):
    """
    Velocloud Enterprise Proxy License model
    """

    enterpriseCount: Optional[int] = None
    edgeCount: Optional[int] = 0
    activatedEdgeCount: Optional[int] = 0
