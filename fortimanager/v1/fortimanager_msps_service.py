"""
FortiManager MSPs API Calls
/dvmdb/msp Endpoint
"""

from common.parsing import evaluate_model

from .fortimanager import SBFortiManagerV1
from .models import FortiManagerMSPV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)


def get_fortimanager_info(client: SBFortiManagerV1) -> FortiManagerMSPV1:
    """
    Get all FortiManager MSPs
    API: POST "/sys/status"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(url="/sys/status")
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortiManagerMSPV1, response)
