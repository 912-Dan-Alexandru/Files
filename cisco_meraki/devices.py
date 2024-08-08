"""
Meraki API
/devices Endpoint Functions
"""

from common.parsing import evaluate_model

from . import models
from .cisco_meraki import SBMeraki


@SBMeraki.exception_handler
def get_device(client: SBMeraki, serial: str) -> models.DeviceBySerial:
    """
    API: /devices/{serial}
    """
    data = client.api.devices.getDevice(serial)
    return evaluate_model(models.DeviceBySerial, data)


@SBMeraki.exception_handler
def get_management_interface(
    client: SBMeraki, serial: str
) -> models.DeviceManagementInterfaces:
    """
    API: /devices/{serial}/managementInterface
    """
    data = client.api.devices.getDeviceManagementInterface(serial)
    return evaluate_model(models.DeviceManagementInterfaces, data)


@SBMeraki.exception_handler
def update_management_interface(
    client: SBMeraki, serial: str, update_data: models.DeviceManagementInterfaces
) -> models.DeviceManagementInterfaces:
    """
    API: /devices/{serial}/managementInterface
    """
    data = client.api.devices.updateDeviceManagementInterface(
        serial=serial, **update_data.dict(exclude_unset=True, by_alias=True)
    )
    return evaluate_model(models.DeviceManagementInterfaces, data)


@SBMeraki.exception_handler
def update_device(
    client: SBMeraki, serial: str, update_data: models.UpdateDeviceData
) -> models.DeviceBySerial:
    """
    API: PUT /devices/{serial}
    """
    data = client.api.devices.updateDevice(
        serial, **update_data.dict(exclude_none=True)
    )
    return evaluate_model(models.DeviceBySerial, data)


@SBMeraki.exception_handler
def get_device_loss_and_latency_history(
    client: SBMeraki,
    serial: str,
    public_ip: str,
    timespan: int,
) -> list[models.DeviceLossAndLatencyHistory]:
    """
    API: /devices/{serial}/lossAndLatencyHistory
    """
    data = client.api.devices.getDeviceLossAndLatencyHistory(
        serial,
        public_ip,
        timespan=timespan,
    )
    return evaluate_model(list[models.DeviceLossAndLatencyHistory], data)


@SBMeraki.exception_handler
def get_device_switch_ports_statuses(
    client: SBMeraki,
    serial: str,
    timespan: int,
) -> list[models.DeviceSwitchPortsStatuses]:
    """
    API: /switch/{serial}/deviceSwitchPortsStatuses
    """
    data = client.api.switch.getDeviceSwitchPortsStatuses(
        serial,
        timespan=timespan,
    )
    return evaluate_model(list[models.DeviceSwitchPortsStatuses], data)


@SBMeraki.exception_handler
def get_device_switch_ports_statuses_packets(
    client: SBMeraki,
    serial: str,
    timespan: int,
) -> list[models.DeviceSwitchPortsStatusesPackets]:
    """
    API: /switch/{serial}/deviceSwitchPortsStatusesPackets
    """
    data = client.api.switch.getDeviceSwitchPortsStatusesPackets(
        serial,
        timespan=timespan,
    )
    return evaluate_model(list[models.DeviceSwitchPortsStatusesPackets], data)


@SBMeraki.exception_handler
def get_switch_ports(client: SBMeraki, serial: str) -> list[models.SwitchPort]:
    """
    API: /devices/{serial}/switch/ports
    """
    data = client.api.switch.getDeviceSwitchPorts(serial)
    return evaluate_model(list[models.SwitchPort], data)


@SBMeraki.exception_handler
def update_switch_port(
    client: SBMeraki,
    serial: str,
    port_id: str,
    update_data: models.UpdateSwitchPortData,
) -> models.SwitchPort:
    """
    API: /devices/{serial}/switch/ports/{portId}
    """
    data = client.api.switch.updateDeviceSwitchPort(
        serial, port_id, **update_data.dict(exclude_unset=True, by_alias=True)
    )
    return evaluate_model(models.SwitchPort, data)
