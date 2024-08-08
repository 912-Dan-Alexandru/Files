"""
Velocloud V1 Enterprise Alerts
"""


from typing import Any, List, Optional

from pydantic import BaseModel

from ..common import ResponseMetadata


class VeloEnterpriseAlertNotificationV1(BaseModel):
    """
    Notified Party List
    """

    enterpriseAlertTriggerId: int
    smsList: List
    emailList: List[str]
    enterpriseUserList: List
    mobileList: List
    snmpList: List
    webhookList: List
    notificationTime: str


class VeloEnterpriseAlertV1(BaseModel):
    """
    Velocloud V1 Enterprise Alert Model
    """

    id: Optional[int] = None
    created: Optional[str] = None
    triggerTime: Optional[str] = None
    enterpriseAlertConfigurationId: Optional[int] = None
    enterpriseId: Optional[int] = None
    edgeId: Optional[int] = None
    edgeName: Optional[str] = None
    linkId: Optional[Any] = None
    linkName: Optional[Any] = None
    enterpriseObjectId: Optional[Any] = None
    enterpriseObjectName: Optional[Any] = None
    name: Optional[str] = None
    type: Optional[str] = None
    state: Optional[str] = None
    stateSetTime: Optional[str] = None
    lastContact: Optional[str] = None
    firstNotificationSeconds: Optional[int] = None
    maxNotifications: Optional[int] = None
    notificationIntervalSeconds: Optional[int] = None
    resetIntervalSeconds: Optional[int] = None
    comment: Optional[str] = None
    nextNotificationTime: Optional[str] = None
    remainingNotifications: Optional[int] = None
    timezone: Optional[str] = None
    locale: Optional[str] = None
    modified: Optional[str] = None
    notifications: Optional[List[VeloEnterpriseAlertNotificationV1]] = None


class GetResponse(BaseModel):
    """
    Response model for /enterprise/getEnterpriseAlerts
    """

    metaData: Optional[ResponseMetadata] = None
    data: Optional[List[VeloEnterpriseAlertV1]] = None


class GetRequestInterval(BaseModel):
    """
    Start and End UNIX timestamp in miliseconds
    """

    start: str
    end: str


class GetRequestFilter(BaseModel):
    """
    Limit of results
    """

    limit: int


class GetRequestBody(BaseModel):
    """
    Request Body for /enterprise/getEnterpriseAlerts
    """

    enterpriseId: int
    interval: GetRequestInterval
    filter: GetRequestFilter
