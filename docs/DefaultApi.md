# openapi_client.DefaultApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validere_web_api_tank_controller_create**](DefaultApi.md#validere_web_api_tank_controller_create) | **POST** /api/sites/{site_id}/tanks | Create a new tank on the specified site 
[**validere_web_api_tank_controller_index**](DefaultApi.md#validere_web_api_tank_controller_index) | **GET** /api/tanks | List all tanks visible to the user 


# **validere_web_api_tank_controller_create**
> Tank validere_web_api_tank_controller_create(site_id, tank_request)

Create a new tank on the specified site 

Create a new tank on the specified site 

### Example

* Bearer (JWT) Authentication (Bearer):
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site ID | 
 **tank_request** | [**TankRequest**](TankRequest.md)| Request body to create a Tank | 

### Return type

[**Tank**](Tank.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tank |  -  |
**400** | Bad Request |  -  |
**401** | Not found |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validere_web_api_tank_controller_index**
> list[ElixirValidereWebApiSpecSchemasTank] validere_web_api_tank_controller_index()

List all tanks visible to the user 

List all tanks visible to the user 

### Example

* Bearer (JWT) Authentication (Bearer):
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
    
    try:
        # List all tanks visible to the user 
        api_response = api_instance.validere_web_api_tank_controller_index()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->validere_web_api_tank_controller_index: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ElixirValidereWebApiSpecSchemasTank]**](ElixirValidereWebApiSpecSchemasTank.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tanks |  -  |
**401** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

