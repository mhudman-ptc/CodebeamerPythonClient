# swagger_client.WorkingSetPermissionApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_working_set_permission**](WorkingSetPermissionApi.md#update_working_set_permission) | **POST** /v3/workingset/{workingSetId}/permission | Set the trackers permissions for specific roles in the given workingset

# **update_working_set_permission**
> update_working_set_permission(body, working_set_id)

Set the trackers permissions for specific roles in the given workingset

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
api_instance = swagger_client.WorkingSetPermissionApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkingSetPermissionRequest() # WorkingSetPermissionRequest | 
working_set_id = 56 # int | 

try:
    # Set the trackers permissions for specific roles in the given workingset
    api_instance.update_working_set_permission(body, working_set_id)
except ApiException as e:
    print("Exception when calling WorkingSetPermissionApi->update_working_set_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkingSetPermissionRequest**](WorkingSetPermissionRequest.md)|  | 
 **working_set_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

