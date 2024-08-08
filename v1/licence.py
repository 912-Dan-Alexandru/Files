"""
Velocloud V1
/licence API Calls
"""

from common.parsing import evaluate_model

from . import models
from .velocloud import SBVelocloudV1


def get_edge_licenses(client: SBVelocloudV1, enterprise_id) -> list[models.Licence]:
    """
    API: /license/getEnterpriseEdgeLicenses"
    """
    data = client.post_api(
        endpoint="/license/getEnterpriseEdgeLicenses",
        body={"enterpriseId": enterprise_id},
    )
    return evaluate_model(list[models.Licence], data)


def get_enterprise_proxy_edge_licenses(
    client: SBVelocloudV1, enterprise_proxy_id: int | None = None
) -> list[models.EnterpriseProxyLicense]:
    """
    API: /license/getEnterpriseProxyEdgeLicenses
    """
    body = {"with": ["counts"]}
    if enterprise_proxy_id is not None:
        body["enterpriseProxyId"] = enterprise_proxy_id
    data = client.post_api(
        endpoint="/license/getEnterpriseProxyEdgeLicenses", body=body
    )
    return evaluate_model(list[models.EnterpriseProxyLicense], data)
