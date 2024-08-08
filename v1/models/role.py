"""
Pydantic Models
Velocloud V1
/role
"""

from pydantic import BaseModel


class EnterpriseRoleCommon(BaseModel):
    """
    Enterprise role
    """

    isDelegated: bool = False
