"""
Service Catalog Connector
"""

import json
from typing import Protocol

import httpx
from fastapi import HTTPException, Request
from pydantic import parse_obj_as

from common.catalog import AVAILABLE_SCHEMAS, AVAILABLE_SPECIFICATIONS
from common.catalog.fortimanager.specifications.version_4_1_0.constants import (
    VERSION as fortimanager_specification_version,
)
from common.catalog.meraki.specifications.version_1_0_0.constants import (
    VERSION as meraki_specification_version,
)
from common.catalog.mist.specifications.version_4_1_0.constants import (
    VERSION as mist_specification_version,
)
from common.catalog.velocloud.specifications.version_4_1_0.constants import (
    VERSION as velocloud_specification_version,
)
from common.errors import ErrorMessage
from common.models import Service
from common.models.catalog.service_schema import ServiceSchemaCreate
from common.models.catalog.service_specification import ServiceSpecification
from common.models.enums import (
    FortiManagerServiceType,
    MerakiServiceType,
    MistServiceType,
    VelocloudServiceType,
)
from common.models.settings import ConfigTMFServices
from common.southbound.dxl.api_client import APIClient
from common.tools import TMFLogger
from common.tools.tmf_href import make_host_url

from .messages import CatalogConnectorMessages as Messages

logger = TMFLogger()
VALUE_SCHEMA_LOCATION = "@valueSchemaLocation"
PARTY_MANAGEMENT_SPECIFICATION_NAME = "Party Management"


class ServiceCatalogConnector(Protocol):
    """
    Interface used to interact with Service Catalog
    """

    def get_schema_by_id(self, schema_id) -> ServiceSchemaCreate | None:
        """
        Get schema by id
        """

    def get_service_specification_by_id(self, id_: str) -> ServiceSpecification | None:
        """
        Get service spec by id
        """

    def get_service_specification_by_name_version_pair(
        self, name: str, version: str
    ) -> ServiceSpecification | None:
        """
        Get service spec by name and version
        """

    def get_service_specification(self, service: Service) -> ServiceSpecification:
        """
        Method to get service specification
        """

    def get_spec_chars_name_to_value_type(self, spec_id: str) -> dict[str, str | None]:
        """
        Method to get specification chars name to value type
        """

    def get_catalog_href(self, request: Request, spec_id: str) -> str:
        """
        Method to generate catalog href
        """


class ServiceCatalogConnectorHttp:
    """
    Service Catalog Connector HTTP
    """

    def __init__(self, tmf_serivces: ConfigTMFServices):
        self.tmf_services: ConfigTMFServices = tmf_serivces

    def get_schema_by_id(self, schema_id) -> ServiceSchemaCreate:
        """
        Get schema by schema id from Catalog
        Exceptions:
        - httpx.HTTPError
        - pydantic.ValidationError
        """
        client = APIClient(endpoint=self.tmf_services.service_catalog)
        response = client.request_get(f"serviceSchema/{schema_id}")
        return parse_obj_as(ServiceSchemaCreate, response.json())

    def get_service_specification_by_id(self, id_: str) -> ServiceSpecification:
        """
        Get Service Specification from Catalog
        Exceptions:
        - httpx.HTTPError
        - pydantic.ValidationError
        """
        client = APIClient(endpoint=self.tmf_services.service_catalog)
        response = client.request_get(f"/serviceSpecification/{id_}")
        return parse_obj_as(ServiceSpecification, response.json())

    def get_service_specification_by_name_version_pair(
        self, name: str, version: str
    ) -> ServiceSpecification:
        """
        Get Service Specification from Catalog by name and version
        Exceptions:
        - httpx.HTTPError
        - pydantic.ValidationError
        """
        client = APIClient(endpoint=self.tmf_services.service_catalog)
        response = client.request_get(
            f"/serviceSpecification?name={name}&version={version}"
        )
        specifications = parse_obj_as(list[ServiceSpecification], response.json())
        return specifications[0]

    def get_service_specification(self, service: Service) -> ServiceSpecification:
        """
        Get service specification data from Catalog API by id if the
        service specification id is present, otherwise it will use the
        specification name and version as query parameters to get it.
        For example: Get from Catalog API the swVc version 3.0 specification.
        """
        if service.serviceSpecification.id:
            try:
                return self.get_service_specification_by_id(
                    service.serviceSpecification.id,
                )

            except httpx.HTTPError as http_error:
                logger.log(
                    Messages.ERROR_FETCHING_SPEC,
                    id=service.serviceSpecification.id,
                    name=service.serviceSpecification.name,
                    version=service.serviceSpecification.version,
                    exc_info=True,
                )
                raise HTTPException(
                    status_code=500, detail=ErrorMessage.UNKNOWN_ERROR.error_response
                ) from http_error

        specification_name: str = get_specification_name(service)

        specification_version: str = (
            service.serviceSpecification.version
            if service.serviceSpecification.version
            else get_specification_version(specification_name)
        )

        try:
            return self.get_service_specification_by_name_version_pair(
                specification_name,
                specification_version,
            )
        except httpx.HTTPError as http_error:
            logger.log(
                Messages.ERROR_FETCHING_SPEC,
                specification_name=specification_name,
                specification_version=specification_version,
                exc_info=True,
            )
            raise HTTPException(
                status_code=500, detail=ErrorMessage.UNKNOWN_ERROR.error_response
            ) from http_error

    def get_spec_chars_name_to_value_type(
        self,
        spec_id: str,
    ) -> dict[str, str | None]:
        """
        Call Service Catalog and then generate a dictionaary from the specification
        Returns:
            dict[str, str | None]: characteristic name: characteristic valueType
        """
        try:
            return {
                spec_char.name: spec_char.valueType
                for spec_char in self.get_service_specification_by_id(
                    spec_id
                ).specCharacteristic
                or []
            }
        except httpx.HTTPError:
            logger.log(Messages.ERROR_RETRIEVING_SPECIFICATION)
            return {}

    def get_catalog_href(self, request: Request, spec_id: str) -> str:
        """Generates catalog href for specification"""
        return get_catalog_href(request, spec_id, self.tmf_services)


