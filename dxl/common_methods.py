"""
Common internal API calls
"""

from pydantic import parse_obj_as

from common.models.notifications.vbit_snow import PostModel
from common.models.service import Service
from common.models.settings import ConfigTMFServices

from . import APIClient


def get_inventory_service(tmf_services: ConfigTMFServices, service_id: str) -> Service:
    """
    Get Service from Inventory
    Exceptions:
      - httpx.HTTPError
      - pydantic.ValidationError
    """
    client = APIClient(endpoint=tmf_services.service_inventory)
    response = client.request_get("/service/" + service_id)
    return Service.parse_obj(response.json())


def get_inventory_snow_service(
    tmf_services: ConfigTMFServices, service_id: str
) -> list[PostModel]:
    """
    Get list PostModel from Inventory
    Exceptions:
      - httpx.HTTPError
      - pydantic.ValidationError
    """
    client = APIClient(endpoint=tmf_services.service_inventory)
    response = client.request_get("/service/snow/" + service_id)
    return parse_obj_as(list[PostModel], response.json())


def delete_inventory_service(tmf_services: ConfigTMFServices, service_id: str):
    """
    Delete Service from Inventory
    Exceptions:
      - httpx.HTTPError
    """
    client = APIClient(endpoint=tmf_services.service_inventory)
    response = client.request_delete("/service/" + service_id)
    return response


def get_inventory_services(tmf_services: ConfigTMFServices) -> list[Service]:
    """
    Get Services from Inventory
    Exceptions:
      - httpx.HTTPError
      - pydantic.ValidationError
    """
    client = APIClient(endpoint=tmf_services.service_inventory)
    response = client.request_get("/service")
    return parse_obj_as(list[Service], response.json())
