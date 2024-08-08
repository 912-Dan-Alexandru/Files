"""
Inventory edge HTTP calls
"""

from common.models.message_bus import EnrichedEdge
from common.southbound.velocloud.inventory_enrichment.velocloud import (
    InventoryVelocloud,
)


def get_edge_information_v1(
    client: InventoryVelocloud, enterprise_id: str, edge_name: str
) -> EnrichedEdge:
    """
    Get extra information about velocloud edge using enterprise and edge id.

    Args:
        client (InventoryVelocloud): client for the ServiceInventory API
        enterprise_id (str): id for a velocloud enterprise.
        edge_name (str): name of a velocloud edge.
    """
    response = client.get_api(
        f"/enrichment/v1/enterprise/{enterprise_id}/edge/{edge_name}"
    )

    return InventoryVelocloud.evaluate_model_for_single_data(EnrichedEdge, response)


def get_edge_information_v2(
    client: InventoryVelocloud, enterprise_logical_id: str, edge_logical_id: str
) -> EnrichedEdge:
    """
    Get extra information about velocloud edge using enterprise and edge id.

    Args:
        client (InventoryVelocloud): client for the ServiceInventory API
        enterprise_logical_id (str): logical id for a velocloud enterprise.
        edge_logical_id (str): logical id for a velocloud edge.
    """
    response = client.get_api(
        f"/enrichment/v2/enterprise/{enterprise_logical_id}/edge/{edge_logical_id}"
    )

    return InventoryVelocloud.evaluate_model_for_single_data(EnrichedEdge, response)
