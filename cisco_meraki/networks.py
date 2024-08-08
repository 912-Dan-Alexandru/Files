"""
Meraki API
/networks Endpoint Functions
"""


from common.parsing import evaluate_model
from common.southbound.cisco_meraki.models.network import ModifyVlan

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_network(client: SBMeraki, network_id: str) -> models.Network:
    """
    API: /networks/{networkId}
    """
    data = client.api.networks.getNetwork(network_id)
    return evaluate_model(models.Network, data)


@SBMeraki.exception_handler
def get_devices(client: SBMeraki, network_id: str) -> list[models.NetworkDevice]:
    """
    API: /networks/{networkId}/devices
    """
    data = client.api.networks.getNetworkDevices(network_id)
    return evaluate_model(list[models.NetworkDevice], data)


@SBMeraki.exception_handler
def claim_device(client: SBMeraki, network_id: str, serials: list[str]):
    """
    API: /networks/{networkId}/devices/claim
    Sucess 200 Response
    """
    data = client.api.networks.claimNetworkDevices(network_id, serials)
    return data


@SBMeraki.exception_handler
def claim_vmx(
    client: SBMeraki, network_id: str, size: models.VMXSizes
) -> list[models.NetworkDevice]:
    """
    API: /networks/{networkId}/devices/claim
    Success 200 Response
    """
    data = client.api.networks.vmxNetworkDevicesClaim(network_id, size.value)
    return evaluate_model(list[models.NetworkDevice], data)


@SBMeraki.exception_handler
def remove_device(client: SBMeraki, network_id: str, serial: str):
    """
    API: /networks/{networkId}/devices/claim
    Success 204 Response
    """
    data = client.api.networks.removeNetworkDevices(network_id, serial)
    return data


@SBMeraki.exception_handler
def update_network(
    client: SBMeraki, network_id: str, network_data: models.NetworkUpdate
) -> models.Network:
    """
    API: /networks/{networkId}
    """
    data = client.api.networks.updateNetwork(
        network_id, **network_data.dict(exclude_none=True)
    )
    return evaluate_model(models.Network, data)


@SBMeraki.exception_handler
def bind_network(
    client: SBMeraki, network_id: str, template_id: str, auto_bind: bool = False
) -> models.Network:
    """
    API: /networks/{networkId}/bind
    Returns Network model updated with binding info
    """
    current_network = client.api.networks.getNetwork(networkId=network_id)
    current_model = evaluate_model(models.Network, current_network)
    if (
        current_model.isBoundToConfigTemplate
        and current_model.configTemplateId == template_id
    ):
        return current_model
    updated_network = client.api.networks.bindNetwork(
        networkId=network_id, configTemplateId=template_id, autoBind=auto_bind
    )
    return evaluate_model(models.Network, updated_network)


@SBMeraki.exception_handler
def unbind_network(
    client: SBMeraki, network_id: str, retain_configs: bool = False
) -> models.Network:
    """
    API: /networks/{networkId}/unbind
    Returns Network model updated with binding info
    """
    current_network = client.api.networks.getNetwork(networkId=network_id)
    current_model = evaluate_model(models.Network, current_network)
    if not current_model.isBoundToConfigTemplate:
        return current_model
    client.api.networks.unbindNetwork(
        networkId=network_id, retainConfigs=retain_configs
    )

    # DISCLAIMER: upon successful unbind operation,
    # the returned Meraki Network model
    # is still reporting the Network as bound to the template
    # this is why it is recommended to GET the Network again
    updated_network = client.api.networks.getNetwork(networkId=network_id)
    return evaluate_model(models.Network, updated_network)


@SBMeraki.exception_handler
def delete_network(client: SBMeraki, network_id: str):
    """
    API: /networks/{networkId}
    Success: 204 Response
    """
    client.api.networks.deleteNetwork(network_id)


