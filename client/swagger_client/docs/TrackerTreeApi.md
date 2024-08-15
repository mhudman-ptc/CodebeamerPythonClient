# swagger_client.TrackerTreeApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tracker_tree**](TrackerTreeApi.md#list_tracker_tree) | **GET** /v3/trackers/tree | List tracker tree
[**update_tracker_tree**](TrackerTreeApi.md#update_tracker_tree) | **POST** /v3/trackers/tree/update | Update tracker tree

# **list_tracker_tree**
> list[TrackerTree] list_tracker_tree(project_id, working_set_id=working_set_id, revision=revision)

List tracker tree

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
api_instance = swagger_client.TrackerTreeApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | 
working_set_id = 56 # int |  (optional)
revision = 56 # int |  (optional)

try:
    # List tracker tree
    api_response = api_instance.list_tracker_tree(project_id, working_set_id=working_set_id, revision=revision)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerTreeApi->list_tracker_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **working_set_id** | **int**|  | [optional] 
 **revision** | **int**|  | [optional] 

### Return type

[**list[TrackerTree]**](TrackerTree.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_tree**
> JsonView update_tracker_tree(body, project_id, working_set_id=working_set_id)

Update tracker tree

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
api_instance = swagger_client.TrackerTreeApi(swagger_client.ApiClient(configuration))
body = [swagger_client.TrackerTree()] # list[TrackerTree] | 
project_id = 56 # int | 
working_set_id = 56 # int |  (optional)

try:
    # Update tracker tree
    api_response = api_instance.update_tracker_tree(body, project_id, working_set_id=working_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerTreeApi->update_tracker_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[TrackerTree]**](TrackerTree.md)|  | 
 **project_id** | **int**|  | 
 **working_set_id** | **int**|  | [optional] 

### Return type

[**JsonView**](JsonView.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

