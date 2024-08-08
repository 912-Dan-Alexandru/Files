"""
Meraki API
/firewall Endpoint Functions
"""

from common.parsing import evaluate_model

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network_appliance_firewall_l3_outbound_firewall_rules(
    client: SBMeraki, network_id: str
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/l3FirewallRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallL3FirewallRules(network_id)
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_l3_firewall_rules(
    client: SBMeraki,
    network_id: str,
    firewall_rules_data: models.NetworkFirewallRules,
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/l3FirewallRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallL3FirewallRules(
        network_id, **firewall_rules_data.dict(exclude_none=True)
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_l3_inbound_firewall_rules(
    client: SBMeraki, network_id: str
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/inboundFirewallRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallInboundFirewallRules(
        network_id
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_inbound_firewall_rules(
    client: SBMeraki,
    network_id: str,
    firewall_rules_data: models.NetworkFirewallRules,
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/inboundFirewallRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallInboundFirewallRules(
        network_id, **firewall_rules_data.dict(exclude_none=True)
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_cellular_firewall_rules(
    client: SBMeraki, network_id: str
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/cellularFirewallRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallCellularFirewallRules(
        network_id
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_cellular_firewall_rules(
    client: SBMeraki,
    network_id: str,
    firewall_rules_data: models.NetworkFirewallRules,
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/cellularFirewallRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallCellularFirewallRules(
        network_id, **firewall_rules_data.dict(exclude_none=True)
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_inbound_cellular_firewall_rules(
    client: SBMeraki, network_id: str
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallInboundCellularFirewallRules(
        network_id
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_inbound_cellular_firewall_rules(
    client: SBMeraki,
    network_id: str,
    firewall_rules_data: models.NetworkFirewallRules,
) -> models.NetworkFirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules
    Success 200 Response

    It is crucial to note that the following Meraki API
    has a bug that prevents rules from being cleared.
    """
    data = (
        client.api.appliance.updateNetworkApplianceFirewallInboundCellularFirewallRules(
            network_id, **firewall_rules_data.dict(exclude={"syslogDefaultRule"})
        )
    )
    return evaluate_model(models.NetworkFirewallRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_l7_firewall_rules(
    client: SBMeraki, network_id: str
) -> models.Layer7FirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/l7FirewallRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallL7FirewallRules(network_id)
    return evaluate_model(models.Layer7FirewallRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_l7_firewall_rules(
    client: SBMeraki,
    network_id: str,
    firewall_rules_data: models.Layer7FirewallRules,
) -> models.Layer7FirewallRules:
    """
    API:  /networks/{networkId}/appliance/firewall/l7FirewallRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallL7FirewallRules(
        network_id, **firewall_rules_data.dict(exclude_none=True)
    )
    return evaluate_model(models.Layer7FirewallRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_port_forwarding_rules(
    client: SBMeraki, network_id: str
) -> models.PortForwardingRules:
    """
    API:  /networks/{networkId}/appliance/firewall/portForwardingRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallPortForwardingRules(
        network_id
    )
    return evaluate_model(models.PortForwardingRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_port_forwarding_rules(
    client: SBMeraki,
    network_id: str,
    firewall_port_forwarding_rules_data: models.PortForwardingRules,
) -> models.PortForwardingRules:
    """
    API:  /networks/{networkId}/appliance/firewall/portForwardingRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallPortForwardingRules(
        network_id, **firewall_port_forwarding_rules_data.dict(exclude_none=True)
    )
    return evaluate_model(models.PortForwardingRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_one_to_one_nat_rules(
    client: SBMeraki, network_id: str
) -> models.OneToOneNatRules:
    """
    API:  GET /networks/{networkId}/appliance/firewall/oneToOneNatRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallOneToOneNatRules(network_id)
    return evaluate_model(models.OneToOneNatRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_one_to_one_nat_rules(
    client: SBMeraki,
    network_id: str,
    payload: models.OneToOneNatRules,
) -> models.OneToOneNatRules:
    """
    API:  PUT /networks/{networkId}/appliance/firewall/oneToOneNatRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallOneToOneNatRules(
        network_id, **payload.dict(exclude_none=True)
    )
    return evaluate_model(models.OneToOneNatRules, data)


@SBMeraki.exception_handler
def get_network_appliance_firewall_one_to_many_nat_rules(
    client: SBMeraki, network_id: str
) -> models.OneToManyNatRules:
    """
    API:  GET /networks/{networkId}/appliance/firewall/oneToManyNatRules
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceFirewallOneToManyNatRules(network_id)
    return evaluate_model(models.OneToManyNatRules, data)


@SBMeraki.exception_handler
def update_network_appliance_firewall_one_to_many_nat_rules(
    client: SBMeraki,
    network_id: str,
    payload: models.OneToManyNatRules,
) -> models.OneToManyNatRules:
    """
    API:  PUT /networks/{networkId}/appliance/firewall/oneToManyNatRules
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceFirewallOneToManyNatRules(
        network_id, **payload.dict(exclude_none=True)
    )
    return evaluate_model(models.OneToManyNatRules, data)
