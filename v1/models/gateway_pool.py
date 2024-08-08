"""
Velocloud V1
/enterprise
"""
from typing import Optional
from pydantic import BaseModel


class EnterpriseProxyGatewayPool(BaseModel):
    """
    Velo Enterprise Proxy Gateway Pool model without Enterprise and Gateway options
    """

    id: int
    networkId: Optional[int] = None
    enterpriseProxyId: Optional[int] = None
    created: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    logicalId: Optional[str] = None
    isDefault: Optional[bool] = None
    ipV4Enabled: Optional[bool] = None
    ipV6Enabled: Optional[bool] = None
    handOffType: Optional[str] = None
    modified: Optional[str] = None
