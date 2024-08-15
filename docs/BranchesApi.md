# swagger_client.BranchesApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tracker_item_on_branch**](BranchesApi.md#get_tracker_item_on_branch) | **GET** /v3/branches/{branchId}/item | Get tracker item on branch

# **get_tracker_item_on_branch**
> TrackerItem get_tracker_item_on_branch(source_item_id, branch_id)

Get tracker item on branch

API can be used for finding a tracker item by a branch id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.BranchesApi(swagger_client.ApiClient(configuration))
source_item_id = 56 # int | 
branch_id = 56 # int | 

try:
    # Get tracker item on branch
    api_response = api_instance.get_tracker_item_on_branch(source_item_id, branch_id)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

