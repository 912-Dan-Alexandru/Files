# Service Inventory refactor documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Starting the Service Inventory](#starting-the-service-inventory)
   - [Startup Process](#startup-process)
   - [Configuration and Initialization](#configuration-and-initialization)
3. [Service Inventory Dependencies](#service-inventory-dependencies)
4. [Service Inventory Routers](#service-inventory-routers)
   - [System Router](#system-router)
   - [Enrichment Router](#enrichment-router)
   - [Service Router](#service-router)
     - [GET Endpoint](#get-endpoint)
     - [Creation Endpoint](#creation-endpoint)
     - [Deletion Endpoint](#deletion-endpoint)
5. [Usage of the Common Module](#usage-of-the-common-module)
6. [Neo4j Refactoring](#neo4j-refactoring)
   - [Generalization of the GraphDB Class](#generalization-of-the-graphdb-class)
   - [Centralization of Queries](#centralization-of-queries)
   - [Query Optimization](#query-optimization)
7. [Service Formatter and Builder](#service-formatter-and-builder)
   - [Current Service Formatter](#current-service-formatter)
   - [Builder Implementation](#builder-implementation)
   - [Handling Related Parties](#handling-related-parties)
   - [Migrate the Builders to the Harlock Library](#migrate-the-builders-to-the-harlock-libraries)
     - [Usage example](#usage-example-builders)
8. [Module Connectors](#module-connectors)
   - [Service Catalog Connector](#service-catalog-connector)
   - [Service Inventory Connector](#service-inventory-connector)
   - [Refactoring Connectors and Models into the Harlock Library](#refactoring-connectors-and-models-into-the-harlock-library)
     - [Separate the connectors from the common module](#separate-the-connectors-from-the-common-module)
     - [Models Consolidation](#models-consolidation)
     - [Usage example](#usage-example-builders)
9. [Import Problems](#import-problems)
    - [Import Analysis](#import-analysis)
    - [Problematic Imports](#problematic-imports)
    - [Refactoring Strategies](#refactoring-strategies)
10. [Final Considerations](#final-considerations)
11. [Interaction with Other Modules](#interaction-with-other-modules)
    - [Workflow Server](#workflow-server)
    - [Inventory Agent](#inventory-agent)

## Introduction

The Service Inventory is a crucial module within the system, responsible for managing and interacting with the Neo4j database for the creation, modification, and management of services. It is the only module that has direct access to Neo4j, using a wide range of queries developed over time to effectively manage services and their associated content.

## Starting the Service Inventory

### Startup Process

The Service Inventory is started using the FastAPI library. The startup process is defined in the main file `service_inventory/main.py`, where the following operations are performed:

1. Creation of the FastAPI instance
2. Definition of the entire Service Inventory application
3. Configuration of exception handling (using functions from the `common` module)
4. Assignment of a specific function for the application lifecycle

### Configuration and Initialization

The application lifecycle function performs several critical operations:

1. Sentry configuration (using a function from the `common` module)
2. Definition of the Service Catalog connector
3. Definition of the Neo4j connection
4. Definition of the message producer
5. Neo4j indexing

It's important to note that most of these operations are handled by the `common` module, with the exception of Neo4j indexing and the initialization of the Service Catalog connector.

Potential improvements:
- Move Neo4j indexing to the `common` module
- Generalize the function for the Service Catalog connector in the `common` module, allowing greater flexibility in using cache or stub

## Service Inventory Dependencies

The Service Inventory has several critical dependencies:

1. GraphDB Database (currently Neo4j): Used for storing and managing service data
2. Message Bus (Kafka): Used for asynchronous communication between various system components
3. Service Catalog: Provides service specifications

Important note: Currently, there is no explicit check to verify if the Service Catalog is running. The responsibility for this check falls on other modules, which verify the status of the Catalog and Inventory before making calls to the Service Inventory. Therefore, the service inventory can be executed even without the service catalog running.

## Service Inventory Routers

The Service Inventory uses three main routers to handle different functionalities:

### System Router

- Origin: Comes from the `common` module
- Functionality: Exposes a simple API that responds with a 200 code if the system is operational
- Usage: Used to verify the operational status of the Service Inventory

### Enrichment Router

- Functionality: Exposes APIs to receive detailed information about Velocloud vendor services
- Features:
  - Allows filtering based on specific characteristics of Velocloud services
  - Directly accesses Neo4j, declaring and executing queries from the Service Inventory
- Area for improvement: Consider creating more dynamic queries to increase flexibility and reusability. In this router, logic is performed on service characteristics, so it's possible to create a dynamic query based on the characteristics and keys passed.

### Service Router

This is the most critical and complex router of the Service Inventory.

Main functionalities:
- Exposes APIs for creating, modifying, retrieving, and deleting Harlock services
- Correctly uses the TMF standard for headers and query params

#### GET Endpoint

Current implementation:
- Supports the `fields` parameter to filter the service fields to return
- Filtering is performed after retrieving data from Neo4j

Proposed improvement:
- Modify the logic to pass the `fields` parameter directly to the Neo4j query, thus optimizing data retrieval

#### Creation Endpoint

Current functionality:
- Uses "Service Formatters" to format services and add them to Neo4j
- Most services use a common Service Formatter

Future goals:
- Standardize the use of a single Service Formatter for all types of services
- Implement the use of the "Builder" (present in the `common` module) for all types of services
- The Builder currently doesn't handle Related Parties, but this functionality can be added

#### Deletion Endpoint

Current situation:
- Uses different functions based on the type of service to be deleted

Proposed improvement:
- Create a single query capable of:
  1. Deleting the specified service
  2. Removing all unused associated nodes
- Alternative: Implement a scheduled task for periodic cleaning of Neo4j nodes without relationships and unused

## Usage of the Common Module

The Service Inventory makes extensive use of the `common` module for several critical functionalities:

1. Sentry configuration: Leverages a centralized function for monitoring configuration
2. Neo4j connection definition: Uses the `GraphDB` class defined in `common`
3. TMF standard implementation: Utilizes predefined functions and classes to adhere to the standard
4. FastAPI library usage: Uses wrappers and utilities defined in `common` for FastAPI integration
5. General use of common functions

## Neo4j Refactoring

Although Neo4j is currently used exclusively by the Service Inventory, there are several areas that could benefit from refactoring:

### Generalization of the GraphDB Class

Objective: Make the `GraphDB` class more flexible to potentially support other types of GraphQL databases in the future.

Proposed implementation:
```python
from abc import ABC, abstractmethod

class AbstractGraphDB(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str, params: dict):
        pass

class Neo4jGraphDB(AbstractGraphDB):
    def connect(self):
        # Neo4j-specific implementation
        pass

    def execute_query(self, query: str, params: dict):
        # Neo4j-specific query execution
        pass
```

### Centralization of Queries

- Move all Neo4j-related queries and functions to the `common` module
- Organize queries in separate files based on their functionality (e.g., services, related parties, etc.)

### Query Optimization

- Refactor existing queries to make them more dynamic and reusable
- Create parametric queries to reduce code duplication

## Service Formatter and Builder

### Current Service Formatter

- Used to format services before insertion into Neo4j
- Different formatters for different types of services

### Builder Implementation

Objective: Use the Builder (present in the `common` module) for all types of services.

Advantages:
- Standardization of service creation
- Greater flexibility and maintainability of the code

Implementation:
1. Extend the existing Builder to cover all types of services
2. Gradually migrate from Service Formatter to Builder

### Handling Related Parties

Current situation:
- Related Parties are managed separately from the Builder

Proposed improvement:
- Extend the Builder to include Related Parties management
- Centralize Related Parties queries in the `common` module for each available GraphDB

### Migrate the Builders to the harlock libraries
The Harlock library is a comprehensive solution for building and managing various service instances across multiple vendors. By migrating the builder functionality into a separate library, we achieve several benefits:

1. **Improved Modularity**: Separating the builder logic allows for easier maintenance and updates.
2. **Enhanced Reusability**: The core builder functionality can be shared across different projects and services.
3. **Standardization**: Provides a consistent approach to building services across different vendors and service types.
4. **Easier Testing**: Isolated components are easier to unit test.
5. **Flexibility**: Allows for easy addition of new vendors, services, or service types.
6. **Scalability**: The structure supports multiple services per vendor, allowing for growth and expansion.

**Directory Structure**

```
harlock/
│
├── builders/
│   ├── __init__.py
│   ├── base_builder.py
│   └── specific_builders/
│       ├── __init__.py
│       ├── vendor1/
│       │   ├── __init__.py
│       │   ├── service1/
│       │   │   ├── __init__.py
│       │   │   ├── service_builder.py
│       │   │   ├── service_characteristics_builder.py
│       │   │   └── update_request_builder.py
│       │   ├── service2/
│       │   │   ├── __init__.py
│       │   │   ├── service_builder.py
│       │   │   ├── service_characteristics_builder.py
│       │   │   └── update_request_builder.py
│       │   └── ...  # Other services for vendor1
│       ├── vendor2/
│       │   ├── __init__.py
│       │   ├── serviceA/
│       │   │   ├── __init__.py
│       │   │   ├── service_builder.py
│       │   │   ├── service_characteristics_builder.py
│       │   │   └── update_request_builder.py
│       │   └── ...  # Other services for vendor2
│       └── ...  # Other vendors
```


**Base Builders (`harlock/builders/base_builder.py`)**

[Content remains the same as in the previous version]

**Vendor Builders**

Each vendor can have multiple services, each with its own set of builders. Here's an example for Vendor1's Service1:

**Vendor1Service1CharacteristicsBuilder (`harlock/builders/specific_builders/vendor1/service1/service_characteristics_builder.py`)**

Extends `ServiceCharacteristicInstanceBuilder` for Vendor1's Service1-specific logic.

```python
class Vendor1Service1CharacteristicsBuilder(ServiceCharacteristicInstanceBuilder):
    def __init__(self, path: list[str]) -> None:
        super().__init__(
            service_specification=vendor1_service1_spec,
            key_characteristics={"path": path},
        )

    def parse_value(self, data, characteristic_specification):
        value = ParsingResult()
        # Vendor1's Service1-specific parsing logic...
        return value
```

**Vendor1Service1Builder (`harlock/builders/specific_builders/vendor1/service1/service_builder.py`)**

Extends `ServiceInstanceBuilder` for Vendor1's Service1-specific service building.

```python
class Vendor1Service1Builder(ServiceInstanceBuilder):
    def __init__(self, catalog_specification_id, service_inventory_url, 
                 service_id, service_name):
        spec = ServiceSpecification(id=catalog_specification_id, **vendor1_service1_spec.dict())
        super().__init__(
            spec,
            Vendor1ServiceType.SERVICE1,
            Vendor1Service1CharacteristicsBuilder(),
            service_inventory_url,
            service_id,
            service_name,
        )
```

**Vendor1Service1UpdateRequestBuilder (`harlock/builders/specific_builders/vendor1/service1/update_request_builder.py`)**

Builds update requests for Vendor1's Service1.

```python
class Vendor1Service1UpdateRequestBuilder:
    def build(self, characteristic_instances):
        update_request = {"settings": {}}
        for instance in characteristic_instances:
            # Vendor1's Service1-specific mapping logic...
            pass
        return Vendor1Service1Model(**update_request)
```

#### Usage Example (Builders)

This example demonstrates how to use the Harlock library to build and update Vendor1's Service1:

```python
from harlock.builders.specific_builders.vendor1.service1.service_builder import Vendor1Service1Builder
from harlock.builders.specific_builders.vendor1.service1.update_request_builder import Vendor1Service1UpdateRequestBuilder

# Create service builder
service_builder = Vendor1Service1Builder(
    catalog_specification_id="vendor1_service1_spec",
    service_inventory_url="http://example.com/inventory",
    service_id="service_123",
    service_name="Vendor1 Service1",
)

# Build service
input_data = {...}  # Vendor1's Service1-specific data
service = service_builder.build(input_data)

# Create update request builder
update_builder = Vendor1Service1UpdateRequestBuilder()

# Build update request
characteristic_instances = [...]  # List of characteristic instances
update_request = update_builder.build(characteristic_instances)
```

**Extending for New Vendors and Services**

To add support for a new vendor or service:

1. Create a new directory under `harlock/builders/specific_builders/` for the vendor if it doesn't exist.
2. Create a new directory for the service under the vendor directory.
3. Implement service-specific builders extending the base classes.
4. Ensure all necessary methods are overridden to handle service-specific logic.

This structure allows for easy addition of new vendors and services while maintaining a consistent interface and reusing core functionality.

## Module Connectors

### Service Catalog Connector

Current status:
- Used only by the Service Inventory
- Supports the use of cache or stub

Future goal:
- Add support for the `/system/liveness` endpoint in the connector
- Extend the use of the connector to all modules that interface with the Service Catalog

### Service Inventory Connector

Current status:
- Defined but not used by any module

Objectives:
1. Implement the use of the connector in all modules that interact with the Service Inventory (e.g., Workflow Server and Inventory Agent)
2. Add support for the `/system/liveness` endpoint in the connector
3. Review and finalize the connector to ensure it covers all use cases

### Refactoring Connectors and Models into the Harlock Library

#### Separate the connectors from the common module

To improve the organization and maintainability of the project, it is beneficial to separate the connectors from the common module and convert them into a single library that encapsulates all types of connectors. This library will initially include the `Service Catalog Connector` and the `Service Inventory Connector`.

**Library Name**: Harlock

**Steps to Convert Connectors into a Library**:

1. **Create the Library Structure**:
   - Organize the library into a logical directory structure.

   ```plaintext
   harlock/
   ├── __init__.py
   ├── connectors/
   │   ├── __init__.py
   │   ├── service_catalog/
   │   │   ├── __init__.py
   │   │   ├── connector.py
   │   │   └── messages.py
   │   ├── service_inventory/
   │   │   ├── __init__.py
   │   │   ├── connector.py
   │   │   └── messages.py
   ├── models/
   │   ├── __init__.py
   │   ├── catalog_models.py
   │   ├── inventory_models.py
   │   └── common_models.py
   └── utils/
       ├── __init__.py
       └── helpers.py
   ```

2. **Refactor the Connectors**:
   - Move the existing code for each connector into the appropriate module within the library.
   - Ensure all imports are updated to reflect the new library structure.

   Example refactored code for `Service Catalog Connector`:

   ```python
   # harlock/connectors/service_catalog/connector.py

   from abc import ABC, abstractmethod
   from typing import Optional, Dict
   import httpx
   from harlock.models.catalog_models import ServiceSchemaCreate, ServiceSpecification

   class ServiceCatalogConnector(ABC):
       @abstractmethod
       def get_schema_by_id(self, schema_id: str) -> Optional[ServiceSchemaCreate]:
           pass

       @abstractmethod
       def get_service_specification_by_id(self, spec_id: str) -> Optional[ServiceSpecification]:
           pass

   class ServiceCatalogConnectorHttp(ServiceCatalogConnector):
       def __init__(self, base_url: str):
           self.client = httpx.Client(base_url=base_url)

       def get_schema_by_id(self, schema_id: str) -> Optional[ServiceSchemaCreate]:
           response = self.client.get(f"/serviceSchema/{schema_id}")
           response.raise_for_status()
           return ServiceSchemaCreate.parse_obj(response.json())

       def get_service_specification_by_id(self, spec_id: str) -> Optional[ServiceSpecification]:
           response = self.client.get(f"/serviceSpecification/{spec_id}")
           response.raise_for_status()
           return ServiceSpecification.parse_obj(response.json())

   class CachingServiceCatalogConnector(ServiceCatalogConnector):
    def __init__(self, base_url: str, cache_type: Literal["in_memory", "redis", "file"]):
        self.client = httpx.Client(base_url=base_url)
        if cache_type == "in_memory":
            self.cache = {}
        elif cache_type == "redis":
            self.cache = redis.Redis(host='localhost', port=6379, db=0)
        elif cache_type == "file":
            self.cache = DiskCache(os.path.join(os.getcwd(), 'disk_cache'))
        else:
            raise ValueError("Invalid cache type")

    def get_schema_by_id(self, schema_id: str) -> Optional[ServiceSchemaCreate]:
        if self.cache.get(schema_id):
            schema_data = self.cache.get(schema_id)
            return ServiceSchemaCreate.parse_obj(json.loads(schema_data) if isinstance(schema_data, str) else schema_data)
        response = self.client.get(f"/serviceSchema/{schema_id}")
        response.raise_for_status()
        schema = ServiceSchemaCreate.parse_obj(response.json())
        self.cache.set(schema_id, json.dumps(schema.dict()) if isinstance(self.cache, dict) else schema.dict())
        return schema

    def get_service_specification_by_id(self, spec_id: str) -> Optional[ServiceSpecification]:
        if self.cache.get(spec_id):
            spec_data = self.cache.get(spec_id)
            return ServiceSpecification.parse_obj(json.loads(spec_data) if isinstance(spec_data, str) else spec_data)
        response = self.client.get(f"/serviceSpecification/{spec_id}")
        response.raise_for_status()
        spec = ServiceSpecification.parse_obj(response.json())
        self.cache.set(spec_id, json.dumps(spec.dict()) if isinstance(self.cache, dict) else spec.dict())
        return spec
   ```

   Example refactored code for `Service Inventory Connector`:

   ```python
   # harlock/connectors/service_inventory/connector.py

   from abc import ABC, abstractmethod
   from typing import Optional
   import httpx
   from harlock.models.inventory_models import Service

   class ServiceInventoryConnector(ABC):
       @abstractmethod
       def get_service(self, service_id: str) -> Optional[Service]:
           pass

       @abstractmethod
       def delete_service(self, service_id: str) -> None:
           pass

   class ServiceInventoryHttp(ServiceInventoryConnector):
       def __init__(self, base_url: str):
           self.client = httpx.Client(base_url=base_url)

       def get_service(self, service_id: str) -> Optional[Service]:
           response = self.client.get(f"/service/{service_id}")
           response.raise_for_status()
           return Service.parse_obj(response.json())

       def delete_service(self, service_id: str) -> None:
           response = self.client.delete(f"/service/{service_id}")
           response.raise_for_status()
   ```

3. **Update Imports in Other Parts of the Project**:
   - Ensure that all other parts of the project that use these connectors are updated to import from the new `harlock` library.

   ```python
   # Example of updated import in another part of the project

   from harlock.connectors.service_catalog.connector import ServiceCatalogConnectorHttp
   ```

4. **Package the Library**:
   - Create a `setup.py` file to package the `harlock` library.

   ```python
   # setup.py

   from setuptools import setup, find_packages

   setup(
       name='harlock',
       version='0.1.0',
       packages=find_packages(),
       install_requires=[
           'httpx',
           'pydantic',
       ],
   )
   ```

5. **Install and Use the Library**:
   - Install the `harlock` library in your project environment.
   - Use the connectors as needed in your project.

#### Models Consolidation

To improve consistency and maintainability, it is beneficial to consolidate all models related to Harlock into the Harlock library. This allows for consistent imports across the project and ensures that all parts of the project are using the same definitions.

**Models Structure**:

```plaintext
harlock/
├── models/
│   ├── __init__.py
│   ├── catalog_models.py
│   ├── inventory_models.py
│   └── common_models.py
```

**Example Model Files**:

**File**: `harlock/models/catalog_models.py`

```python
from pydantic import BaseModel

class ServiceSchemaCreate(BaseModel):
    # Define your schema fields here
    pass

class ServiceSpecification(BaseModel):
    # Define your specification fields here
    pass
```

**File**: `harlock/models/inventory_models.py`

```python
from pydantic import BaseModel

class Service(BaseModel):
    # Define your service fields here
    pass
```

#### Usage Examples (Connectors)

Here are some examples of how to use the refactored connectors and models in your project.

**Usage Example**:

```python
from harlock.connectors.service_catalog.connector import (
    ServiceCatalogConnectorHttp,
    CachingServiceCatalogConnector
)
from harlock.connectors.service_inventory.connector import ServiceInventoryHttp
from harlock.models.catalog_models import ServiceSchemaCreate, ServiceSpecification
from harlock.models.inventory_models import Service

def main():
    service_catalog_url = "http://localhost:4321/"
    service_inventory_url = "http://localhost:1234/"

    # Initialize base HTTP connector for Service Catalog
    base_catalog_connector = ServiceCatalogConnectorHttp(base_url=service_catalog_url)

    # Initialize caching connector for Service Catalog
    cache_type = "redis"  # Options: "in_memory", "redis", "file"
    caching_catalog_connector = CachingServiceCatalogConnector(base_url=service_catalog_url, cache_type=cache_type)

    # Example: Using the base HTTP connector
    schema_id = "12345"
    try:
        schema = base_catalog_connector.get_schema_by_id(schema_id)
        print(f"Fetched schema via HTTP: {schema}")
    except httpx.HTTPError as e:
        print(f"Error fetching schema via HTTP: {e}")

    # Example: Using the caching connector
    try:
        schema = caching_catalog_connector.get_schema_by_id(schema_id)
        print(f"Fetched schema via Cache: {schema}")
    except httpx.HTTPError as e:
        print(f"Error fetching schema via Cache: {e}")

    # Initialize inventory connector
    inventory_connector = ServiceInventoryHttp(base_url=service_inventory_url)

    # Fetch a service by ID from the Service Inventory
    service_id = "abcde"
    try:
        service = inventory_connector.get_service(service_id)
        print(f"Fetched service: {service}")
    except httpx.HTTPError as e:
        print(f"Error fetching service: {e}")

    # Delete a service by ID from the Service Inventory
    try:
        inventory_connector.delete_service(service_id)
        print(f"Deleted service with ID: {service_id}")
    except httpx.HTTPError as e:
        print(f"Error deleting service: {e}")

if __name__ == "__main__":
    main()
```

By following these steps, you can effectively separate the connectors from the common module and package them into a single library, `harlock`, which can be easily maintained and reused across your project. Additionally, consolidating all models into the Harlock library ensures consistency and maintainability throughout the project.

## Import Problems

### Import Analysis

An in-depth analysis of imports between the following modules has been conducted:
- Service Catalog
- Workflow Server
- Service Ordering
- Service Inventory
- Inventory Agent
- Common

### Problematic Imports

The following potentially problematic import files have been identified:

1. Modules importing from other modules:
   - `imports_of_service_ordering_in_workflow_server.txt`
   - `imports_of_inventory_agent_in_workflow_server.txt`
   - `imports_of_inventory_agent_in_service_inventory.txt`

2. Common importing from other modules:
   - `imports_of_service_inventory_in_common.txt`
   - `imports_of_service_catalog_in_common.txt`

### Refactoring Strategies

Questions to consider:
1. Can modules import from modules other than the "Common" module?
2. Can the Common module import from other modules?

Necessary actions:
1. Analyze each problematic import and determine if it's necessary
2. For necessary imports, evaluate if the functionality can be moved to the `common` module
3. For unnecessary imports, remove them and refactor the code accordingly
4. Consider creating interfaces or abstract classes in the `common` module to reduce direct dependencies between modules

## Final Considerations

1. Use of TMF standard: The Service Inventory correctly implements the TMF standard for headers and query params.

2. Integration with FastAPI: The use of the FastAPI library is well implemented and leverages the functionalities offered by the `common` module.

3. Extensive use of the Common module: The Service Inventory makes extensive use of the functionalities offered by the `common` module.

4. Service Inventory Connector: An interface for the connector exists in the `common` module, but it's not currently used. The implementation and adoption of this connector should be a priority.

5. Areas for improvement:
   - Neo4j management: Centralization and optimization of queries
   - Use of connectors: Complete implementation and adoption in all relevant modules
   - Import structure: Resolution of circular and unnecessary dependency problems
   - Service Formatter and Builder: Standardization and extension to cover all types of services

6. Main objectives:
   - Increase the modularity of the Service Inventory
   - Improve the efficiency of operations, particularly those involving Neo4j or any GraphDB
   - Facilitate code maintenance through better organization and standardization
   - Optimize interaction with other system modules, particularly through the use of standardized connectors

7. Possible refactor:
   - Migrate everything related to Harlock to a specific Harlock library.

## Interaction with Other Modules

### Workflow Server

The Workflow Server frequently interacts with the Service Inventory. However, it's necessary to standardize all calls to the Service Inventory through the dedicated connector.

### Inventory Agent

The Inventory Agent is another module that closely interacts with the Service Inventory. However, it's necessary to use the Service Inventory connector for all interactions.