@SBMeraki.exception_handler
def list_network_appliance_vlans(
    client: SBMeraki, network_id: str
) -> list[models.VLANGetResponse]:
    """
    API: /networks/{networkId}/appliance/vlans
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceVlans(network_id)
    return evaluate_model(list[models.VLANGetResponse], data)


@SBMeraki.exception_handler
def list_network_appliance_ports(
    client: SBMeraki, network_id: str
) -> list[models.PortGetResponse]:
    """
    API: /networks/{networkId}/appliance/ports
    Success 200 Response
    """
    data = client.api.appliance.getNetworkAppliancePorts(network_id)
    return evaluate_model(list[models.PortGetResponse], data)


@SBMeraki.exception_handler
def update_network_appliance_port(
    client: SBMeraki, network_id: str, port_id: str, port_data: models.PortUpdate
) -> models.PortGetResponse:
    """
    API: /networks/{networkId}/appliance/ports/{portId}
    """
    data = client.api.appliance.updateNetworkAppliancePort(
        network_id, port_id, **port_data.dict(exclude_none=True)
    )
    return evaluate_model(models.PortGetResponse, data)


@SBMeraki.exception_handler
def get_network_appliance_port(
    client: SBMeraki, network_id: str, port_id: str
) -> models.PortGetResponse:
    """
    API: /networks/{networkId}/appliance/ports/{portId}
    """
    data = client.api.appliance.getNetworkAppliancePort(network_id, port_id)
    return evaluate_model(models.PortGetResponse, data)


@SBMeraki.exception_handler
def get_network_appliance_vlan(
    client: SBMeraki, network_id: str, vlan_id: str
) -> models.VLANGetResponse:
    """
    API:  /networks/{networkId}/appliance/vlans/{vlanId}
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceVlan(network_id, vlan_id)
    return evaluate_model(models.VLANGetResponse, data)


@SBMeraki.exception_handler
def get_network_appliance_single_lan(
    client: SBMeraki, network_id: str
) -> models.SingleLan:
    """
    API:  /networks/{networkId}/appliance/singleLan
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSingleLan(network_id)
    return evaluate_model(models.SingleLan, data)


@SBMeraki.exception_handler
def update_network_appliance_single_lan(
    client: SBMeraki, network_id: str, lan_data: models.SingleLan
) -> models.SingleLan:
    """
    API:  /networks/{networkId}/appliance/singleLan
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceSingleLan(
        network_id, **lan_data.dict(exclude_unset=True, by_alias=True)
    )
    return evaluate_model(models.SingleLan, data)


@SBMeraki.exception_handler
def create_network_appliance_vlan(
    client: SBMeraki, network_id: str, vlan_data: models.CreateVlan
) -> models.CreateVlanResponse:
    """
    API:  /networks/{networkId}/appliance/vlans
    Success 201 Response
    """
    data = client.api.appliance.createNetworkApplianceVlan(
        network_id, **vlan_data.dict(exclude_none=True)
    )
    return evaluate_model(models.CreateVlanResponse, data)


@SBMeraki.exception_handler
def update_network_appliance_vlan(
    client: SBMeraki,
    network_id: str,
    vlan_id: str,
    vlan_data: ModifyVlan,
) -> models.VLANGetResponse:
    """
    API: /networks/{networkId}/appliance/vlans/{vlanId}
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceVlan(
        network_id, vlan_id, **vlan_data.dict(exclude_none=True)
    )
    return evaluate_model(models.VLANGetResponse, data)


@SBMeraki.exception_handler
def delete_network_appliance_vlan(client: SBMeraki, network_id: str, vlan_id: str):
    """
    API: /networks/{networkId}/appliance/vlans/{vlanId}
    Success: 204 Response
    """
    client.api.appliance.deleteNetworkApplianceVlan(network_id, vlan_id)


@SBMeraki.exception_handler
def list_network_appliance_vlans_settings(
    client: SBMeraki, network_id: str
) -> models.NetworkApplianceVlansSettings:
    """
    API: /networks/{networkId}/appliance/vlans/settings
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceVlansSettings(network_id)
    return evaluate_model(models.NetworkApplianceVlansSettings, data)


