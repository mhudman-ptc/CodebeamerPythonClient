# openapi_client.TrackerItemMoveApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_move_field_mapping**](TrackerItemMoveApi.md#get_item_move_field_mapping) | **GET** /v3/items/move/field-mapping | Gets the default field mapping between two trackers
[**move_tracker_items**](TrackerItemMoveApi.md#move_tracker_items) | **POST** /v3/items/move | Move Tracker Items from the Source Tracker to the Target Tracker


# **get_item_move_field_mapping**
> TrackerItemFieldMappingInfo get_item_move_field_mapping(source_tracker_id, target_tracker_id)

Gets the default field mapping between two trackers

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_field_mapping_info import TrackerItemFieldMappingInfo
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
    api_instance = openapi_client.TrackerItemMoveApi(api_client)
    source_tracker_id = 56 # int | The id of the source Tracker
    target_tracker_id = 56 # int | The id of the target Tracker

    try:
        # Gets the default field mapping between two trackers
        api_response = api_instance.get_item_move_field_mapping(source_tracker_id, target_tracker_id)
        print("The response of TrackerItemMoveApi->get_item_move_field_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemMoveApi->get_item_move_field_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_tracker_id** | **int**| The id of the source Tracker | 
 **target_tracker_id** | **int**| The id of the target Tracker | 

### Return type

[**TrackerItemFieldMappingInfo**](TrackerItemFieldMappingInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The field mapping |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_tracker_items**
> JobReference move_tracker_items(tracker_item_move_request)

Move Tracker Items from the Source Tracker to the Target Tracker

Move Tracker Items from the Source Tracker to the Target Tracker. The items are optional, if it is not provided all the Tracker Items will be moved from the Source Tracker. All the fields from the Source Tracker must be in the mapping. If you want to ignore one you set the targetField to null in the request.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.job_reference import JobReference
from openapi_client.models.tracker_item_move_request import TrackerItemMoveRequest
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
    api_instance = openapi_client.TrackerItemMoveApi(api_client)
    tracker_item_move_request = openapi_client.TrackerItemMoveRequest() # TrackerItemMoveRequest | 

    try:
        # Move Tracker Items from the Source Tracker to the Target Tracker
        api_response = api_instance.move_tracker_items(tracker_item_move_request)
        print("The response of TrackerItemMoveApi->move_tracker_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemMoveApi->move_tracker_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_item_move_request** | [**TrackerItemMoveRequest**](TrackerItemMoveRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Background job information that is started to move the Tracker Items. |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

