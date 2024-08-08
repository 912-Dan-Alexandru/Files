"""
Inventory enterprise HTTP calls
"""


from common.models.message_bus import EnrichedEnterprise
from common.southbound.velocloud.inventory_enrichment.velocloud import (
    InventoryVelocloud,
)


def get_enterprise_information_v1(
    client: InventoryVelocloud, enterprise_id: str
) -> EnrichedEnterprise:
    """
    Get extra information about velocloud enterprise using enterprise id.

    Args:
        client (InventoryVelocloud): client for the ServiceInventory API
        enterprise_id (str): id for a velocloud enterprise.

    """
    response = client.get_api(f"/enrichment/v1/enterprise/{enterprise_id}")

    return InventoryVelocloud.evaluate_model_for_single_data(
        EnrichedEnterprise, response
    )


def get_enterprise_information_v2(
    client: InventoryVelocloud, enterprise_logical_id: str
) -> EnrichedEnterprise:
    """
    Get extra information about velocloud enterprise using enterprise id.

    Args:
        client (InventoryVelocloud): client for the ServiceInventory API
        enterprise_logical_id (str): logical id for a velocloud enterprise.

    """
    response = client.get_api(f"/enrichment/v2/enterprise/{enterprise_logical_id}")
    return InventoryVelocloud.evaluate_model_for_single_data(
        EnrichedEnterprise, response
    )
