# swagger_client.WorkingSetApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_mapping_in_working_set**](WorkingSetApi.md#get_items_mapping_in_working_set) | **POST** /v3/working-sets/items-mapping | Maps Tracker Items in Working-Set
[**get_tracker_working_sets**](WorkingSetApi.md#get_tracker_working_sets) | **GET** /v3/trackers/{trackerId}/working-sets | Lists Working-Sets
[**get_working_set_information**](WorkingSetApi.md#get_working_set_information) | **GET** /v3/working-sets/{workingSetId} | Working-Set information
[**get_working_set_trackers**](WorkingSetApi.md#get_working_set_trackers) | **GET** /v3/working-sets/{workingSetId}/trackers |  Lists the trackers in a Working-Set
[**list_working_sets_of_project**](WorkingSetApi.md#list_working_sets_of_project) | **GET** /v3/projects/{projectId}/working-sets | Project level Working-Sets information

# **get_items_mapping_in_working_set**
> list[WorkingSetItemMapping] get_items_mapping_in_working_set(body)

Maps Tracker Items in Working-Set

Maps Tracker Items to the corresponding Tracker Items in target Working-Set.

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
api_instance = swagger_client.WorkingSetApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkingSetItemsMappingRequest() # WorkingSetItemsMappingRequest | 

try:
    # Maps Tracker Items in Working-Set
    api_response = api_instance.get_items_mapping_in_working_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingSetApi->get_items_mapping_in_working_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkingSetItemsMappingRequest**](WorkingSetItemsMappingRequest.md)|  | 

### Return type

[**list[WorkingSetItemMapping]**](WorkingSetItemMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_working_sets**
> list[TrackerWorkingSet] get_tracker_working_sets(tracker_id, include_deleted=include_deleted)

Lists Working-Sets

Lists Working-Sets that contain the given Tracker or Branch.

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
api_instance = swagger_client.WorkingSetApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | Tracker or Branch id
include_deleted = true # bool | Find Tracker or Branch if deleted and the result contains the deleted Working-Sets (optional)

try:
    # Lists Working-Sets
    api_response = api_instance.get_tracker_working_sets(tracker_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingSetApi->get_tracker_working_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**| Tracker or Branch id | 
 **include_deleted** | **bool**| Find Tracker or Branch if deleted and the result contains the deleted Working-Sets | [optional] 

### Return type

[**list[TrackerWorkingSet]**](TrackerWorkingSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_working_set_information**
> WorkingSetInformation get_working_set_information(working_set_id, include_deleted=include_deleted)

Working-Set information

Gets the Working-Set information for the given id.

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
api_instance = swagger_client.WorkingSetApi(swagger_client.ApiClient(configuration))
working_set_id = 56 # int | Id of the Working-Set
include_deleted = true # bool | The result contains the deleted Working-Sets (optional)

try:
    # Working-Set information
    api_response = api_instance.get_working_set_information(working_set_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingSetApi->get_working_set_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_set_id** | **int**| Id of the Working-Set | 
 **include_deleted** | **bool**| The result contains the deleted Working-Sets | [optional] 

### Return type

[**WorkingSetInformation**](WorkingSetInformation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_working_set_trackers**
> list[WorkingSetTracker] get_working_set_trackers(working_set_id, include_deleted=include_deleted)

 Lists the trackers in a Working-Set

Lists the trackers (shared and included) in the given Working-Set.

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
api_instance = swagger_client.WorkingSetApi(swagger_client.ApiClient(configuration))
working_set_id = 56 # int | Working-Set id
include_deleted = true # bool | The result contains the deleted Trackers (optional)

try:
    #  Lists the trackers in a Working-Set
    api_response = api_instance.get_working_set_trackers(working_set_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingSetApi->get_working_set_trackers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_set_id** | **int**| Working-Set id | 
 **include_deleted** | **bool**| The result contains the deleted Trackers | [optional] 

### Return type

[**list[WorkingSetTracker]**](WorkingSetTracker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_working_sets_of_project**
> list[WorkingSetMinimal] list_working_sets_of_project(project_id, include_deleted=include_deleted)

Project level Working-Sets information

Lists top-level Working-Sets minimal information for the given project.

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
api_instance = swagger_client.WorkingSetApi(swagger_client.ApiClient(configuration))
project_id = 56 # int | The id of the project
include_deleted = true # bool | The result lists the deleted Working-Sets (optional)

try:
    # Project level Working-Sets information
    api_response = api_instance.list_working_sets_of_project(project_id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkingSetApi->list_working_sets_of_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The id of the project | 
 **include_deleted** | **bool**| The result lists the deleted Working-Sets | [optional] 

### Return type

[**list[WorkingSetMinimal]**](WorkingSetMinimal.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

