"""
Velocloud V1
/enterprise
"""

from common.parsing import evaluate_model
from common.tools.tmf_logger import TMFLogger

from . import models
from .models import enterprise_alert
from .velocloud import SBVelocloudV1

logger = TMFLogger()


def get_enterprise_alerts(
    client: SBVelocloudV1,
    enterprise_id,
    interval_start: str,
    interval_end: str,
    limit: int,
) -> enterprise_alert.GetResponse:
    """
    API: /enterprise/getEnterpriseAlerts
    Gets past triggered alerts for the specified enterprise.
    interval_start and interval_end are TZ Formatted Time
    2022-07-07T16:32:54.000Z
    """
    body = enterprise_alert.GetRequestBody(
        enterpriseId=enterprise_id,
        interval=enterprise_alert.GetRequestInterval(
            start=interval_start, end=interval_end
        ),
        filter=enterprise_alert.GetRequestFilter(limit=limit),
    )
    data = client.post_api("/enterprise/getEnterpriseAlerts", body.dict())
    return evaluate_model(enterprise_alert.GetResponse, data)


def get_enterprise_property(
    client: SBVelocloudV1, enterprise_id: int, prop: str
) -> models.VeloEnterprisePropertyV1 | None:
    """
    API: /enterprise/getEnterpriseProperty

    TODO: Explain why this is Union of None.
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseProperty",
        body={"name": prop, "enterpriseId": enterprise_id},
    )
    return evaluate_model(models.VeloEnterprisePropertyV1 | None, data)


def get_specific_operator_configurations(
    client: SBVelocloudV1, enterprise_id
) -> list[models.VeloSpecificOperatorConfigurationV1]:
    """
    API: /enterprise/getEnterpriseSpecificOperatorConfigurations
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseSpecificOperatorConfigurations",
        body={
            "enterpriseId": enterprise_id,
            "withEdgeCount": True,
            "withImageInfo": True,
        },
    )
    return evaluate_model(list[models.VeloSpecificOperatorConfigurationV1], data)


def get_configurations(
    client: SBVelocloudV1, enterprise_id: int
) -> list[models.VeloEnterpriseConfigurationV1]:
    """
    API: /enterprise/getEnterpriseConfigurations
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseConfigurations",
        body={"enterpriseId": enterprise_id, "with": ["modules", "edgeCount"]},
    )
    return evaluate_model(list[models.VeloEnterpriseConfigurationV1], data)


def get_operator_configuration(
    client: SBVelocloudV1, enterprise_id
) -> models.VeloSpecificOperatorConfigurationV1:
    """
    API: /enterprise/getEnterpriseOperatorConfiguration
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseOperatorConfiguration",
        body={"enterpriseId": enterprise_id},
    )
    return evaluate_model(models.VeloSpecificOperatorConfigurationV1, data)


def get_enterprise_edges(
    client: SBVelocloudV1, edge_id: int, enterprise_id: int
) -> list[models.EnterpriseEdge]:
    """
    API: /enterprise/getEnterpriseEdges
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseEdges",
        body={
            "enterpriseId": enterprise_id,
            "edgeIds": [edge_id],
            "with": ["configuration", "licenses"],
        },
    )
    return evaluate_model(list[models.EnterpriseEdge], data)


def get_users(client: SBVelocloudV1, enterprise_id) -> list[models.EnterpriseUser]:
    """
    API: /enterprise/getEnterpriseUsers
    """
    data = client.post_api(
        endpoint="/enterprise/getEnterpriseUsers",
        body={"enterpriseId": enterprise_id},
    )

    return evaluate_model(list[models.EnterpriseUser], data)


def clone_enterprise(client: SBVelocloudV1, body: dict) -> models.CloneEnterprise:
    """
    Clone Enterprise
    API: /enterprise/cloneEnterpriseV2
    """
    data = client.post_api(
        endpoint="/enterprise/cloneEnterpriseV2",
        body=body,
    )
    return evaluate_model(models.CloneEnterprise, data)


def delete_enterprise(
    client: SBVelocloudV1, swvc_vendor_id
) -> models.DeleteEnterpriseResponse:
    """
    API: /enterprise/deleteEnterprise
    """
    data = client.post_api(
        endpoint="/enterprise/deleteEnterprise",
        body={"enterpriseId": swvc_vendor_id},
    )
    return evaluate_model(models.DeleteEnterpriseResponse, data)


def get_events(
    client: SBVelocloudV1,
    enterprise_id: str,
    time: str,
    time_end: str,
    next_page_link: str,
) -> models.VeloEventV1:
    """
    API: /event/getEnterpriseEvents
    """
    if next_page_link:
        body = {
            "enterpriseId": int(enterprise_id),
            "interval": {"start": int(time), "end": int(time_end)},
            "nextPageLink": next_page_link,
        }
    else:
        body = {
            "enterpriseId": int(enterprise_id),
            "interval": {"start": int(time), "end": int(time_end)},
        }
    data = client.post_api("/event/getEnterpriseEvents", body)
    return evaluate_model(models.VeloEventV1, data)
