# swagger_client.TrackerApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tracker**](TrackerApi.md#delete_tracker) | **DELETE** /v3/trackers/{trackerId} | Deletes a tracker
[**get_choice_option**](TrackerApi.md#get_choice_option) | **GET** /v3/trackers/{trackerId}/fields/{fieldId}/options/{optionId} | Get option of a choice field of tracker
[**get_items_by_tracker**](TrackerApi.md#get_items_by_tracker) | **GET** /v3/trackers/{trackerId}/items | Get items in a specific tracker
[**get_tracker**](TrackerApi.md#get_tracker) | **GET** /v3/trackers/{trackerId} | Get tracker
[**get_tracker_baselines**](TrackerApi.md#get_tracker_baselines) | **GET** /v3/trackers/{trackerId}/baselines | Get baselines of a specific tracker
[**get_tracker_configuration**](TrackerApi.md#get_tracker_configuration) | **GET** /v3/tracker/{trackerId}/configuration | Get tracker configuration
[**get_tracker_field**](TrackerApi.md#get_tracker_field) | **GET** /v3/trackers/{trackerId}/fields/{fieldId} | Get field of tracker
[**get_tracker_field_permissions**](TrackerApi.md#get_tracker_field_permissions) | **GET** /v3/trackers/{trackerId}/fields/{fieldId}/permissions | Get permissions of tracker field
[**get_tracker_fields**](TrackerApi.md#get_tracker_fields) | **GET** /v3/trackers/{trackerId}/fields | Get fields of tracker
[**get_tracker_fields_permissions**](TrackerApi.md#get_tracker_fields_permissions) | **GET** /v3/trackers/{trackerId}/fields/permissions | Get permissions of all fields of a tracker
[**get_tracker_outline**](TrackerApi.md#get_tracker_outline) | **GET** /v3/trackers/{trackerId}/outline | Get outline of a specific tracker
[**get_tracker_schema**](TrackerApi.md#get_tracker_schema) | **GET** /v3/trackers/{trackerId}/schema | Get the schema of a tracker
[**get_tracker_transitions**](TrackerApi.md#get_tracker_transitions) | **GET** /v3/trackers/{trackerId}/transitions | Get all transitions of a specific tracker
[**get_tracker_type**](TrackerApi.md#get_tracker_type) | **GET** /v3/trackers/types/{trackerTypeId} | Get the immutable definition of a tracker type
[**get_tracker_types**](TrackerApi.md#get_tracker_types) | **GET** /v3/trackers/types | Get the list of tracker types
[**post_tracker_configuration**](TrackerApi.md#post_tracker_configuration) | **POST** /v3/tracker/configuration | Create or update tracker configuration
[**update_tracker**](TrackerApi.md#update_tracker) | **PUT** /v3/trackers/{trackerId} | Updates a specific tracker
[**update_tracker_icon**](TrackerApi.md#update_tracker_icon) | **PUT** /v3/trackers/{trackerId}/icon | Upload a tracker icon

# **delete_tracker**
> delete_tracker(tracker_id)

Deletes a tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Deletes a tracker
    api_instance.delete_tracker(tracker_id)
except ApiException as e:
    print("Exception when calling TrackerApi->delete_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_choice_option**
> ChoiceOptionReference get_choice_option(tracker_id, field_id, option_id)

Get option of a choice field of tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
field_id = 56 # int | 
option_id = 56 # int | 

try:
    # Get option of a choice field of tracker
    api_response = api_instance.get_choice_option(tracker_id, field_id, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_choice_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **field_id** | **int**|  | 
 **option_id** | **int**|  | 

### Return type

[**ChoiceOptionReference**](ChoiceOptionReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_tracker**
> TrackerItemReferenceSearchResult get_items_by_tracker(tracker_id, page=page, page_size=page_size)

Get items in a specific tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Get items in a specific tracker
    api_response = api_instance.get_items_by_tracker(tracker_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_items_by_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **page** | **int**| Index of the result page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items in a result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemReferenceSearchResult**](TrackerItemReferenceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker**
> Tracker get_tracker(tracker_id)

Get tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get tracker
    api_response = api_instance.get_tracker(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**Tracker**](Tracker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_baselines**
> ReferenceSearchResult get_tracker_baselines(tracker_id)

Get baselines of a specific tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get baselines of a specific tracker
    api_response = api_instance.get_tracker_baselines(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_baselines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**ReferenceSearchResult**](ReferenceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_configuration**
> TrackerConfiguration get_tracker_configuration(tracker_id)

Get tracker configuration

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get tracker configuration
    api_response = api_instance.get_tracker_configuration(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**TrackerConfiguration**](TrackerConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_field**
> AbstractField get_tracker_field(tracker_id, field_id)

Get field of tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
field_id = 56 # int | 

try:
    # Get field of tracker
    api_response = api_instance.get_tracker_field(tracker_id, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **field_id** | **int**|  | 

### Return type

[**AbstractField**](AbstractField.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_field_permissions**
> list[TrackerFieldStatusPermissions] get_tracker_field_permissions(tracker_id, field_id, status_id=status_id)

Get permissions of tracker field

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
field_id = 56 # int | 
status_id = 56 # int |  (optional)

try:
    # Get permissions of tracker field
    api_response = api_instance.get_tracker_field_permissions(tracker_id, field_id, status_id=status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_field_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **field_id** | **int**|  | 
 **status_id** | **int**|  | [optional] 

### Return type

[**list[TrackerFieldStatusPermissions]**](TrackerFieldStatusPermissions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_fields**
> list[FieldReference] get_tracker_fields(tracker_id)

Get fields of tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get fields of tracker
    api_response = api_instance.get_tracker_fields(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**list[FieldReference]**](FieldReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_fields_permissions**
> TrackerFieldsStatusPermissions get_tracker_fields_permissions(tracker_id, status_id=status_id)

Get permissions of all fields of a tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
status_id = 56 # int |  (optional)

try:
    # Get permissions of all fields of a tracker
    api_response = api_instance.get_tracker_fields_permissions(tracker_id, status_id=status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_fields_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **status_id** | **int**|  | [optional] 

### Return type

[**TrackerFieldsStatusPermissions**](TrackerFieldsStatusPermissions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_outline**
> OutlineItemSearchResult get_tracker_outline(tracker_id, parent_item_id=parent_item_id, result_depth_filter=result_depth_filter)

Get outline of a specific tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
parent_item_id = 56 # int | Show only the children of this item. (optional)
result_depth_filter = 56 # int | The depth level of the result outline. (optional)

try:
    # Get outline of a specific tracker
    api_response = api_instance.get_tracker_outline(tracker_id, parent_item_id=parent_item_id, result_depth_filter=result_depth_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **parent_item_id** | **int**| Show only the children of this item. | [optional] 
 **result_depth_filter** | **int**| The depth level of the result outline. | [optional] 

### Return type

[**OutlineItemSearchResult**](OutlineItemSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_schema**
> list[AbstractField] get_tracker_schema(tracker_id)

Get the schema of a tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get the schema of a tracker
    api_response = api_instance.get_tracker_schema(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**list[AbstractField]**](AbstractField.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_transitions**
> list[WorkflowTransition] get_tracker_transitions(tracker_id, from_status_id=from_status_id)

Get all transitions of a specific tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
from_status_id = 56 # int | The from status id filter for transitions. (optional)

try:
    # Get all transitions of a specific tracker
    api_response = api_instance.get_tracker_transitions(tracker_id, from_status_id=from_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_transitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **from_status_id** | **int**| The from status id filter for transitions. | [optional] 

### Return type

[**list[WorkflowTransition]**](WorkflowTransition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_type**
> TrackerType get_tracker_type(tracker_type_id)

Get the immutable definition of a tracker type

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_type_id = 56 # int | 

try:
    # Get the immutable definition of a tracker type
    api_response = api_instance.get_tracker_type(tracker_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_type_id** | **int**|  | 

### Return type

[**TrackerType**](TrackerType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_types**
> list[TrackerTypeReference] get_tracker_types(outline=outline)

Get the list of tracker types

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
outline = 'ANY' # str | Outline is enabled, disabled or any(no filtering will be applied). (optional) (default to ANY)

try:
    # Get the list of tracker types
    api_response = api_instance.get_tracker_types(outline=outline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->get_tracker_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outline** | **str**| Outline is enabled, disabled or any(no filtering will be applied). | [optional] [default to ANY]

### Return type

[**list[TrackerTypeReference]**](TrackerTypeReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tracker_configuration**
> TrackerConfiguration post_tracker_configuration(body)

Create or update tracker configuration

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerConfiguration() # TrackerConfiguration | 

try:
    # Create or update tracker configuration
    api_response = api_instance.post_tracker_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->post_tracker_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerConfiguration**](TrackerConfiguration.md)|  | 

### Return type

[**TrackerConfiguration**](TrackerConfiguration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker**
> Tracker update_tracker(body, tracker_id)

Updates a specific tracker

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Tracker() # Tracker | 
tracker_id = 56 # int | 

try:
    # Updates a specific tracker
    api_response = api_instance.update_tracker(body, tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerApi->update_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tracker**](Tracker.md)|  | 
 **tracker_id** | **int**|  | 

### Return type

[**Tracker**](Tracker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_icon**
> update_tracker_icon(tracker_id, icon=icon)

Upload a tracker icon

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
api_instance = swagger_client.TrackerApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | Id of the tracker
icon = 'icon_example' # str |  (optional)

try:
    # Upload a tracker icon
    api_instance.update_tracker_icon(tracker_id, icon=icon)
except ApiException as e:
    print("Exception when calling TrackerApi->update_tracker_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**| Id of the tracker | 
 **icon** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

