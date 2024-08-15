# openapi_client.TrackerItemApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

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
> TrackerItemChildReference add_child_to_tracker(tracker_id, tracker_item_revision)

Add a child item to a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference
from openapi_client.models.tracker_item_revision import TrackerItemRevision
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_id = 56 # int | 
    tracker_item_revision = openapi_client.TrackerItemRevision() # TrackerItemRevision | 

    try:
        # Add a child item to a tracker item
        api_response = api_instance.add_child_to_tracker(tracker_id, tracker_item_revision)
        print("The response of TrackerItemApi->add_child_to_tracker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->add_child_to_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **tracker_item_revision** | [**TrackerItemRevision**](TrackerItemRevision.md)|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Child item reference with index |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_child_to_tracker_item**
> TrackerItemChildReference add_child_to_tracker_item(item_id, tracker_item_revision)

Add a child item to a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference
from openapi_client.models.tracker_item_revision import TrackerItemRevision
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    tracker_item_revision = openapi_client.TrackerItemRevision() # TrackerItemRevision | 

    try:
        # Add a child item to a tracker item
        api_response = api_instance.add_child_to_tracker_item(item_id, tracker_item_revision)
        print("The response of TrackerItemApi->add_child_to_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->add_child_to_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **tracker_item_revision** | [**TrackerItemRevision**](TrackerItemRevision.md)|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Child item reference with index |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_tracker_item_fields**
> BulkOperationResponse bulk_update_tracker_item_fields(update_tracker_item_field_with_item_id, atomic=atomic)

Bulk update fields of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.bulk_operation_response import BulkOperationResponse
from openapi_client.models.update_tracker_item_field_with_item_id import UpdateTrackerItemFieldWithItemId
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    update_tracker_item_field_with_item_id = [openapi_client.UpdateTrackerItemFieldWithItemId()] # List[UpdateTrackerItemFieldWithItemId] | 
    atomic = False # bool | If it's turned on the whole update will run in a single transaction. (optional) (default to False)

    try:
        # Bulk update fields of a tracker item
        api_response = api_instance.bulk_update_tracker_item_fields(update_tracker_item_field_with_item_id, atomic=atomic)
        print("The response of TrackerItemApi->bulk_update_tracker_item_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->bulk_update_tracker_item_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_tracker_item_field_with_item_id** | [**List[UpdateTrackerItemFieldWithItemId]**](UpdateTrackerItemFieldWithItemId.md)|  | 
 **atomic** | **bool**| If it&#39;s turned on the whole update will run in a single transaction. | [optional] [default to False]

### Return type

[**BulkOperationResponse**](BulkOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulk update response |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Field not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_tracker_item_lock**
> LockInfo check_tracker_item_lock(item_id)

Check whether a tracker item is locked, and if it is, retrieve the details of the lock

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.lock_info import LockInfo
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | Tracker item id

    try:
        # Check whether a tracker item is locked, and if it is, retrieve the details of the lock
        api_response = api_instance.check_tracker_item_lock(item_id)
        print("The response of TrackerItemApi->check_tracker_item_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->check_tracker_item_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 

### Return type

[**LockInfo**](LockInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the lock, or an empty response |  -  |
**401** | Authentication is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracker_item**
> TrackerItem create_tracker_item(tracker_id, tracker_item, parent_item_id=parent_item_id, reference_item_id=reference_item_id, position=position)

Create a tracker item

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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_id = 56 # int | 
    tracker_item = openapi_client.TrackerItem() # TrackerItem | 
    parent_item_id = 56 # int |  (optional)
    reference_item_id = 56 # int |  (optional)
    position = 'position_example' # str |  (optional)

    try:
        # Create a tracker item
        api_response = api_instance.create_tracker_item(tracker_id, tracker_item, parent_item_id=parent_item_id, reference_item_id=reference_item_id, position=position)
        print("The response of TrackerItemApi->create_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->create_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **tracker_item** | [**TrackerItem**](TrackerItem.md)|  | 
 **parent_item_id** | **int**|  | [optional] 
 **reference_item_id** | **int**|  | [optional] 
 **position** | **str**|  | [optional] 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Field not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item**
> TrackerItem delete_tracker_item(item_id)

Move tracker item to trash

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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 

    try:
        # Move tracker item to trash
        api_response = api_instance.delete_tracker_item(item_id)
        print("The response of TrackerItemApi->delete_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->delete_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

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
**200** | Basic tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_children**
> TrackerItemReferenceSearchResult find_tracker_children(tracker_id, page=page, page_size=page_size)

Get child items of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_id = 56 # int | 
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Get child items of a tracker item
        api_response = api_instance.find_tracker_children(tracker_id, page=page, page_size=page_size)
        print("The response of TrackerItemApi->find_tracker_children:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List child items of a tracker item ordered by ordinal |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_item_children**
> TrackerItemReferenceSearchResult find_tracker_item_children(item_id, page=page, page_size=page_size)

Get child items of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Get child items of a tracker item
        api_response = api_instance.find_tracker_item_children(item_id, page=page, page_size=page_size)
        print("The response of TrackerItemApi->find_tracker_item_children:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List child items of a tracker item ordered by ordinal |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_items**
> TrackerItemSearchResult find_tracker_items(query_string, baseline_id=baseline_id, page=page, page_size=page_size)

Get tracker items by cbQL query string

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_search_result import TrackerItemSearchResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    query_string = 'priority='Normal'' # str | 
    baseline_id = 56 # int | Baseline on which the queery is applied. (optional)
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Get tracker items by cbQL query string
        api_response = api_instance.find_tracker_items(query_string, baseline_id=baseline_id, page=page, page_size=page_size)
        print("The response of TrackerItemApi->find_tracker_items:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List tracker items by cbQL |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tracker_items_by_cb_ql**
> TrackerItemSearchResult find_tracker_items_by_cb_ql(tracker_item_search_request)

Get tracker items by cbQL query string

API can be called with a complex cbQL string to find tracker items

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_search_request import TrackerItemSearchRequest
from openapi_client.models.tracker_item_search_result import TrackerItemSearchResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_item_search_request = openapi_client.TrackerItemSearchRequest() # TrackerItemSearchRequest | 

    try:
        # Get tracker items by cbQL query string
        api_response = api_instance.find_tracker_items_by_cb_ql(tracker_item_search_request)
        print("The response of TrackerItemApi->find_tracker_items_by_cb_ql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->find_tracker_items_by_cb_ql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_item_search_request** | [**TrackerItemSearchRequest**](TrackerItemSearchRequest.md)|  | 

### Return type

[**TrackerItemSearchResult**](TrackerItemSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List tracker items by cbQL |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseline_tracker_item_relations**
> TrackerItemRelationsResult get_baseline_tracker_item_relations(item_id, baseline_id=baseline_id, page=page, page_size=page_size)

Get tracker items related to a tracker item

Use this endpoint to fetch tracker items related to a specified tracker item. The relations include downstream references, upstream references, incoming associations and outgoing associations of the given item. Relations with entities that are not tracker items (e.g., trackers, projects, URLs, etc.) will not be included in the result.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_relations_result import TrackerItemRelationsResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    baseline_id = 56 # int |  (optional)
    page = 1 # int | Index of page, starting from 1. (optional) (default to 1)
    page_size = 500 # int | Number of items per page. Max value: 500 (optional) (default to 500)

    try:
        # Get tracker items related to a tracker item
        api_response = api_instance.get_baseline_tracker_item_relations(item_id, baseline_id=baseline_id, page=page, page_size=page_size)
        print("The response of TrackerItemApi->get_baseline_tracker_item_relations:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker item list |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_baseline_tracker_items_relations**
> List[TrackerItemRelationsResult] get_baseline_tracker_items_relations(tracker_items_request, baseline_id=baseline_id)

Get tracker items related to some tracker items

Use this endpoint to fetch tracker items related to some specified tracker items. The relations include downstream references, upstream references, incoming associations and outgoing associations of the given items. Relations with entities that are not tracker items (e.g., trackers, projects, URLs, etc.) will not be included in the result.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_relations_result import TrackerItemRelationsResult
from openapi_client.models.tracker_items_request import TrackerItemsRequest
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_items_request = openapi_client.TrackerItemsRequest() # TrackerItemsRequest | 
    baseline_id = 56 # int |  (optional)

    try:
        # Get tracker items related to some tracker items
        api_response = api_instance.get_baseline_tracker_items_relations(tracker_items_request, baseline_id=baseline_id)
        print("The response of TrackerItemApi->get_baseline_tracker_items_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->get_baseline_tracker_items_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_items_request** | [**TrackerItemsRequest**](TrackerItemsRequest.md)|  | 
 **baseline_id** | **int**|  | [optional] 

### Return type

[**List[TrackerItemRelationsResult]**](TrackerItemRelationsResult.md)

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

# **get_choice_options**
> ReferenceSearchResult get_choice_options(item_id, field_id, page=page, page_size=page_size)

Get the options of a choice field of tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.reference_search_result import ReferenceSearchResult
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    field_id = 56 # int | 
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Get the options of a choice field of tracker
        api_response = api_instance.get_choice_options(item_id, field_id, page=page, page_size=page_size)
        print("The response of TrackerItemApi->get_choice_options:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Options |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | No option found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_accessibility**
> TrackerItemFieldAccessibilityList get_item_accessibility(item_id, target_status_id=target_status_id)

Get a tracker item fields accessibility

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_field_accessibility_list import TrackerItemFieldAccessibilityList
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | Tracker item id
    target_status_id = 56 # int |  (optional)

    try:
        # Get a tracker item fields accessibility
        api_response = api_instance.get_item_accessibility(item_id, target_status_id=target_status_id)
        print("The response of TrackerItemApi->get_item_accessibility:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accessibility returned |  -  |
**401** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item**
> TrackerItem get_tracker_item(item_id, version=version, baseline_id=baseline_id)

Get basic tracker item

API can be used for fetching basic information of a tracker item

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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    version = 56 # int |  (optional)
    baseline_id = 56 # int |  (optional)

    try:
        # Get basic tracker item
        api_response = api_instance.get_tracker_item(item_id, version=version, baseline_id=baseline_id)
        print("The response of TrackerItemApi->get_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_fields**
> TrackerItemField get_tracker_item_fields(item_id)

Get fields of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_field import TrackerItemField
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 

    try:
        # Get fields of a tracker item
        api_response = api_instance.get_tracker_item_fields(item_id)
        print("The response of TrackerItemApi->get_tracker_item_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->get_tracker_item_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**TrackerItemField**](TrackerItemField.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fields of tracker item by id |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Item not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_history**
> TrackerItemHistory get_tracker_item_history(item_id)

Get tracker item history

API can be used for fetching basic information of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_history import TrackerItemHistory
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 

    try:
        # Get tracker item history
        api_response = api_instance.get_tracker_item_history(item_id)
        print("The response of TrackerItemApi->get_tracker_item_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->get_tracker_item_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**TrackerItemHistory**](TrackerItemHistory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_reviews**
> List[TrackerItemReview] get_tracker_item_reviews(item_id)

Get all Tracker Item Reviews for a particular Tracker Item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_review import TrackerItemReview
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 

    try:
        # Get all Tracker Item Reviews for a particular Tracker Item
        api_response = api_instance.get_tracker_item_reviews(item_id)
        print("The response of TrackerItemApi->get_tracker_item_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->get_tracker_item_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**List[TrackerItemReview]**](TrackerItemReview.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tracker item reviews for the particular item |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Tracker item reviews are disabled, or access to them is denied |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_transitions**
> List[WorkflowTransition] get_tracker_item_transitions(item_id)

Get available transitions for a tracker item

API can be used for getting available transitions for a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.workflow_transition import WorkflowTransition
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 

    try:
        # Get available transitions for a tracker item
        api_response = api_instance.get_tracker_item_transitions(item_id)
        print("The response of TrackerItemApi->get_tracker_item_transitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->get_tracker_item_transitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

[**List[WorkflowTransition]**](WorkflowTransition.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available transitions |  -  |
**401** | Authentication is required |  -  |
**403** | Missing user permissions |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_tracker_item**
> lock_tracker_item(item_id, lock_request)

Put a soft lock on a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.lock_request import LockRequest
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | Tracker item id
    lock_request = openapi_client.LockRequest() # LockRequest | 

    try:
        # Put a soft lock on a tracker item
        api_instance.lock_tracker_item(item_id, lock_request)
    except Exception as e:
        print("Exception when calling TrackerItemApi->lock_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lock acquired successfully |  -  |
**400** | Bad request, request validation error |  -  |
**401** | Authentication is required |  -  |
**403** | Could not acquire lock |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_children_of_tracker**
> TrackerItemChildReference patch_children_of_tracker(tracker_id, tracker_item_child_reference, mode=mode)

Patch the child item list of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_id = 56 # int | 
    tracker_item_child_reference = openapi_client.TrackerItemChildReference() # TrackerItemChildReference | 
    mode = 'INSERT' # str |  (optional) (default to 'INSERT')

    try:
        # Patch the child item list of a tracker item
        api_response = api_instance.patch_children_of_tracker(tracker_id, tracker_item_child_reference, mode=mode)
        print("The response of TrackerItemApi->patch_children_of_tracker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->patch_children_of_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **tracker_item_child_reference** | [**TrackerItemChildReference**](TrackerItemChildReference.md)|  | 
 **mode** | **str**|  | [optional] [default to &#39;INSERT&#39;]

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New child item reference on the requested index |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_children_of_tracker_item**
> TrackerItemChildReference patch_children_of_tracker_item(item_id, mode, tracker_item_child_reference)

Patch the child item list of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    mode = 'mode_example' # str | 
    tracker_item_child_reference = openapi_client.TrackerItemChildReference() # TrackerItemChildReference | 

    try:
        # Patch the child item list of a tracker item
        api_response = api_instance.patch_children_of_tracker_item(item_id, mode, tracker_item_child_reference)
        print("The response of TrackerItemApi->patch_children_of_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->patch_children_of_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **mode** | **str**|  | 
 **tracker_item_child_reference** | [**TrackerItemChildReference**](TrackerItemChildReference.md)|  | 

### Return type

[**TrackerItemChildReference**](TrackerItemChildReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New child item reference on the requested index |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_children_of_tracker**
> TrackerItemReferenceSearchResult replace_children_of_tracker(tracker_id, update_tracker_item_children_request, result_page_size=result_page_size)

Reorder the child item list of a tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
from openapi_client.models.update_tracker_item_children_request import UpdateTrackerItemChildrenRequest
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    tracker_id = 56 # int | 
    update_tracker_item_children_request = openapi_client.UpdateTrackerItemChildrenRequest() # UpdateTrackerItemChildrenRequest | 
    result_page_size = 25 # int | Number of items in the result page. Max value: 500 (optional) (default to 25)

    try:
        # Reorder the child item list of a tracker
        api_response = api_instance.replace_children_of_tracker(tracker_id, update_tracker_item_children_request, result_page_size=result_page_size)
        print("The response of TrackerItemApi->replace_children_of_tracker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->replace_children_of_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **update_tracker_item_children_request** | [**UpdateTrackerItemChildrenRequest**](UpdateTrackerItemChildrenRequest.md)|  | 
 **result_page_size** | **int**| Number of items in the result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemReferenceSearchResult**](TrackerItemReferenceSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | First page of the new child list |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_children_of_tracker_item**
> TrackerItemReferenceSearchResult replace_children_of_tracker_item(item_id, update_tracker_item_children_request, result_page_size=result_page_size)

Replace the child item list of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
from openapi_client.models.update_tracker_item_children_request import UpdateTrackerItemChildrenRequest
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    update_tracker_item_children_request = openapi_client.UpdateTrackerItemChildrenRequest() # UpdateTrackerItemChildrenRequest | 
    result_page_size = 25 # int | Number of items in the result page. Max value: 500 (optional) (default to 25)

    try:
        # Replace the child item list of a tracker item
        api_response = api_instance.replace_children_of_tracker_item(item_id, update_tracker_item_children_request, result_page_size=result_page_size)
        print("The response of TrackerItemApi->replace_children_of_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->replace_children_of_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **update_tracker_item_children_request** | [**UpdateTrackerItemChildrenRequest**](UpdateTrackerItemChildrenRequest.md)|  | 
 **result_page_size** | **int**| Number of items in the result page. Max value: 500 | [optional] [default to 25]

### Return type

[**TrackerItemReferenceSearchResult**](TrackerItemReferenceSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | First page of the new child list |  -  |
**400** | Invalid request |  -  |
**401** | Permission is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item is not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_tracker_item**
> unlock_tracker_item(item_id)

Unlock a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | Tracker item id

    try:
        # Unlock a tracker item
        api_instance.unlock_tracker_item(item_id)
    except Exception as e:
        print("Exception when calling TrackerItemApi->unlock_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Tracker item id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unlock successful |  -  |
**401** | Authentication is required |  -  |
**403** | Could not unlock |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_tracker_item**
> TrackerItem update_custom_field_tracker_item(item_id, update_tracker_item_field, quiet_mode=quiet_mode)

Update fields of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item import TrackerItem
from openapi_client.models.update_tracker_item_field import UpdateTrackerItemField
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    update_tracker_item_field = openapi_client.UpdateTrackerItemField() # UpdateTrackerItemField | 
    quiet_mode = False # bool | If it's turned on HTTP 200 with empty response indicates that the update was successful. (optional) (default to False)

    try:
        # Update fields of a tracker item
        api_response = api_instance.update_custom_field_tracker_item(item_id, update_tracker_item_field, quiet_mode=quiet_mode)
        print("The response of TrackerItemApi->update_custom_field_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->update_custom_field_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **update_tracker_item_field** | [**UpdateTrackerItemField**](UpdateTrackerItemField.md)|  | 
 **quiet_mode** | **bool**| If it&#39;s turned on HTTP 200 with empty response indicates that the update was successful. | [optional] [default to False]

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Field not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_field_tracker_item**
> TrackerItem update_table_field_tracker_item(item_id, table_field_id, update_tracker_item_table_field)

Update table field of tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item import TrackerItem
from openapi_client.models.update_tracker_item_table_field import UpdateTrackerItemTableField
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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    table_field_id = 56 # int | 
    update_tracker_item_table_field = openapi_client.UpdateTrackerItemTableField() # UpdateTrackerItemTableField | 

    try:
        # Update table field of tracker item
        api_response = api_instance.update_table_field_tracker_item(item_id, table_field_id, update_tracker_item_table_field)
        print("The response of TrackerItemApi->update_table_field_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->update_table_field_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **table_field_id** | **int**|  | 
 **update_tracker_item_table_field** | [**UpdateTrackerItemTableField**](UpdateTrackerItemTableField.md)|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Field not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_item**
> TrackerItem update_tracker_item(item_id, tracker_item, reference_item_id=reference_item_id, position=position)

Update tracker item

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
    api_instance = openapi_client.TrackerItemApi(api_client)
    item_id = 56 # int | 
    tracker_item = openapi_client.TrackerItem() # TrackerItem | 
    reference_item_id = 56 # int |  (optional)
    position = 'position_example' # str |  (optional)

    try:
        # Update tracker item
        api_response = api_instance.update_tracker_item(item_id, tracker_item, reference_item_id=reference_item_id, position=position)
        print("The response of TrackerItemApi->update_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemApi->update_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **tracker_item** | [**TrackerItem**](TrackerItem.md)|  | 
 **reference_item_id** | **int**|  | [optional] 
 **position** | **str**|  | [optional] 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Basic tracker item by id |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Field not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