class ServiceCatalogConnectorStub:
    """
    Service Catalog Connector Stub
    """

    def __init__(self, tmf_services):
        self.tmf_services: ConfigTMFServices = tmf_services
        self.available_schemas_by_id: dict[str, ServiceSchemaCreate] = {
            schema.schema_id: schema for schema in AVAILABLE_SCHEMAS
        }
        self.available_specs_by_id: dict[str, ServiceSpecification] = {
            generate_specification_id(specification.name): ServiceSpecification(
                id=generate_specification_id(specification.name),
                **specification.dict(),
            )
            for specification in AVAILABLE_SPECIFICATIONS
        }
        self.available_specs_by_name_and_version: dict[
            tuple[str, str], ServiceSpecification
        ] = {
            (specification.name, specification.version): ServiceSpecification(
                id=generate_specification_id(specification.name),
                **specification.dict(),
            )
            for specification in AVAILABLE_SPECIFICATIONS
        }

    def get_schema_by_id(self, schema_id) -> ServiceSchemaCreate | None:
        """
        Get schema by schema id from memory
        """
        return self.available_schemas_by_id.get(schema_id)

    def get_service_specification_by_id(self, id_: str) -> ServiceSpecification | None:
        """
        Get Service Specification from memory
        """
        return self.available_specs_by_id.get(id_)

    def get_service_specification_by_name_version_pair(
        self, name: str, version: str
    ) -> ServiceSpecification | None:
        """
        Get Service Specification from memory by name and version
        """
        return self.available_specs_by_name_and_version.get((name, version))

    def get_service_specification(self, service: Service) -> ServiceSpecification:
        """
        Get service specification data from Catalog API by id if the
        service specification id is present, otherwise it will use the
        specification name and version as arguments to get it.
        example: Get from AVAILABLE_SPECIFICATIONS the swVc version 3.0 specification.
        """
        error_details: dict = {
            "code": "1",
            "status": 500,
            "reason": "Server Error",
            "message": "Failed to retrieve service specification",
        }
        if service.serviceSpecification.id:
            service_spec = self.get_service_specification_by_id(
                service.serviceSpecification.id
            )
            if service_spec is None:
                logger.log(
                    Messages.ERROR_FETCHING_SPEC,
                    id=service.serviceSpecification.id,
                    name=service.serviceSpecification.name,
                    version=service.serviceSpecification.version,
                )
                raise HTTPException(
                    status_code=500, detail=json.dumps(obj=error_details, indent=4)
                )
            return service_spec

        specification_name: str = get_specification_name(service)

        specification_version: str = (
            service.serviceSpecification.version
            if service.serviceSpecification.version
            else get_specification_version(specification_name)
        )
        service_spec = self.get_service_specification_by_name_version_pair(
            specification_name, specification_version
        )
        if service_spec is None:
            logger.log(
                Messages.ERROR_FETCHING_SPEC,
                specification_name=specification_name,
                specification_version=specification_version,
            )
            raise HTTPException(status_code=500, detail=json.dumps(obj=error_details))
        return service_spec

    def get_spec_chars_name_to_value_type(
        self,
        spec_id: str,
    ) -> dict[str, str | None]:
        """
        Call Service Catalog and then generate a dictionary from the specification
        Returns:
            dict[str, str | None]: characteristic name: characteristic valueType
        """
        specification = self.get_service_specification_by_id(spec_id)
        if specification is None:
            logger.log(Messages.ERROR_RETRIEVING_SPECIFICATION)
            return {}

        return {
            spec_char.name: spec_char.valueType
            for spec_char in specification.specCharacteristic or []
        }

    def get_catalog_href(self, request: Request, spec_id: str) -> str:
        """Generates catalog href for specification"""
        return get_catalog_href(request, spec_id, self.tmf_services)