@SBMeraki.exception_handler
def update_network_appliance_vlans_settings(
    client: SBMeraki,
    network_id: str,
    vlan_data: models.NetworkApplianceVlansSettings,
) -> models.NetworkApplianceVlansSettings:
    """
    API:  /networks/{networkId}/appliance/vlans/settings
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceVlansSettings(
        network_id, **vlan_data.dict(exclude_none=True)
    )
    return evaluate_model(models.NetworkApplianceVlansSettings, data)


def create_network_appliance_static_route(
    client: SBMeraki, network_id: str, static_route_data: models.StaticRouteCreate
) -> models.StaticRouteGet:
    """
    API: /networks/{networkId}/appliance/staticRoutes
    Success 201 Response
    """
    data = client.api.appliance.createNetworkApplianceStaticRoute(
        network_id, **static_route_data.dict(exclude_none=True)
    )
    return evaluate_model(models.StaticRouteGet, data)


@SBMeraki.exception_handler
def list_network_appliance_static_routes(
    client: SBMeraki, network_id: str
) -> list[models.StaticRouteGet]:
    """
    API: /networks/{networkId}/appliance/staticRoutes
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceStaticRoutes(network_id)
    return evaluate_model(list[models.StaticRouteGet], data)


@SBMeraki.exception_handler
def get_network_appliance_static_route(
    client: SBMeraki, network_id: str, static_route_id: str
) -> models.StaticRouteGet:
    """
    API: /networks/{networkId}/appliance/staticRoutes/{staticRouteId}
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceStaticRoute(
        network_id, static_route_id
    )
    return evaluate_model(models.StaticRouteGet, data)


@SBMeraki.exception_handler
def update_network_appliance_static_route(
    client: SBMeraki,
    network_id: str,
    static_route_id: str,
    static_route_data: models.StaticRouteUpdate,
) -> models.StaticRouteGet:
    """
    API: /networks/{networkId}/appliance/staticRoutes/{staticRouteId}
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceStaticRoute(
        network_id, static_route_id, **static_route_data.dict(exclude_none=True)
    )
    return evaluate_model(models.StaticRouteGet, data)


@SBMeraki.exception_handler
def delete_network_appliance_static_route(
    client: SBMeraki, network_id: str, static_route_id: str
):
    """
    API: /networks/{networkId}/appliance/staticRoutes/{staticRouteId}
    Success: 204 Response
    """
    client.api.appliance.deleteNetworkApplianceStaticRoute(network_id, static_route_id)


@SBMeraki.exception_handler
def list_network_appliance_ssids(
    client: SBMeraki, network_id: str
) -> list[models.ApplianceSSIDGetResponses]:
    """
    API: networks/{networkId}/appliance/ssids
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSsids(network_id)
    return evaluate_model(list[models.ApplianceSSIDGetResponses], data)


@SBMeraki.exception_handler
def get_network_appliance_ssid(
    client: SBMeraki, network_id: str, ssid_number: str
) -> models.ApplianceSSIDGetResponses:
    """
    API: /networks/{networkId}/appliance/ssids/{number}
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSsid(network_id, ssid_number)
    return evaluate_model(models.ApplianceSSIDGetResponses, data)


@SBMeraki.exception_handler
def update_network_appliance_ssids(
    client: SBMeraki,
    network_id: str,
    ssid_id: str,
    ssid_data: models.ApplianceSSIDUpdateInput,
) -> models.ApplianceSSIDGetResponses:
    """
    API: /networks/{networkId}/appliance/ssids/{number}
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceSsid(
        network_id, ssid_id, **ssid_data.dict(exclude_unset=True)
    )
    return evaluate_model(models.ApplianceSSIDGetResponses, data)


@SBMeraki.exception_handler
def get_network_appliance_settings(
    client: SBMeraki, network_id: str
) -> models.ApplianceSettingsBase:
    """
    API: /networks/{networkId}/appliance/settings
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSettings(network_id)
    return evaluate_model(models.ApplianceSettingsBase, data)


