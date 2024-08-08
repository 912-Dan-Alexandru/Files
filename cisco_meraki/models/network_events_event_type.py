"""
Network Events Event Type
"""

from typing import Optional

from pydantic import BaseModel


class NetworkEventsEventTypes(BaseModel):
    """
    Network Events Event Type Pydantic model
    """

    category: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