def is_specification_name_valid(specification_name: str | None) -> bool:
    """
    Check if the given specification name is present
    in one of the serviceType Enums
    """
    return any(
        specification_name in service_type.__members__.values()
        for service_type in [
            VelocloudServiceType,
            MerakiServiceType,
            MistServiceType,
            FortiManagerServiceType,
        ]
    )


def get_specification_name(service: Service) -> str:
    """
    Get service specification name.
    If it is not defined in the specification section it will be take by
    the servicetype, assuming it is not None
    """
    specification_name = (
        service.serviceSpecification.name
        if service.serviceSpecification.name is not None
        else service.serviceType
    )

    if specification_name is None or not is_specification_name_valid(
        specification_name
    ):
        details: dict = {
            "code": "1",
            "status": 422,
            "reason": "Unprocessable Entity",
            "message": "Not Valid Service Specification Information",
        }

        logger.log(Messages.MISSING_SPECIFICATION_INFORMATION, service=service)
        raise HTTPException(
            status_code=400,
            detail=json.dumps(details, indent=4),
        )

    if service.serviceType != specification_name:
        logger.log(
            Messages.SERVICE_TYPE_MODIFICATION,
            service_type=service.serviceType,
            requested_name=specification_name,
        )

        service.serviceType = parse_obj_as(
            VelocloudServiceType
            | MerakiServiceType
            | MistServiceType
            | FortiManagerServiceType
            | None,
            specification_name,
        )

    return specification_name


def get_specification_version(specification_name: str) -> str:
    """
    Get service specification version if it is not defined
    in the specification section by using the default specification version
    by checking its type
    """
    if specification_name in VelocloudServiceType.__members__.values():
        return velocloud_specification_version

    if specification_name in MerakiServiceType.__members__.values():
        return meraki_specification_version

    if specification_name in MistServiceType.__members__.values():
        return mist_specification_version

    if specification_name in FortiManagerServiceType.__members__.values():
        return fortimanager_specification_version

    details: dict = {
        "code": "1",
        "status": 422,
        "reason": "Unprocessable Entity",
        "message": "Not Valid Service Specification Version Found",
    }

    logger.log(Messages.SPEC_NOT_FOUND, specification=specification_name)
    raise HTTPException(status_code=400, detail=json.dumps(details, indent=4))


def get_catalog_href(
    request: Request, spec_id: str, tmf_services: ConfigTMFServices
) -> str:
    """
    This method generates the service specification href
    TODO use config flag to determine whether to use the request host or config
    """
    catalog_url = (
        make_host_url(request) + "/serviceCatalogManagement/v4"
        if tmf_services.href_use_request_host
        else str(tmf_services.service_catalog)
    )
    return catalog_url + "/serviceSpecification/" + spec_id


def generate_specification_id(spec_name: str) -> str:
    """
    Function to create a specification id based on spec name
    Mainly used for AVAILABLE_SPECIFICATIONS
    """
    return f"{spec_name}-specification-id".replace(" ", "")
