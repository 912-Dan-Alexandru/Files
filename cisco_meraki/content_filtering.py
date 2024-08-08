"""
Meraki API
/content filtering Endpoint Functions
"""
from common.parsing import evaluate_model

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network_appliance_content_filtering(
    client: SBMeraki, network_id: str
) -> models.ContentFilteringGET:
    """
    API:  /networks/{networkId}/appliance/contentFiltering
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceContentFiltering(network_id)
    return evaluate_model(models.ContentFilteringGET, data)


@SBMeraki.exception_handler
def update_network_appliance_content_filtering(
    client: SBMeraki,
    network_id: str,
    content_filtering_data: models.ContentFilteringPUT,
) -> models.ContentFilteringGET:
    """
    API:  /networks/{networkId}/appliance/contentFiltering
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceContentFiltering(
        network_id, **content_filtering_data.dict(exclude_none=True)
    )
    return evaluate_model(models.ContentFilteringGET, data)


@SBMeraki.exception_handler
def get_network_appliance_content_filtering_categories(
    client: SBMeraki, network_id: str
) -> models.ContentFilteringURLCatagories:
    """
    API:  /networks/{networkId}/appliance/contentFiltering
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceContentFilteringCategories(
        network_id
    )
    return evaluate_model(models.ContentFilteringURLCatagories, data)