@SBMeraki.exception_handler
def update_network_appliance_settings(
    client: SBMeraki,
    network_id: str,
    appliance_settings: models.ApplianceSettingsBase,
) -> models.ApplianceSettingsBase:
    """
    API: /networks/{networkId}/appliance/settings
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceSettings(
        network_id, **appliance_settings.dict(exclude_none=True)
    )
    return evaluate_model(models.ApplianceSettingsBase, data)


@SBMeraki.exception_handler
def get_network_appliance_security_intrusion(
    client: SBMeraki, network_id: str
) -> models.SecurityIntrusionModel:
    """
    API: GET /networks/{networkId}/appliance/security/intrusion
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceSecurityIntrusion(network_id)
    return evaluate_model(models.SecurityIntrusionModel, data)


@SBMeraki.exception_handler
def update_network_appliance_security_intrusion(
    client: SBMeraki,
    network_id: str,
    security_intrusion: models.SecurityIntrusionModel,
) -> models.SecurityIntrusionModel:
    """
    API: PUT /networks/{networkId}/appliance/security/intrusion
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceSecurityIntrusion(
        network_id, **security_intrusion.dict(exclude_unset=True, by_alias=True)
    )
    return evaluate_model(models.SecurityIntrusionModel, data)


@SBMeraki.exception_handler
def get_network_appliance_uplink_config_bandwidth_limits(
    client: SBMeraki, network_id: str
) -> models.UplinkConfig:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(
        network_id
    )
    return evaluate_model(models.UplinkConfig, data)


@SBMeraki.exception_handler
def get_network_appliance_uplink_selection(
    client: SBMeraki, network_id: str
) -> models.network.UplinkSelection:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkSelection
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceTrafficShapingUplinkSelection(
        network_id
    )
    return evaluate_model(models.network.UplinkSelection, data)


@SBMeraki.exception_handler
def update_network_appliance_uplink_selection(
    client: SBMeraki, network_id: str, uplink_selection: models.UplinkSelectionUpdate
) -> models.UplinkSelection:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkSelection
    Success: 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceTrafficShapingUplinkSelection(
        network_id, **uplink_selection.dict(exclude_unset=True, by_alias=True)
    )
    return evaluate_model(models.UplinkSelection, data)


@SBMeraki.exception_handler
def update_network_appliance_uplink_config_bandwidth_limits(
    client: SBMeraki, network_id: str, bandwidth_limit_data: models.UplinkConfig
) -> models.UplinkConfig:
    """
    API: /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth
    Success: 200 Response
    """
    params = bandwidth_limit_data.dict(exclude_none=False)
    if params["bandwidthLimits"]["wan2"] is None:
        del params["bandwidthLimits"]["wan2"]

    data = client.api.appliance.updateNetworkApplianceTrafficShapingUplinkBandwidth(
        network_id, **params
    )
    return evaluate_model(models.UplinkConfig, data)


def get_network_appliance_connectivity_monitoring_destinations(
    client: SBMeraki, network_id: str
) -> models.ApplianceConnectivityMonitoringDestinations:
    """
    API: /networks/{networkId}/appliance/connectivityMonitoringDestinations
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceConnectivityMonitoringDestinations(
        network_id
    )
    return evaluate_model(models.ApplianceConnectivityMonitoringDestinations, data)


