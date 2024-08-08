"""
Velocloud V1 Enterprise Users models
"""

from __future__ import annotations
from typing import Optional

from pydantic import BaseModel
from .common import VeloBinary


class EnterpriseUser(BaseModel):
    """
    Velocloud Enterprise Users model
    """

    id: int
    created: Optional[str] = None
    userType: Optional[str] = None
    username: Optional[str] = None
    domain: Optional[str] = None
    password: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    officePhone: Optional[str] = None
    mobilePhone: Optional[str] = None
    isNative: Optional[VeloBinary] = None
    isActive: VeloBinary
    isLocked: VeloBinary
    disableSecondFactor: Optional[VeloBinary] = None
    email: Optional[str] = None
    lastLogin: Optional[str] = None
    modified: Optional[str] = None
    salt: Optional[str] = None
    passwordModified: Optional[str] = None
    roleId: Optional[int] = None
    roleName: Optional[str] = None
    isSuper: Optional[VeloBinary] = None
