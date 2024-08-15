# openapi_client.BranchesApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tracker_item_on_branch**](BranchesApi.md#get_tracker_item_on_branch) | **GET** /v3/branches/{branchId}/item | Get tracker item on branch


# **get_tracker_item_on_branch**
> TrackerItem get_tracker_item_on_branch(source_item_id, branch_id)

Get tracker item on branch

API can be used for finding a tracker item by a branch id

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item import TrackerItem
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
    api_instance = openapi_client.BranchesApi(api_client)
    source_item_id = 56 # int | 
    branch_id = 56 # int | 

    try:
        # Get tracker item on branch
        api_response = api_instance.get_tracker_item_on_branch(source_item_id, branch_id)
        print("The response of BranchesApi->get_tracker_item_on_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BranchesApi->get_tracker_item_on_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_item_id** | **int**|  | 
 **branch_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id and branch id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

