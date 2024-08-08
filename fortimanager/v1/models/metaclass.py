"""
This module contains metaclasses for Pydantic models with optional fields.
"""

from typing import Any

from pydantic import BaseModel, Field
from pydantic.fields import ModelField
from pydantic.main import ModelMetaclass


class AllOptional(ModelMetaclass):
    """
    Make every field as optional with Pydantic.
    """

    def __new__(mcs, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = annotations[field] | None
        namespaces["__annotations__"] = annotations
        return super().__new__(mcs, name, bases, namespaces, **kwargs)


class AllOptionalMeta(ModelMetaclass):
    """
    Make every field as optional with Pydantic. Added support for nesting of models.
    """

    def __new__(
        mcs, name: str, bases: tuple[type], namespaces: dict[str, Any], **kwargs
    ):
        annotations: dict = namespaces.get("__annotations__", {})

        for base in bases:
            for base_ in base.__mro__:
                if base_ is BaseModel:
                    break

                annotations.update(base_.__annotations__)
                for k, v in base_.__dict__["__fields__"].items():
                    if isinstance(v, ModelField):
                        namespaces[k] = Field(alias=v.alias)

        namespaces = mcs.__update_annotations(
            namespaces=namespaces, annotations=annotations
        )

        return super().__new__(mcs, name, bases, namespaces, **kwargs)

    @classmethod
    def __update_annotations(
        cls, namespaces: dict[str, Any], annotations
    ) -> dict[str, Any]:
        """
        Update annotations for each field
        """
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = annotations[field] | None

        namespaces["__annotations__"] = annotations
        return namespaces
