"""
Velocloud V1
/role API Calls
"""

from common.parsing import evaluate_model

from . import models
from .velocloud import SBVelocloudV1


def is_delegated_to_enterprise_proxy(
    client: SBVelocloudV1, enterprise_id: int
) -> models.EnterpriseRoleCommon:
    """
    API: /role/isEnterpriseDelegatedToEnterpriseProxy
            /role/isEnterpriseDelegatedToOperator
            /role/isEnterpriseUserManagementDelegatedToOperator
    """
    data = client.post_api(
        endpoint="/role/isEnterpriseDelegatedToEnterpriseProxy",
        body={"enterpriseId": enterprise_id},
    )
    return evaluate_model(models.EnterpriseRoleCommon, data)


def is_delegated_to_operator(
    client: SBVelocloudV1, enterprise_id: int
) -> models.EnterpriseRoleCommon:
    """
    API: /role/isEnterpriseDelegatedToEnterpriseProxy
            /role/isEnterpriseDelegatedToOperator
            /role/isEnterpriseUserManagementDelegatedToOperator
    """
    data = client.post_api(
        endpoint="/role/isEnterpriseDelegatedToOperator",
        body={"enterpriseId": enterprise_id},
    )
    return evaluate_model(models.EnterpriseRoleCommon, data)


def is_user_management_delegated_to_operator(
    client: SBVelocloudV1, enterprise_id: int
) -> models.EnterpriseRoleCommon:
    """
    API: /role/isEnterpriseUserManagementDelegatedToOperator
    """
    data = client.post_api(
        endpoint="/role/isEnterpriseUserManagementDelegatedToOperator",
        body={"enterpriseId": enterprise_id},
    )
    return evaluate_model(models.EnterpriseRoleCommon, data)
