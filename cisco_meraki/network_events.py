"""
API for network events and network events type
"""
from typing import List

from common.parsing import evaluate_model

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network_events(
    client: SBMeraki,
    network_id: str,
    product_type: str,
    per_page: int,
    starting_after: str,
) -> models.NetworkEvents:
    """
    API: /network/{network_id}/events
    """
    data = client.api.networks.getNetworkEvents(
        network_id,
        productType=product_type,
        perPage=per_page,
        startingAfter=starting_after,
        direction="next",
        total_pages=-1,
    )
    return evaluate_model(models.NetworkEvents, data)


@SBMeraki.exception_handler
def get_network_events_types(
    client: SBMeraki, network_id: str
) -> List[models.NetworkEventsEventTypes]:
    """
    API: /network/{network_id}/events/eventTypes
    """
    data = client.api.networks.getNetworkEventsEventTypes(network_id)
    return evaluate_model(List[models.NetworkEventsEventTypes], data)
