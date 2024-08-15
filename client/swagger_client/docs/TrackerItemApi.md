# swagger_client.TrackerItemApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_child_to_tracker**](TrackerItemApi.md#add_child_to_tracker) | **POST** /v3/trackers/{trackerId}/children | Add a child item to a tracker item
[**add_child_to_tracker_item**](TrackerItemApi.md#add_child_to_tracker_item) | **POST** /v3/items/{itemId}/children | Add a child item to a tracker item
[**bulk_update_tracker_item_fields**](TrackerItemApi.md#bulk_update_tracker_item_fields) | **PUT** /v3/items/fields | Bulk update fields of a tracker item
[**check_tracker_item_lock**](TrackerItemApi.md#check_tracker_item_lock) | **GET** /v3/items/{itemId}/lock | Check whether a tracker item is locked, and if it is, retrieve the details of the lock
[**create_tracker_item**](TrackerItemApi.md#create_tracker_item) | **POST** /v3/trackers/{trackerId}/items | Create a tracker item
[**delete_tracker_item**](TrackerItemApi.md#delete_tracker_item) | **DELETE** /v3/items/{itemId} | Move tracker item to trash
[**find_tracker_children**](TrackerItemApi.md#find_tracker_children) | **GET** /v3/trackers/{trackerId}/children | Get child items of a tracker item
[**find_tracker_item_children**](TrackerItemApi.md#find_tracker_item_children) | **GET** /v3/items/{itemId}/children | Get child items of a tracker item
[**find_tracker_items**](TrackerItemApi.md#find_tracker_items) | **GET** /v3/items/query | Get tracker items by cbQL query string
[**find_tracker_items_by_cb_ql**](TrackerItemApi.md#find_tracker_items_by_cb_ql) | **POST** /v3/items/query | Get tracker items by cbQL query string
[**get_baseline_tracker_item_relations**](TrackerItemApi.md#get_baseline_tracker_item_relations) | **GET** /v3/items/{itemId}/relations | Get tracker items related to a tracker item
[**get_baseline_tracker_items_relations**](TrackerItemApi.md#get_baseline_tracker_items_relations) | **POST** /v3/items/relations | Get tracker items related to some tracker items
[**get_choice_options**](TrackerItemApi.md#get_choice_options) | **GET** /v3/items/{itemId}/fields/{fieldId}/options | Get the options of a choice field of tracker
[**get_item_accessibility**](TrackerItemApi.md#get_item_accessibility) | **GET** /v3/items/{itemId}/fields/accessibility | Get a tracker item fields accessibility
[**get_tracker_item**](TrackerItemApi.md#get_tracker_item) | **GET** /v3/items/{itemId} | Get basic tracker item
[**get_tracker_item_fields**](TrackerItemApi.md#get_tracker_item_fields) | **GET** /v3/items/{itemId}/fields | Get fields of a tracker item
[**get_tracker_item_history**](TrackerItemApi.md#get_tracker_item_history) | **GET** /v3/items/{itemId}/history | Get tracker item history
[**get_tracker_item_reviews**](TrackerItemApi.md#get_tracker_item_reviews) | **GET** /v3/items/{itemId}/reviews | Get all Tracker Item Reviews for a particular Tracker Item
[**get_tracker_item_transitions**](TrackerItemApi.md#get_tracker_item_transitions) | **GET** /v3/items/{itemId}/transitions | Get available transitions for a tracker item
[**lock_tracker_item**](TrackerItemApi.md#lock_tracker_item) | **PUT** /v3/items/{itemId}/lock | Put a soft lock on a tracker item
[**patch_children_of_tracker**](TrackerItemApi.md#patch_children_of_tracker) | **PATCH** /v3/trackers/{trackerId}/children | Patch the child item list of a tracker item
[**patch_children_of_tracker_item**](TrackerItemApi.md#patch_children_of_tracker_item) | **PATCH** /v3/items/{itemId}/children | Patch the child item list of a tracker item
[**replace_children_of_tracker**](TrackerItemApi.md#replace_children_of_tracker) | **PUT** /v3/trackers/{trackerId}/children | Reorder the child item list of a tracker
[**replace_children_of_tracker_item**](TrackerItemApi.md#replace_children_of_tracker_item) | **PUT** /v3/items/{itemId}/children | Replace the child item list of a tracker item
[**unlock_tracker_item**](TrackerItemApi.md#unlock_tracker_item) | **DELETE** /v3/items/{itemId}/lock | Unlock a tracker item
[**update_custom_field_tracker_item**](TrackerItemApi.md#update_custom_field_tracker_item) | **PUT** /v3/items/{itemId}/fields | Update fields of a tracker item
[**update_table_field_tracker_item**](TrackerItemApi.md#update_table_field_tracker_item) | **PUT** /v3/items/{itemId}/fields/tables/{tableFieldId} | Update table field of tracker item
[**update_tracker_item**](TrackerItemApi.md#update_tracker_item) | **PUT** /v3/items/{itemId} | Update tracker item

# **add_child_to_tracker**
> TrackerItemChildReference add_child_to_tracker(body, tracker_id)

Add a child item to a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemRevision() # TrackerItemRevision | 
tracker_id = 56 # int | 

try:
    # Add a child item to a tracker item
    api_response = api_instance.add_child_to_tracker(body, tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->add_child_to_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemRevision**](TrackerItemRevision.md)|  | 
 **tracker_id** | **int**|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_child_to_tracker_item**
> TrackerItemChildReference add_child_to_tracker_item(body, item_id)

Add a child item to a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemRevision() # TrackerItemRevision | 
item_id = 56 # int | 

try:
    # Add a child item to a tracker item
    api_response = api_instance.add_child_to_tracker_item(body, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->add_child_to_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemRevision**](TrackerItemRevision.md)|  | 
 **item_id** | **int**|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_tracker_item_fields**
> BulkOperationResponse bulk_update_tracker_item_fields(body, atomic=atomic)

Bulk update fields of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = [swagger_client.UpdateTrackerItemFieldWithItemId()] # list[UpdateTrackerItemFieldWithItemId] | 
atomic = false # bool | If it's turned on the whole update will run in a single transaction. (optional) (default to false)

try:
    # Bulk update fields of a tracker item
    api_response = api_instance.bulk_update_tracker_item_fields(body, atomic=atomic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->bulk_update_tracker_item_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UpdateTrackerItemFieldWithItemId]**](UpdateTrackerItemFieldWithItemId.md)|  | 
 **atomic** | **bool**| If it&#x27;s turned on the whole update will run in a single transaction. | [optional] [default to false]

### Return type

[**BulkOperationResponse**](BulkOperationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_tracker_item_lock**
> LockInfo check_tracker_item_lock(item_id)

Check whether a tracker item is locked, and if it is, retrieve the details of the lock

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | Tracker item id

try:
    # Check whether a tracker item is locked, and if it is, retrieve the details of the lock
    api_response = api_instance.check_tracker_item_lock(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->check_tracker_item_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 

### Return type

[**LockInfo**](LockInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracker_item**
> TrackerItem create_tracker_item(body, tracker_id, parent_item_id=parent_item_id, reference_item_id=reference_item_id, position=position)

Create a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItem() # TrackerItem | 
tracker_id = 56 # int | 
parent_item_id = 56 # int |  (optional)
reference_item_id = 56 # int |  (optional)
position = 'position_example' # str |  (optional)

try:
    # Create a tracker item
    api_response = api_instance.create_tracker_item(body, tracker_id, parent_item_id=parent_item_id, reference_item_id=reference_item_id, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->create_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItem**](TrackerItem.md)|  | 
 **tracker_id** | **int**|  | 
 **parent_item_id** | **int**|  | [optional] 
 **reference_item_id** | **int**|  | [optional] 
 **position** | **str**|  | [optional] 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item**
> TrackerItem delete_tracker_item(item_id)

Move tracker item to trash

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Move tracker item to trash
    api_response = api_instance.delete_tracker_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->delete_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_children**
> TrackerItemReferenceSearchResult find_tracker_children(tracker_id, page=page, page_size=page_size)

Get child items of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Get child items of a tracker item
    api_response = api_instance.find_tracker_children(tracker_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->find_tracker_children: %s\n" % e)
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

# **find_tracker_item_children**
> TrackerItemReferenceSearchResult find_tracker_item_children(item_id, page=page, page_size=page_size)

Get child items of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Get child items of a tracker item
    api_response = api_instance.find_tracker_item_children(item_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->find_tracker_item_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
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

# **find_tracker_items**
> TrackerItemSearchResult find_tracker_items(query_string, baseline_id=baseline_id, page=page, page_size=page_size)

Get tracker items by cbQL query string

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
query_string = 'query_string_example' # str | 
baseline_id = 56 # int | Baseline on which the queery is applied. (optional)
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Get tracker items by cbQL query string
    api_response = api_instance.find_tracker_items(query_string, baseline_id=baseline_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->find_tracker_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_string** | **str**|  | 
 **baseline_id** | **int**| Baseline on which the queery is applied. | [optional] 
 **page** | **int**| Index of the result page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items in a result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemSearchResult**](TrackerItemSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_items_by_cb_ql**
> TrackerItemSearchResult find_tracker_items_by_cb_ql(body)

Get tracker items by cbQL query string

API can be called with a complex cbQL string to find tracker items

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemSearchRequest() # TrackerItemSearchRequest | 

try:
    # Get tracker items by cbQL query string
    api_response = api_instance.find_tracker_items_by_cb_ql(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->find_tracker_items_by_cb_ql: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemSearchRequest**](TrackerItemSearchRequest.md)|  | 

### Return type

[**TrackerItemSearchResult**](TrackerItemSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseline_tracker_item_relations**
> TrackerItemRelationsResult get_baseline_tracker_item_relations(item_id, baseline_id=baseline_id, page=page, page_size=page_size)

Get tracker items related to a tracker item

Use this endpoint to fetch tracker items related to a specified tracker item. The relations include downstream references, upstream references, incoming associations and outgoing associations of the given item. Relations with entities that are not tracker items (e.g., trackers, projects, URLs, etc.) will not be included in the result.

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
baseline_id = 56 # int |  (optional)
page = 1 # int | Index of page, starting from 1. (optional) (default to 1)
page_size = 500 # int | Number of items per page. Max value: 500 (optional) (default to 500)

try:
    # Get tracker items related to a tracker item
    api_response = api_instance.get_baseline_tracker_item_relations(item_id, baseline_id=baseline_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_baseline_tracker_item_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **baseline_id** | **int**|  | [optional] 
 **page** | **int**| Index of page, starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. Max value: 500 | [optional] [default to 500]

### Return type

[**TrackerItemRelationsResult**](TrackerItemRelationsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseline_tracker_items_relations**
> list[TrackerItemRelationsResult] get_baseline_tracker_items_relations(body, baseline_id=baseline_id)

Get tracker items related to some tracker items

Use this endpoint to fetch tracker items related to some specified tracker items. The relations include downstream references, upstream references, incoming associations and outgoing associations of the given items. Relations with entities that are not tracker items (e.g., trackers, projects, URLs, etc.) will not be included in the result.

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemsRequest() # TrackerItemsRequest | 
baseline_id = 56 # int |  (optional)

try:
    # Get tracker items related to some tracker items
    api_response = api_instance.get_baseline_tracker_items_relations(body, baseline_id=baseline_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_baseline_tracker_items_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemsRequest**](TrackerItemsRequest.md)|  | 
 **baseline_id** | **int**|  | [optional] 

### Return type

[**list[TrackerItemRelationsResult]**](TrackerItemRelationsResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_choice_options**
> ReferenceSearchResult get_choice_options(item_id, field_id, page=page, page_size=page_size)

Get the options of a choice field of tracker

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
field_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Get the options of a choice field of tracker
    api_response = api_instance.get_choice_options(item_id, field_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_choice_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **field_id** | **int**|  | 
 **page** | **int**| Index of the result page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items in a result page. Max value: 500 | [optional] [default to 25]

### Return type

[**ReferenceSearchResult**](ReferenceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_accessibility**
> TrackerItemFieldAccessibilityList get_item_accessibility(item_id, target_status_id=target_status_id)

Get a tracker item fields accessibility

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | Tracker item id
target_status_id = 56 # int |  (optional)

try:
    # Get a tracker item fields accessibility
    api_response = api_instance.get_item_accessibility(item_id, target_status_id=target_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_item_accessibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 
 **target_status_id** | **int**|  | [optional] 

### Return type

[**TrackerItemFieldAccessibilityList**](TrackerItemFieldAccessibilityList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item**
> TrackerItem get_tracker_item(item_id, version=version, baseline_id=baseline_id)

Get basic tracker item

API can be used for fetching basic information of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
version = 56 # int |  (optional)
baseline_id = 56 # int |  (optional)

try:
    # Get basic tracker item
    api_response = api_instance.get_tracker_item(item_id, version=version, baseline_id=baseline_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **version** | **int**|  | [optional] 
 **baseline_id** | **int**|  | [optional] 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_fields**
> TrackerItemField get_tracker_item_fields(item_id)

Get fields of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Get fields of a tracker item
    api_response = api_instance.get_tracker_item_fields(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**TrackerItemField**](TrackerItemField.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_history**
> TrackerItemHistory get_tracker_item_history(item_id)

Get tracker item history

API can be used for fetching basic information of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Get tracker item history
    api_response = api_instance.get_tracker_item_history(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**TrackerItemHistory**](TrackerItemHistory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_reviews**
> list[TrackerItemReview] get_tracker_item_reviews(item_id)

Get all Tracker Item Reviews for a particular Tracker Item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Get all Tracker Item Reviews for a particular Tracker Item
    api_response = api_instance.get_tracker_item_reviews(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item_reviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**list[TrackerItemReview]**](TrackerItemReview.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_transitions**
> list[WorkflowTransition] get_tracker_item_transitions(item_id)

Get available transitions for a tracker item

API can be used for getting available transitions for a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Get available transitions for a tracker item
    api_response = api_instance.get_tracker_item_transitions(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->get_tracker_item_transitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**list[WorkflowTransition]**](WorkflowTransition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_tracker_item**
> lock_tracker_item(body, item_id)

Put a soft lock on a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.LockRequest() # LockRequest | 
item_id = 56 # int | Tracker item id

try:
    # Put a soft lock on a tracker item
    api_instance.lock_tracker_item(body, item_id)
except ApiException as e:
    print("Exception when calling TrackerItemApi->lock_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LockRequest**](LockRequest.md)|  | 
 **item_id** | **int**| Tracker item id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_children_of_tracker**
> TrackerItemChildReference patch_children_of_tracker(body, tracker_id, mode=mode)

Patch the child item list of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemChildReference() # TrackerItemChildReference | 
tracker_id = 56 # int | 
mode = 'INSERT' # str |  (optional) (default to INSERT)

try:
    # Patch the child item list of a tracker item
    api_response = api_instance.patch_children_of_tracker(body, tracker_id, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->patch_children_of_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemChildReference**](TrackerItemChildReference.md)|  | 
 **tracker_id** | **int**|  | 
 **mode** | **str**|  | [optional] [default to INSERT]

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_children_of_tracker_item**
> TrackerItemChildReference patch_children_of_tracker_item(body, mode, item_id)

Patch the child item list of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemChildReference() # TrackerItemChildReference | 
mode = 'mode_example' # str | 
item_id = 56 # int | 

try:
    # Patch the child item list of a tracker item
    api_response = api_instance.patch_children_of_tracker_item(body, mode, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->patch_children_of_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemChildReference**](TrackerItemChildReference.md)|  | 
 **mode** | **str**|  | 
 **item_id** | **int**|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_children_of_tracker**
> TrackerItemReferenceSearchResult replace_children_of_tracker(body, tracker_id, result_page_size=result_page_size)

Reorder the child item list of a tracker

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTrackerItemChildrenRequest() # UpdateTrackerItemChildrenRequest | 
tracker_id = 56 # int | 
result_page_size = 25 # int | Number of items in the result page. Max value: 500 (optional) (default to 25)

try:
    # Reorder the child item list of a tracker
    api_response = api_instance.replace_children_of_tracker(body, tracker_id, result_page_size=result_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->replace_children_of_tracker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTrackerItemChildrenRequest**](UpdateTrackerItemChildrenRequest.md)|  | 
 **tracker_id** | **int**|  | 
 **result_page_size** | **int**| Number of items in the result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemReferenceSearchResult**](TrackerItemReferenceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_children_of_tracker_item**
> TrackerItemReferenceSearchResult replace_children_of_tracker_item(body, item_id, result_page_size=result_page_size)

Replace the child item list of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTrackerItemChildrenRequest() # UpdateTrackerItemChildrenRequest | 
item_id = 56 # int | 
result_page_size = 25 # int | Number of items in the result page. Max value: 500 (optional) (default to 25)

try:
    # Replace the child item list of a tracker item
    api_response = api_instance.replace_children_of_tracker_item(body, item_id, result_page_size=result_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->replace_children_of_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTrackerItemChildrenRequest**](UpdateTrackerItemChildrenRequest.md)|  | 
 **item_id** | **int**|  | 
 **result_page_size** | **int**| Number of items in the result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemReferenceSearchResult**](TrackerItemReferenceSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_tracker_item**
> unlock_tracker_item(item_id)

Unlock a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | Tracker item id

try:
    # Unlock a tracker item
    api_instance.unlock_tracker_item(item_id)
except ApiException as e:
    print("Exception when calling TrackerItemApi->unlock_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_tracker_item**
> TrackerItem update_custom_field_tracker_item(body, item_id, quiet_mode=quiet_mode)

Update fields of a tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTrackerItemField() # UpdateTrackerItemField | 
item_id = 56 # int | 
quiet_mode = false # bool | If it's turned on HTTP 200 with empty response indicates that the update was successful. (optional) (default to false)

try:
    # Update fields of a tracker item
    api_response = api_instance.update_custom_field_tracker_item(body, item_id, quiet_mode=quiet_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->update_custom_field_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTrackerItemField**](UpdateTrackerItemField.md)|  | 
 **item_id** | **int**|  | 
 **quiet_mode** | **bool**| If it&#x27;s turned on HTTP 200 with empty response indicates that the update was successful. | [optional] [default to false]

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_field_tracker_item**
> TrackerItem update_table_field_tracker_item(body, item_id, table_field_id)

Update table field of tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTrackerItemTableField() # UpdateTrackerItemTableField | 
item_id = 56 # int | 
table_field_id = 56 # int | 

try:
    # Update table field of tracker item
    api_response = api_instance.update_table_field_tracker_item(body, item_id, table_field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->update_table_field_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTrackerItemTableField**](UpdateTrackerItemTableField.md)|  | 
 **item_id** | **int**|  | 
 **table_field_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_item**
> TrackerItem update_tracker_item(body, item_id, reference_item_id=reference_item_id, position=position)

Update tracker item

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
api_instance = swagger_client.TrackerItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItem() # TrackerItem | 
item_id = 56 # int | 
reference_item_id = 56 # int |  (optional)
position = 'position_example' # str |  (optional)

try:
    # Update tracker item
    api_response = api_instance.update_tracker_item(body, item_id, reference_item_id=reference_item_id, position=position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemApi->update_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItem**](TrackerItem.md)|  | 
 **item_id** | **int**|  | 
 **reference_item_id** | **int**|  | [optional] 
 **position** | **str**|  | [optional] 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

