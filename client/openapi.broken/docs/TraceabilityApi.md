# openapi_client.TraceabilityApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_traceability_initial_item_ids**](TraceabilityApi.md#get_traceability_initial_item_ids) | **POST** /v3/traceability/items | Get initial ids
[**get_traceability_level_item_ids**](TraceabilityApi.md#get_traceability_level_item_ids) | **POST** /v3/traceability/relations | Get traceability level item ids


# **get_traceability_initial_item_ids**
> List[TraceabilityItem] get_traceability_initial_item_ids(traceability_initial_level_filter, page_size=page_size, page_no=page_no)

Get initial ids

Get traceability initial ids!

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.traceability_initial_level_filter import TraceabilityInitialLevelFilter
from openapi_client.models.traceability_item import TraceabilityItem
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nvidiatrial.codebeamer.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nvidiatrial.codebeamer.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TraceabilityApi(api_client)
    traceability_initial_level_filter = openapi_client.TraceabilityInitialLevelFilter() # TraceabilityInitialLevelFilter | 
    page_size = 56 # int | Number of items in a result page. (optional)
    page_no = 56 # int | Index of the result page. (optional)

    try:
        # Get initial ids
        api_response = api_instance.get_traceability_initial_item_ids(traceability_initial_level_filter, page_size=page_size, page_no=page_no)
        print("The response of TraceabilityApi->get_traceability_initial_item_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraceabilityApi->get_traceability_initial_item_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceability_initial_level_filter** | [**TraceabilityInitialLevelFilter**](TraceabilityInitialLevelFilter.md)|  | 
 **page_size** | **int**| Number of items in a result page. | [optional] 
 **page_no** | **int**| Index of the result page. | [optional] 

### Return type

[**List[TraceabilityItem]**](TraceabilityItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker item list |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traceability_level_item_ids**
> TraceabilityResult get_traceability_level_item_ids(traceability_level_filter, items_on_level=items_on_level, items_from_previous_item=items_from_previous_item)

Get traceability level item ids

Get traceability item ids!

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.traceability_level_filter import TraceabilityLevelFilter
from openapi_client.models.traceability_result import TraceabilityResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://nvidiatrial.codebeamer.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://nvidiatrial.codebeamer.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TraceabilityApi(api_client)
    traceability_level_filter = openapi_client.TraceabilityLevelFilter() # TraceabilityLevelFilter | 
    items_on_level = 56 # int | Number of items per level. (optional)
    items_from_previous_item = 56 # int | Number of items per item. (optional)

    try:
        # Get traceability level item ids
        api_response = api_instance.get_traceability_level_item_ids(traceability_level_filter, items_on_level=items_on_level, items_from_previous_item=items_from_previous_item)
        print("The response of TraceabilityApi->get_traceability_level_item_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TraceabilityApi->get_traceability_level_item_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **traceability_level_filter** | [**TraceabilityLevelFilter**](TraceabilityLevelFilter.md)|  | 
 **items_on_level** | **int**| Number of items per level. | [optional] 
 **items_from_previous_item** | **int**| Number of items per item. | [optional] 

### Return type

[**TraceabilityResult**](TraceabilityResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Traceability items list |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

