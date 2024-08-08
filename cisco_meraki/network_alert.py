"""
API for network alert
"""
from typing import List

from common.parsing import evaluate_model

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network_alerts_history(
    client: SBMeraki,
    network_id: str,
    per_page: int,
    starting_after: str,
) -> List[models.NetworkAlertHistory]:
    """
    API: /network/{network_id}/alerts/history
    """
    data = client.api.networks.getNetworkAlertsHistory(
        network_id,
        perPage=per_page,
        startingAfter=starting_after,
        direction="next",
        total_pages=-1,
    )
    return evaluate_model(List[models.NetworkAlertHistory], data)
