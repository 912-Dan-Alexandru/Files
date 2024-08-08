"""
Network Alert History
"""

from typing import Optional

from pydantic import BaseModel


class Device(BaseModel):
    """
    Device Pydantic model
    """

    serial: Optional[str] = None


class Email(BaseModel):
    """
    Email Pydantic model
    """

    sentAt: Optional[str] = None


class Push(BaseModel):
    """
    Push Pydantic model
    """

    sentAt: Optional[str] = None


class Sms(BaseModel):
    """
    Sms Pydantic model
    """

    sentAt: Optional[str] = None


class Webhook(BaseModel):
    """
    Webook Pydantic model
    """

    sentAt: Optional[str] = None


class Destinations(BaseModel):
    """
    Destination Pydantic model
    """

    email: Optional[Email] = None
    push: Optional[Push] = None
    sms: Optional[Sms] = None
    webhook: Optional[Webhook] = None


class NetworkAlertData(BaseModel):
    """
    Network Alert Data Pydantic Model
    """

    name: Optional[str] = None
    url: Optional[str] = None
    changes: Optional[dict] = None


class NetworkAlertHistory(BaseModel):
    """
    Network Alert History Pydantic model
    """

    occurredAt: Optional[str] = None
    alertTypeId: Optional[str] = None
    alertType: Optional[str] = None
    device: Optional[Device] = None
    destinations: Optional[Destinations] = None
    alertData: Optional[NetworkAlertData] = None
