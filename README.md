# openapi-client
validere

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.198.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:4000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    site_id = 'site_id_example' # str | Site ID
tank_request = openapi_client.TankRequest() # TankRequest | Request body to create a Tank

    try:
        # Create a new tank on the specified site 
        api_response = api_instance.validere_web_api_tank_controller_create(site_id, tank_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->validere_web_api_tank_controller_create: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**validere_web_api_tank_controller_create**](docs/DefaultApi.md#validere_web_api_tank_controller_create) | **POST** /api/sites/{site_id}/tanks | Create a new tank on the specified site 
*DefaultApi* | [**validere_web_api_tank_controller_index**](docs/DefaultApi.md#validere_web_api_tank_controller_index) | **GET** /api/tanks | List all tanks visible to the user 


## Documentation For Models

 - [BadRequest](docs/BadRequest.md)
 - [NotFound](docs/NotFound.md)
 - [Tank](docs/Tank.md)
 - [TankRequest](docs/TankRequest.md)
 - [Unauthorized](docs/Unauthorized.md)


## Documentation For Authorization


## Bearer

- **Type**: Bearer authentication (JWT)


## Author



