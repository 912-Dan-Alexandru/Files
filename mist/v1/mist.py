"""
Southbound Mist v1 Client
"""
from typing import TypeVar

import httpx

from common.parsing import evaluate_model

T = TypeVar("T")


class SBMistV1:
    """
    Mist V1 API Operations
    """

    def __init__(self, host: str, api_key: str):
        self.host = host
        self.api_key = api_key

    def get_api(self, endpoint, response_model: type[T]) -> T:
        """
        Get Request for Mist API
        Raises:
            `httpx.HTTPError`
            `pydantic.ValidationError`
        """
        headers = {"Authorization": "Token " + self.api_key}
        response = httpx.get(self.host + endpoint, headers=headers)
        response.raise_for_status()
        return evaluate_model(response_model, response.json())
