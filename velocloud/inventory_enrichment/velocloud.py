"""
Southbound ServiceInventory V1/V2 client
"""

import httpx
from pydantic import ValidationError, parse_obj_as
from structlog import get_logger

from common.models.velocloud.velocloud_version import VelocloudVersion

log = get_logger()


class InventoryVelocloud:
    """
    Velocloud ServiceInventory V1/V2 API Operations
    """

    def __init__(self, host: str, api_version: VelocloudVersion):
        self.host = host
        self.base_path = "serviceInventory/v4"
        self.api_version = api_version

    def get_api(self, endpoint):
        """
        Get Request for API
        """
        request = httpx.Request(
            "GET",
            self.host + self.base_path + endpoint,
        )
        client = httpx.Client()
        response = client.send(request)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            log.error(
                "Failed to Fetch",
                code=exc.response.status_code,
                url=exc.response.url,
                data=exc.response.text,
            )
        response_json = response.json()
        if isinstance(response_json, dict) and response_json.get("error") is not None:
            error_message = response_json.get("error", {}).get("message")
            log.critical(
                "Error Querying Service Inventory API",
                message=error_message,
            )
            nested_error_messages = self._format_error_message(response_json)
            raise httpx.HTTPError(
                "Service Inventory API Returned Error: "
                + f"{error_message} {nested_error_messages}"
            )
        return response_json

    @staticmethod
    def _format_error_message(json: dict):
        """format the nested error messages into a string"""
        error_message = json.get("error", {}).get("message", "")
        nested_error_messages = [
            res["message"]
            for res in json.get("error", {}).get("data", {}).get("error", [{}])
            if res.get("message")
        ]
        if nested_error_messages:
            nested_error_messages = "; ".join(nested_error_messages)
            return error_message + ": " + nested_error_messages
        return error_message

    @staticmethod
    def evaluate_model_for_single_data(model, data):
        """
        Evaluate the data received from the API and ensure it's correct with Pydantic,
        if not correct will return None
        """
        try:
            return parse_obj_as(model, data)
        except ValidationError as exception_info:
            log.error("Error Validating API Response", exc_info=True)
            raise exception_info
