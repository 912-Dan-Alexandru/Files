"""
Content Filtering Pydantic model
"""
from typing import List

from pydantic import BaseModel


class URLCategory(BaseModel):
    """
    URLCategory
    """

    id: str
    name: str


class ContentFilteringGET(BaseModel):
    """
    ContentFilteringGET
    """

    blockedUrlCategories: List[URLCategory] | None = None
    blockedUrlPatterns: List[str] | None = None
    allowedUrlPatterns: List[str] | None = None


class ContentFilteringPUT(BaseModel):
    """
    ContentFilteringPUT
    """

    blockedUrlCategories: List[str] | None = None
    blockedUrlPatterns: List[str] | None = None
    allowedUrlPatterns: List[str] | None = None


class ContentFilteringCharacteristics(ContentFilteringGET):
    """
    ContentFilteringCharacteristics
    """

    uuid: str


class ContentFilteringURLCatagories(BaseModel):
    """
    ContentFilteringURLCatagories
    """

    categories: List[URLCategory]


class ContentFilteringURLCatagoriesCharacteristics(ContentFilteringURLCatagories):
    """
    ContentFilteringURLCatagoriesCharacteristics
    """

    uuid: str
