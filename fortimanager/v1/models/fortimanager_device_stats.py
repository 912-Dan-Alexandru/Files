"""
Fortimanager device stats Pydantic model
"""
from enum import Enum


class FortiManagerDeviceStatus(str, Enum):
    """
    FortiManager device stats status Enum class
    """

    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class FmDeviceType(str, Enum):
    """
    Fortimanager device stats type
    """

    ACCESS_POINT = "ap"
    BLE = "ble"
    GATEWAY = "gateway"
    SWITCH = "switch"
    VIRTUAL_CHASSIS = "Virtual Chassis"
    DEVICE = "device"
    MX_EDGES = "mxedges"
