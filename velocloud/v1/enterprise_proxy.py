"""
Velocloud V1
/enterpriseProxy API Calls
"""

from common.parsing import evaluate_model

from . import models
from .velocloud import SBVelocloudV1


def get_proxy_enterprises(client: SBVelocloudV1) -> list[models.VeloEnterpriseV1]:
    """
    API: enterpriseProxy/getEnterpriseProxyEnterprises
    """
    data = client.post_api(
        "/enterpriseProxy/getEnterpriseProxyEnterprises",
        body={"with": ["edges"]},
    )
    return evaluate_model(list[models.VeloEnterpriseV1], data)


def get_enterprise_proxy(client: SBVelocloudV1) -> models.EnterpriseProxy:
    """
    API: /enterpriseProxy/getEnterpriseProxy
    """

    data = client.post_api(endpoint="/enterpriseProxy/getEnterpriseProxy", body={})
    return evaluate_model(models.EnterpriseProxy, data)


def get_cloneable_enterprises(
    client: SBVelocloudV1, enterprise_proxy_id: int
) -> list[models.CloneableEnterprise]:
    """
    API: /enterpriseProxy/getEnterpriseProxyCloneableEnterprises
    """
    data = client.post_api(
        endpoint="/enterpriseProxy/getEnterpriseProxyCloneableEnterprises",
        body={"enterpriseProxyId": enterprise_proxy_id},
    )

    return evaluate_model(list[models.CloneableEnterprise], data)


def get_gateway_pools(
    client: SBVelocloudV1, enterprise_proxy_id: None | int = None
) -> list[models.EnterpriseProxyGatewayPool]:
    """
    API: /enterpriseProxy/getEnterpriseProxyGatewayPools
    """
    data = client.post_api(
        endpoint="/enterpriseProxy/getEnterpriseProxyGatewayPools",
        body={
            "with": ["gateways", "enterprises"],
            "enterpriseProxyId": enterprise_proxy_id,
        },
    )
    return evaluate_model(list[models.EnterpriseProxyGatewayPool], data)


def get_operator_profiles(
    client: SBVelocloudV1, enterprise_proxy_id: int
) -> list[models.VeloEnterpriseConfigurationV1]:
    """
    API: /enterpriseProxy/getEnterpriseProxyOperatorProfiles
    """
    data = client.post_api(
        endpoint="/enterpriseProxy/getEnterpriseProxyOperatorProfiles",
        body={
            "with": ["modules", "edgeCount"],
            "enterpriseProxyId": enterprise_proxy_id,
        },
    )
    return evaluate_model(list[models.VeloEnterpriseConfigurationV1], data)


def insert_enterprise(
    client: SBVelocloudV1, body: dict
) -> models.InsertEnterpriseProxyEnterprise:
    """
    API: /enterpriseProxy/insertEnterpriseProxyEnterprise
    """
    data = client.post_api(
        endpoint="/enterpriseProxy/insertEnterpriseProxyEnterprise",
        body=body,
    )
    return evaluate_model(models.InsertEnterpriseProxyEnterprise, data)
