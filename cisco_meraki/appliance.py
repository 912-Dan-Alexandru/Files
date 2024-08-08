"""
Meraki API
/appliance Endpoint Functions
"""

from meraki.exceptions import APIError

from common.parsing import evaluate_model
from common.tools.tmf_logger import TMFLogger

from . import models
from .cisco_meraki import SBMeraki
from .messages import MerakiMessages as Messages
from .models.appliance_query_params import (
    UplinksLossAndLatencyQueryParams,
    UplinksStatusesQueryParams,
    UplinksUsageByNetworkQueryParams,
    VpnStatsQueryParams,
)

logger = TMFLogger()


@SBMeraki.exception_handler
def get_appliance_uplinks_statuses(
    client: SBMeraki,
    organization_id: str,
    params: UplinksStatusesQueryParams = UplinksStatusesQueryParams(),
) -> list[models.OrganizationApplianceUplinksStatuses]:
    """
    API: /organizations/{organizationId}/appliance/uplink/statuses
    """
    data = client.api.appliance.getOrganizationApplianceUplinkStatuses(
        organizationId=organization_id, **params.dict(exclude_none=True, by_alias=True)
    )
    return evaluate_model(list[models.OrganizationApplianceUplinksStatuses], data)


@SBMeraki.exception_handler
def get_appliance_uplinks_usage_by_network(
    client: SBMeraki,
    organization_id: str,
    params: UplinksUsageByNetworkQueryParams = UplinksUsageByNetworkQueryParams(),
) -> list[models.OrganizationApplianceUplinksUsageByNetwork]:
    """
    API: /organizations/{organizationId}/appliance/uplinks/usage/byNetwork
    Success 200 Response
    """
    data = client.api.appliance.getOrganizationApplianceUplinksUsageByNetwork(
        organizationId=organization_id, **params.dict(exclude_none=True, by_alias=True)
    )

    return evaluate_model(list[models.OrganizationApplianceUplinksUsageByNetwork], data)


@SBMeraki.exception_handler
def get_organization_appliance_uplink_vpn_stats(
    client: SBMeraki,
    organization_id: str,
    params: VpnStatsQueryParams = VpnStatsQueryParams(),
) -> list[models.OrganizationApplianceVpnStats]:
    """
    API: /organizations/{organizationId}/appliance/vpn/stats
    Success 200 Response
    """
    data = client.api.appliance.getOrganizationApplianceVpnStats(
        organizationId=organization_id, **params.dict(exclude_none=True, by_alias=True)
    )

    return evaluate_model(list[models.OrganizationApplianceVpnStats], data)


@SBMeraki.exception_handler
def get_network_appliance_security_malware_settings(
    client: SBMeraki, network_id: str
) -> models.NetworkApplianceMalwareProtection:
    """
    API: GET /networks/{networkId}/appliance/security/malware
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSecurityMalware(network_id)
    return evaluate_model(models.NetworkApplianceMalwareProtection, data)


@SBMeraki.exception_handler
def update_network_appliance_security_malware_settings(
    client: SBMeraki,
    network_id: str,
    payload: models.NetworkApplianceMalwareProtection,
) -> models.NetworkApplianceMalwareProtection:
    """
    API: PUT /networks/{networkId}/appliance/security/malware
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceSecurityMalware(
        network_id, **payload.dict(by_alias=True)
    )
    return evaluate_model(models.NetworkApplianceMalwareProtection, data)


@SBMeraki.exception_handler
def get_organization_device_uplink_loss_and_latency(
    client: SBMeraki,
    organization_id: str,
    params: UplinksLossAndLatencyQueryParams = UplinksLossAndLatencyQueryParams(),
) -> list[models.UplinksLossAndLatency]:
    """
    API: /organizations/{organizationId}/device/uplinksLossAndLatency
    Success 200 Response
    """
    data = client.api.organizations.getOrganizationDevicesUplinksLossAndLatency(
        organizationId=organization_id, **params.dict(exclude_none=True, by_alias=True)
    )

    return evaluate_model(list[models.UplinksLossAndLatency], data)


@SBMeraki.exception_handler
def get_network_appliance_traffic_shaping_uplink_selection(
    client: SBMeraki,
    network_id: str,
) -> models.TrafficShapingUplinkSelection | None:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkSelection
    """
    try:
        data = client.api.appliance.getNetworkApplianceTrafficShapingUplinkSelection(
            networkId=network_id
        )
    except APIError as exc:
        if exc.status in [400]:
            logger.log(Messages.UNSUPPORTED_REQUEST)
            return None
        raise exc
    return evaluate_model(models.TrafficShapingUplinkSelection, data)


@SBMeraki.exception_handler
def get_network_appliance_traffic_shaping_uplink_bandwidth(
    client: SBMeraki,
    network_id: str,
) -> models.TrafficShapingUplinkBandwidth | None:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth
    """
    try:
        data = client.api.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(
            networkId=network_id
        )
    except APIError as exc:
        if exc.status in [400]:
            logger.log(Messages.UNSUPPORTED_REQUEST)
            return None
        raise exc
    return evaluate_model(models.TrafficShapingUplinkBandwidth, data)


@SBMeraki.exception_handler
def get_switch_port_status(
    client: SBMeraki,
    organization_id: str,
) -> models.OrganizationSwitchPortsBySwitch | None:
    """
    API: /organizations/{organizationId}/switch/ports/statuses/bySwitch
    """
    try:
        data = client.api.switch.getOrganizationSwitchPortsBySwitch(
            organization_id
        )
    except APIError as exc:
        if exc.status in [400]:
            TMFLogger().log(Messages.UNSUPPORTED_REQUEST)
            return None
        raise exc

    return evaluate_model(models.OrganizationSwitchPortsBySwitch, data)
