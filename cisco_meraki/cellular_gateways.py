"""
Meraki API
/networks/{networkId}/cellularGateway Endpoint Functions
"""

from common.parsing import evaluate_model
from .cisco_meraki import SBMeraki
from . import models


@SBMeraki.exception_handler
def get_cellular_gateway_lan_settings(
    client: SBMeraki, serial: str
) -> models.CellularGatewayLanSettings:
    """
    API: /devices/{serial}/cellularGateway/lan
    """
    data = client.api.cellularGateway.getDeviceCellularGatewayLan(serial=serial)
    lan_settings = evaluate_model(models.CellularGatewayLanSettings, data)
    if lan_settings is None:
        raise RuntimeError("Unexpected format")
    return lan_settings


@SBMeraki.exception_handler
def update_cellular_gateway_lan_settings(
    client: SBMeraki,
    serial: str,
    update_request: models.CellularGatewayLanSettingsUpdateRequest,
) -> models.CellularGatewayLanSettings:
    """
    API: /devices/{serial}/cellularGateway/lan
    """
    data = client.api.cellularGateway.updateDeviceCellularGatewayLan(
        serial=serial,
        reservedIpRanges=update_request.reservedIpRanges,
        fixedIpAssignments=update_request.fixedIpAssignments,
    )
    update_lan_settings = evaluate_model(models.CellularGatewayLanSettings, data)
    if update_lan_settings is None:
        raise RuntimeError("Unexpected format")
    return update_lan_settings


@SBMeraki.exception_handler
def get_network_cellular_gateway_subnet_pool(
    client: SBMeraki, network_id: str
) -> models.SubnetPool:
    """
    API: /networks/{networkId}/cellularGateway/subnetPool
    Success 200 Response
    """
    data = client.api.cellularGateway.getNetworkCellularGatewaySubnetPool(network_id)
    return evaluate_model(models.SubnetPool, data)


@SBMeraki.exception_handler
def update_network_cellular_gateway_subnet_pool(
    client: SBMeraki,
    network_id: str,
    network_cellular_gateway_subnet_pool_request: models.UpdateSubnetPoolData,
) -> models.SubnetPool:
    """
    API:  /networks/{networkId}/cellularGateway/subnetPool
    Success 200 Response
    """
    data = client.api.cellularGateway.updateNetworkCellularGatewaySubnetPool(
        network_id,
        **network_cellular_gateway_subnet_pool_request.dict(exclude_unset=True),
    )
    return evaluate_model(models.SubnetPool, data)


@SBMeraki.exception_handler
def get_dhcp(client: SBMeraki, network_id: str) -> models.CellularGatewayDhcp:
    """
    API: /networks/{networkId}/cellularGateway/dhcp
    Success 200 Response
    """
    data = client.api.cellularGateway.getNetworkCellularGatewayDhcp(network_id)
    return evaluate_model(models.CellularGatewayDhcp, data)


@SBMeraki.exception_handler
def update_dhcp(
    client: SBMeraki, network_id: str, dhcp_request: models.CellularGatewayDhcp
) -> models.CellularGatewayDhcp:
    """
    API: /networks/{networkId}/cellularGateway/dhcp
    Success 200 Response
    """
    data = client.api.cellularGateway.updateNetworkCellularGatewayDhcp(
        network_id, **dhcp_request.dict(exclude_unset=True)
    )
    return evaluate_model(models.CellularGatewayDhcp, data)
