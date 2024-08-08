"""
Service Inventory Connector
"""

from typing import Protocol

from httpx import HTTPError
from pydantic import ValidationError
from structlog import get_logger

from common.models import Service
from common.models.notifications.vbit_snow import PostModel
from common.models.settings import ConfigTMFServices
from common.southbound.dxl.common_methods import (
    delete_inventory_service,
    get_inventory_service,
    get_inventory_snow_service,
)

logger = get_logger()


class ServiceInventoryConnector(Protocol):
    """
    Interface used to interact with Service Inventory
    """

    def get_service(self, service_id: str | None) -> Service | None:
        """
        Method to get a service from a service id
        """

    def delete_service(self, service_id: str) -> None:
        """
        Method to delete a service by service id
        """

    def get_snow_service(self, service_id: str | None) -> list[PostModel] | None:
        """
        Method to get a list post model from a service id
        """


class ServiceInventoryHttp:
    """
    Class containing the methods for interacting with the Service Inventory via API
    """

    def __init__(self, tmf_services: ConfigTMFServices):
        self.tmf_services = tmf_services

    def get_snow_service(self, service_id: str | None) -> list[PostModel] | None:
        """
        Retrieve Snow PostModel from Inventory API
        """
        if service_id is None:
            logger.error("VBIT SNOW Convertor: Service ID is None")
            return None

        try:
            post_model = get_inventory_snow_service(self.tmf_services, service_id)
        except HTTPError:
            logger.warning(
                "Error getting service from the Service Inventory API.",
                base_url=self.tmf_services.service_inventory,
                service_id=service_id,
            )
            return None
        except ValidationError:
            logger.error("Error Validating API Response", exc_info=True)
            return None

        return post_model

    def get_service(self, service_id: str | None) -> Service | None:
        """
        Get Service data from Inventory API
        """
        if service_id is None:
            logger.error("VBIT SNOW Convertor: Service ID is None")
            return None

        try:
            service = get_inventory_service(self.tmf_services, service_id)
        except HTTPError:
            logger.warning(
                "Error getting service from the Service Inventory API.",
                base_url=self.tmf_services.service_inventory,
                service_id=service_id,
            )
            return None
        except ValidationError:
            logger.error("Error Validating API Response", exc_info=True)
            return None

        return service

    def delete_service(self, service_id: str) -> None:
        """
        Delete Service from Inventory API
        """
        try:
            delete_inventory_service(self.tmf_services, service_id)
        except HTTPError:
            logger.warning(
                "Error deleting service from the Service Inventory API.",
                base_url=self.tmf_services.service_inventory,
                service_id=service_id,
            )
