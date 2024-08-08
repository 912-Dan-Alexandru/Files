"""
File that contain the wrapper function used for V1 and V2 of  enterprise velocloud API
"""

import common.southbound.velocloud.v1.enterprise as enterprise_v1
import common.southbound.velocloud.v2.enterprises as enterprise_v2
from common.southbound.velocloud import SBVelocloudV1, SBVelocloudV2
from common.southbound.velocloud.v1.enterprise_proxy import get_proxy_enterprises
from common.southbound.velocloud.v1.models.enterprise import VeloEnterpriseV1
from common.southbound.velocloud.v2.models.enterprise import VeloEnterpriseV2


def get_enterprises(
    client: SBVelocloudV2 | SBVelocloudV1,
) -> list[VeloEnterpriseV1] | list[VeloEnterpriseV2]:
    """
    wrapper of get enterprise for V2 or V1
    if the client is instane of SBVelocloudV1 will be call V1
    Args:
        client (SBVelocloudV2 | SBVelocloudV1): client to run the api

    Returns:
       list of all enterprises
    """
    if isinstance(client, SBVelocloudV1):
        return get_proxy_enterprises(client)
    return enterprise_v2.get_enterprises(client)


def get_events(
    client: SBVelocloudV1 | SBVelocloudV2,
    enterprise_id: str,
    next_page_link: str | None,
    time: str,
    time_end: str,
):
    """
    wrapper of function get_event that use V1 or V2 method

    Args:
        client (SBVelocloudV1 | SBVelocloudV2): client to run the api
        id (str): id or logical_id using for call
        next_page_link (str | None): next page for the query next
        time (str): Start time in string
        time_end (str): End time in string

    Returns:
       object Event V1 or V2
    """
    if isinstance(client, SBVelocloudV1):
        return enterprise_v1.get_events(
            client=client,
            enterprise_id=enterprise_id,
            time=time,
            time_end=time_end,
            next_page_link=next_page_link if next_page_link is not None else "",
        )

    return enterprise_v2.get_events(
        client=client,
        logical_id=enterprise_id,
        start=time,
        end=time_end,
        next_page_link=next_page_link if next_page_link is not None else "",
    )


def get_enterprise_id(enterprise: VeloEnterpriseV2 | VeloEnterpriseV1) -> str:
    """
    Method that get the ID of enterprise normal ID for V1 and logicalID for V2

    Args:
        enterprise (VeloEnterpriseV2 | VeloEnterpriseV1): _description_

    Raises:
        ReferenceError: _description_

    Returns:
        str: _description_
    """
    if isinstance(enterprise, VeloEnterpriseV2):
        if not enterprise.logicalId:
            raise ValueError("Invalid enterprise")
        return str(enterprise.logicalId)
    if not enterprise.id:
        raise ValueError("Invalid enterprise")
    return str(enterprise.id)
