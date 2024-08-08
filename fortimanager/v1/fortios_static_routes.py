"""
FortiOS related API Calls
"""

from common.parsing import evaluate_model
from common.southbound.fortimanager.v1.models.fortimanager_responses import (
    FortiManagerAPIResponseStatusV1,
)

from .fortimanager import SBFortiManagerV1
from .models.fortimanager_requests import (
    FortiManagerAPIRequestParameterV1,
    FortiManagerAPIRequestParameterV1NoData,
    FortiManagerAPIRequestV1,
)
from .models.fortimanager_static_route import (
    CreateFortinetStaticRoute,
    FortinetStaticRoute,
    UpdateFortinetStaticRoute,
)


def get_device_static_routes(
    client: SBFortiManagerV1, device: str, vdom: str
) -> list[FortinetStaticRoute]:
    """

    Select all IPV4 device's static routes entries.
    API: GET "/router/static"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device}/vdom/{vdom}/router/static"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(list[FortinetStaticRoute], response)


def get_device_static_route(
    client: SBFortiManagerV1, device: str, sequence_number: str
) -> FortinetStaticRoute:
    """

    Select a specific IPV4 device's static routes entry by the
    entry's sequence number.
    API: GET "/router/static/{static_route_sequence_number}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device}/vdom/root/router/static/{sequence_number}"
    )
    request = FortiManagerAPIRequestV1(method="get", params=[request_parameter])
    response = client.post_api(request)
    return evaluate_model(FortinetStaticRoute, response)


def create_device_static_route(
    client: SBFortiManagerV1, device: str, static_route: CreateFortinetStaticRoute
) -> FortiManagerAPIResponseStatusV1:
    """

    Create an IPV4 device static routes entry.
    API: POST "/router/static"
    """

    request_parameter = FortiManagerAPIRequestParameterV1[CreateFortinetStaticRoute](
        url=f"pm/config/device/{device}/vdom/root/router/static", data=static_route
    )
    request = FortiManagerAPIRequestV1(
        method="add",
        params=[request_parameter],
    )
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def update_device_static_route(
    client: SBFortiManagerV1,
    device: str,
    static_route: UpdateFortinetStaticRoute,
    sequence_number: str,
) -> FortiManagerAPIResponseStatusV1:
    """

    Update an IPV4 device static routes entry.
    API: SET "/router/static/{static_route_sequence_number}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1[UpdateFortinetStaticRoute](
        url=f"pm/config/device/{device}/vdom/root/router/static/{sequence_number}",
        data=static_route,
    )

    request = FortiManagerAPIRequestV1(method="set", params=[request_parameter])
    response = client.post_api(request, respond_with_data=False)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)


def delete_device_static_route(
    client: SBFortiManagerV1,
    device: str,
    sequence_number: str,
) -> FortiManagerAPIResponseStatusV1:
    """

    Delete an IPV4 device static routes entry.
    API: DELETE "/router/static/{static_route_sequence_number}"
    """
    request_parameter = FortiManagerAPIRequestParameterV1NoData(
        url=f"pm/config/device/{device}/vdom/root/router/static/{sequence_number}"
    )
    request = FortiManagerAPIRequestV1(
        method="delete",
        params=[request_parameter],
    )
    response = client.post_api(request)
    return evaluate_model(FortiManagerAPIResponseStatusV1, response)
