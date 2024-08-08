"""
Wrapper of VeloEnterpriseV1 and VeloEnterpriseV2
"""

from pydantic import BaseModel

from common.southbound.velocloud.v1.models.enterprise import VeloEnterpriseV1
from common.southbound.velocloud.v2.models.enterprise import VeloEnterpriseV2


class VeloEnterprise(BaseModel):
    """
    Wrapper of VeloEnterpriseV1 and VeloEnterpriseV2
    """

    enterprise: VeloEnterpriseV1 | VeloEnterpriseV2