@SBMeraki.exception_handler
def update_network_appliance_connectivity_monitoring_destinations(
    client: SBMeraki,
    network_id: str,
    uplink_stats_data: models.ApplianceConnectivityMonitoringDestinations,
) -> models.ApplianceConnectivityMonitoringDestinations:
    """
    API: /networks/{networkId}/appliance/connectivityMonitoringDestinations
    Success: 200 Response
    """
    data = (
        client.api.appliance.updateNetworkApplianceConnectivityMonitoringDestinations(
            network_id, **uplink_stats_data.dict(exclude_none=True)
        )
    )
    return evaluate_model(models.ApplianceConnectivityMonitoringDestinations, data)


def get_site_to_site_vpn(client: SBMeraki, network_id: str) -> models.ResponseS2SVPN:
    """
    API: /networks/{networkId}/appliance/vpn/siteToSiteVpn
    Success 200 Response
    """
    data = client.api.appliance.getNetworkApplianceVpnSiteToSiteVpn(network_id)
    return evaluate_model(models.ResponseS2SVPN, data)


@SBMeraki.exception_handler
def update_site_to_site_vpn(
    client: SBMeraki, network_id: str, site_to_site_vpn_data: models.S2SVPNUpdateInput
) -> models.ResponseS2SVPN:
    """
    API: /networks/{networkId}/appliance/vpn/siteToSiteVpn
    Success 200 Response
    """
    data = client.api.appliance.updateNetworkApplianceVpnSiteToSiteVpn(
        network_id, **site_to_site_vpn_data.dict(exclude_none=True)
    )
    return evaluate_model(models.ResponseS2SVPN, data)


@SBMeraki.exception_handler
def get_network_switch_stp(
    client: SBMeraki, network_id: str
) -> models.NetworkSwitchStp:
    """
    GET: /networks/{networkId}/switch/stp
    Success 200 Response
    """
    data = client.api.switch.getNetworkSwitchStp(network_id)
    return evaluate_model(models.NetworkSwitchStp, data)


@SBMeraki.exception_handler
def update_network_switch_stp(
    client: SBMeraki,
    network_id: str,
    data: models.UpdateNetworkSwitchStp,
) -> models.NetworkSwitchStp:
    """
    PUT: /networks/{networkId}/switch/stp
    Success: 200 Response
    """
    data = client.api.switch.updateNetworkSwitchStp(
        network_id, **data.dict(exclude_unset=True)
    )
    return evaluate_model(models.NetworkSwitchStp, data)


@SBMeraki.exception_handler
def get_network_switch_settings(
    client: SBMeraki, network_id: str
) -> models.NetworkSwitchSettings:
    """
    GET: /networks/{networkId}/switch/settings
    Success 200 Response
    """
    data = client.api.switch.getNetworkSwitchSettings(network_id)
    return evaluate_model(models.NetworkSwitchSettings, data)


@SBMeraki.exception_handler
def update_network_switch_settings(
    client: SBMeraki,
    network_id: str,
    data: models.UpdateNetworkSwitchSettings,
) -> models.NetworkSwitchSettings:
    """
    PUT: /networks/{networkId}/switch/settings
    Success: 200 Response
    """
    data = client.api.switch.updateNetworkSwitchSettings(
        network_id, **data.dict(exclude_unset=True)
    )
    return evaluate_model(models.NetworkSwitchSettings, data)


@SBMeraki.exception_handler
def update_network_settings(
    client: SBMeraki, network_id: str, network_settings_data: models.NetworkSettingsPUT
) -> models.NetworkSettingsGET:
    """
    API: /networks/{networkId}/settings
    Success 200 Response
    """
    data = client.api.networks.updateNetworkSettings(
        network_id, **network_settings_data.dict(exclude_none=True)
    )
    return evaluate_model(models.NetworkSettingsGET, data)


@SBMeraki.exception_handler
def get_network_settings(
    client: SBMeraki, network_id: str
) -> models.NetworkSettingsGET:
    """
    API: /networks/{networkId}/settings
    Success 200 Response
    """
    data = client.api.networks.getNetworkSettings(network_id)
    return evaluate_model(models.NetworkSettingsGET, data)
