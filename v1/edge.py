"""
Velocloud V1
/edge
"""
from typing import List

from common.parsing import evaluate_model

from . import models
from .velocloud import SBVelocloudV1


def get_edge(
    client: SBVelocloudV1, customer_id=None, edge_name=None, edge_logical_id=None
) -> models.Edge:
    """
    API: /edge/getEdge
    """
    body = {"with": ["configuration", "site"]}
    if customer_id is not None:
        body["enterpriseId"] = customer_id
    if edge_logical_id is not None:
        body["logicalId"] = edge_logical_id
    if edge_name is not None:
        body["name"] = edge_name
    data = client.post_api("/edge/getEdge", body)

    return evaluate_model(models.Edge, data)


def get_configuration_stack(
    client: SBVelocloudV1, edge_id, enterprise_id
) -> List[models.VeloSpecificOperatorConfigurationV1]:
    """
    API: /edge/getEdgeConfigurationStack
    """
    data = client.post_api(
        endpoint="/edge/getEdgeConfigurationStack",
        body={
            "edgeId": edge_id,
            "enterpriseId": enterprise_id,
            "with": ["modules"],
        },
    )
    return evaluate_model(List[models.VeloSpecificOperatorConfigurationV1], data)


def provision_edge(client: SBVelocloudV1, body: dict) -> models.EdgeProvisionResponse:
    """
    API: /edge/edgeProvision
    """
    data = client.post_api(
        endpoint="/edge/edgeProvision",
        body=body,
    )
    return evaluate_model(models.EdgeProvisionResponse, data)


def delete_edge(
    client: SBVelocloudV1, edge_vendor_id, swvc_vendor_id
) -> List[models.VeloEnterpriseProxyInsertEnterpriseProxyEnterprise]:
    """
    API: /edge/deleteEdge
    """
    data = client.post_api(
        endpoint="/edge/deleteEdge",
        body={"ids": [edge_vendor_id], "enterpriseId": swvc_vendor_id},
    )
    return evaluate_model(
        List[models.VeloEnterpriseProxyInsertEnterpriseProxyEnterprise], data
    )


def update_attributes(
    client: SBVelocloudV1, swvc_vendor_id, edge_vendor_id, update_dict: dict
) -> models.DeleteEnterpriseResponse:
    """
    API: /edge/updateEdgeAttributes
    """
    data = client.post_api(
        endpoint="/edge/updateEdgeAttributes",
        body={
            "enterpriseId": swvc_vendor_id,
            "id": edge_vendor_id,
            "_update": update_dict,
        },
    )
    return evaluate_model(models.DeleteEnterpriseResponse, data)
