"""
Network Events Model
"""
from typing import List, Optional

from pydantic import BaseModel


class EventData(BaseModel):
    """
    Event Data Pydantic model
    """

    channel: Optional[str] = None
    rssi: Optional[str] = None
    peer_ip: Optional[str] = None
    local_as: Optional[str] = None
    remote_as: Optional[str] = None
    new_state: Optional[str] = None
    error_code: Optional[str] = None
    error_subcode: Optional[str] = None
    desc: Optional[str] = None
    peer_type: Optional[str] = None
    peer: Optional[str] = None
    connection_status: Optional[str] = None
    vpn_type: Optional[str] = None
    peer_contact: Optional[str] = None
    connectivity: Optional[str] = None
    device: Optional[str] = None
    carrier: Optional[str] = None
    msg: Optional[str] = None
    radio: Optional[str] = None
    vap: Optional[str] = None
    client_mac: Optional[str] = None
    client_ip: Optional[str] = None
    aid: Optional[str] = None


class Event(BaseModel):
    """
    Event Pydantic model
    """

    occurredAt: Optional[str] = None
    networkId: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    clientId: Optional[str] = None
    clientDescription: Optional[str] = None
    deviceSerial: Optional[str] = None
    deviceName: Optional[str] = None
    ssidNumber: Optional[int] = None
    ssidName: Optional[str] = None
    eventData: EventData


class NetworkEvents(BaseModel):
    """
    Network Event Pydantic model
    """

    message: Optional[str] = None
    pageStartAt: Optional[str] = None
    pageEndAt: Optional[str] = None
    events: Optional[List[Event]] = None
