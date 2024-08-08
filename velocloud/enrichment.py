"""
Enrichment functions module
"""
from pydantic import ValidationError

from common.models.message_bus import assurance_enrichment
from common.models.velocloud.velocloud_version import VelocloudVersion
from common.southbound.velocloud import SBVelocloudV1, SBVelocloudV2
from common.southbound.velocloud.inventory_enrichment.edge import (
    get_edge_information_v1,
    get_edge_information_v2,
)
from common.southbound.velocloud.inventory_enrichment.enterprise import (
    get_enterprise_information_v1,
    get_enterprise_information_v2,
)
from common.southbound.velocloud.inventory_enrichment.velocloud import (
    InventoryVelocloud,
)
from common.southbound.velocloud.v1.edge import get_edge as get_edge_v1
from common.southbound.velocloud.v1.enterprise import get_enterprise_property
from common.southbound.velocloud.v2.enterprises import get_edge as get_edge_v2
from common.southbound.velocloud.v2.enterprises import get_enterprise


def get_enterprise_data(
    client: SBVelocloudV1 | SBVelocloudV2 | InventoryVelocloud,
    enterprise_information: str,
) -> assurance_enrichment.EnrichedEnterprise | None:
    """
    Get the enrichment enterprise information, from a specific source
    The source is determined by the "client"

    Args:
        client(SBVelocloudV1 | SBVelocloudV2 | InventoryVelocloud): the client
        through data will be retrieved
        enterprise_information(str): the logical id of the enterprise, if
        the event is V2, otherwise the id of the enterprise

    Returns:
        EnrichedEnterprise: the enrichment data of the enterprise
    """
    if isinstance(client, SBVelocloudV2):
        response_v2 = get_enterprise(client, logical_id=enterprise_information)
        return assurance_enrichment.EnrichedEnterprise(
            logical_id=response_v2.logicalId,
            id=response_v2.logicalId if response_v2.logicalId else "",
            name=response_v2.name if response_v2.name else "",
            account_number=response_v2.accountNumber,
        )

    if isinstance(client, SBVelocloudV1):
        response_v1 = get_enterprise_property(
            client,
            enterprise_id=enterprise_information,
            prop="???",
        )

        if not response_v1:
            raise RuntimeError("V1 get_enterprise_property API error!")

        return assurance_enrichment.EnrichedEnterprise(
            logical_id=str(response_v1.enterpriseId),
            id=str(response_v1.id),
            name=response_v1.name,
            account_number="???",
        )

    try:
        if client.api_version == VelocloudVersion.V1:
            return get_enterprise_information_v1(
                client, enterprise_id=enterprise_information
            )

        return get_enterprise_information_v2(
            client, enterprise_logical_id=enterprise_information
        )
    except ValidationError:
        return None


def get_edge_data(
    client: SBVelocloudV1 | SBVelocloudV2 | InventoryVelocloud,
    enterprise_information: str,
    edge_information: str,
) -> assurance_enrichment.EnrichedEdge | None:
    """
    Get the enrichment edge information, from a specific source
    The source is determined by the "client"

    Args:
        client(SBVelocloudV1 | SBVelocloudV2 | InventoryVelocloud): the client
        through data will be retrieved
        enterprise_id(str): the id of the enterprise
        edge_information(str): the id of the edge, if the event is V2, otherwise
        the edge name

    Returns:
        EnrichedEdge: the enrichment data of the edge
    """

    if isinstance(client, SBVelocloudV2):
        response_v2 = get_edge_v2(
            client,
            enterprise_logical_id=enterprise_information,
            edge_logical_id=edge_information,
        )
        return assurance_enrichment.EnrichedEdge(
            id=response_v2.deviceId if response_v2.deviceId else "",
            logical_id=response_v2.logicalId,
            name=response_v2.name if response_v2.name else "",
            custom_field=response_v2.customInfo,
        )
    if isinstance(client, SBVelocloudV1):
        response_v1 = get_edge_v1(
            client,
            customer_id=enterprise_information,
            edge_name=edge_information,
        )

        return assurance_enrichment.EnrichedEdge(
            id=str(response_v1.id),
            logical_id=response_v1.logicalId,
            name=response_v1.name if response_v1.name else "",
            custom_field=response_v1.customInfo,
        )

    try:
        if client.api_version == VelocloudVersion.V1:
            return get_edge_information_v1(
                client, enterprise_id=enterprise_information, edge_name=edge_information
            )

        return get_edge_information_v2(
            client,
            enterprise_logical_id=enterprise_information,
            edge_logical_id=edge_information,
        )
    except ValidationError:
        return None
