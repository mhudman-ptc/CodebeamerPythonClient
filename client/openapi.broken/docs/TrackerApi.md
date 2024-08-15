# openapi_client.TrackerApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Deletes a tracker
        api_instance.delete_tracker(tracker_id)
    except Exception as e:
        print("Exception when calling TrackerApi->delete_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker deleted. |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_choice_option**
> ChoiceOptionReference get_choice_option(tracker_id, field_id, option_id)

Get option of a choice field of tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.choice_option_reference import ChoiceOptionReference
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    field_id = 56 # int | 
    option_id = 56 # int | 

    try:
        # Get option of a choice field of tracker
        api_response = api_instance.get_choice_option(tracker_id, field_id, option_id)
        print("The response of TrackerApi->get_choice_option:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option by id |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Option not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_by_tracker**
> TrackerItemReferenceSearchResult get_items_by_tracker(tracker_id, page=page, page_size=page_size)

Get items in a specific tracker

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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Get items in a specific tracker
        api_response = api_instance.get_items_by_tracker(tracker_id, page=page, page_size=page_size)
        print("The response of TrackerApi->get_items_by_tracker:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tracker items |  -  |
**400** | Request cannot be processed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker**
> Tracker get_tracker(tracker_id)

Get tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker import Tracker
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get tracker
        api_response = api_instance.get_tracker(tracker_id)
        print("The response of TrackerApi->get_tracker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**Tracker**](Tracker.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker |  -  |
**403** | Authentication is required |  -  |
**404** | Project / Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_baselines**
> ReferenceSearchResult get_tracker_baselines(tracker_id)

Get baselines of a specific tracker

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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get baselines of a specific tracker
        api_response = api_instance.get_tracker_baselines(tracker_id)
        print("The response of TrackerApi->get_tracker_baselines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_baselines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**ReferenceSearchResult**](ReferenceSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Baselines of the tracker |  -  |
**401** | Not authorized |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_configuration**
> TrackerConfiguration get_tracker_configuration(tracker_id)

Get tracker configuration

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_configuration import TrackerConfiguration
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get tracker configuration
        api_response = api_instance.get_tracker_configuration(tracker_id)
        print("The response of TrackerApi->get_tracker_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**TrackerConfiguration**](TrackerConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker configuration |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |
**500** | Failed to retrieve the Tracker |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_field**
> AbstractField get_tracker_field(tracker_id, field_id)

Get field of tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.abstract_field import AbstractField
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    field_id = 56 # int | 

    try:
        # Get field of tracker
        api_response = api_instance.get_tracker_field(tracker_id, field_id)
        print("The response of TrackerApi->get_tracker_field:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Field by id |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Field not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_field_permissions**
> List[TrackerFieldStatusPermissions] get_tracker_field_permissions(tracker_id, field_id, status_id=status_id)

Get permissions of tracker field

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_field_status_permissions import TrackerFieldStatusPermissions
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    field_id = 56 # int | 
    status_id = 56 # int |  (optional)

    try:
        # Get permissions of tracker field
        api_response = api_instance.get_tracker_field_permissions(tracker_id, field_id, status_id=status_id)
        print("The response of TrackerApi->get_tracker_field_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_field_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **field_id** | **int**|  | 
 **status_id** | **int**|  | [optional] 

### Return type

[**List[TrackerFieldStatusPermissions]**](TrackerFieldStatusPermissions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions by status and role |  -  |
**400** | Status id is invalid |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Tracker or field not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_fields**
> List[FieldReference] get_tracker_fields(tracker_id)

Get fields of tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.field_reference import FieldReference
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get fields of tracker
        api_response = api_instance.get_tracker_fields(tracker_id)
        print("The response of TrackerApi->get_tracker_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**List[FieldReference]**](FieldReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Field references |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Field not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_fields_permissions**
> TrackerFieldsStatusPermissions get_tracker_fields_permissions(tracker_id, status_id=status_id)

Get permissions of all fields of a tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_fields_status_permissions import TrackerFieldsStatusPermissions
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    status_id = 56 # int |  (optional)

    try:
        # Get permissions of all fields of a tracker
        api_response = api_instance.get_tracker_fields_permissions(tracker_id, status_id=status_id)
        print("The response of TrackerApi->get_tracker_fields_permissions:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions by status and role |  -  |
**400** | Status id is invalid |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_outline**
> OutlineItemSearchResult get_tracker_outline(tracker_id, parent_item_id=parent_item_id, result_depth_filter=result_depth_filter)

Get outline of a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.outline_item_search_result import OutlineItemSearchResult
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    parent_item_id = 56 # int | Show only the children of this item. (optional)
    result_depth_filter = 56 # int | The depth level of the result outline. (optional)

    try:
        # Get outline of a specific tracker
        api_response = api_instance.get_tracker_outline(tracker_id, parent_item_id=parent_item_id, result_depth_filter=result_depth_filter)
        print("The response of TrackerApi->get_tracker_outline:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Outline of the tracker |  -  |
**400** | Request cannot be processed |  -  |
**401** | Not authorized |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_schema**
> List[AbstractField] get_tracker_schema(tracker_id)

Get the schema of a tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.abstract_field import AbstractField
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get the schema of a tracker
        api_response = api_instance.get_tracker_schema(tracker_id)
        print("The response of TrackerApi->get_tracker_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**List[AbstractField]**](AbstractField.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Field definitions |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**404** | Field not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_transitions**
> List[WorkflowTransition] get_tracker_transitions(tracker_id, from_status_id=from_status_id)

Get all transitions of a specific tracker

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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    from_status_id = 56 # int | The from status id filter for transitions. (optional)

    try:
        # Get all transitions of a specific tracker
        api_response = api_instance.get_tracker_transitions(tracker_id, from_status_id=from_status_id)
        print("The response of TrackerApi->get_tracker_transitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_transitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **from_status_id** | **int**| The from status id filter for transitions. | [optional] 

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
**200** | Tracker transition list |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_type**
> TrackerType get_tracker_type(tracker_type_id)

Get the immutable definition of a tracker type

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_type import TrackerType
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_type_id = 56 # int | 

    try:
        # Get the immutable definition of a tracker type
        api_response = api_instance.get_tracker_type(tracker_type_id)
        print("The response of TrackerApi->get_tracker_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_type_id** | **int**|  | 

### Return type

[**TrackerType**](TrackerType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker type |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker type is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_types**
> List[TrackerTypeReference] get_tracker_types(outline=outline)

Get the list of tracker types

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_type_reference import TrackerTypeReference
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
    api_instance = openapi_client.TrackerApi(api_client)
    outline = 'ANY' # str | Outline is enabled, disabled or any(no filtering will be applied). (optional) (default to 'ANY')

    try:
        # Get the list of tracker types
        api_response = api_instance.get_tracker_types(outline=outline)
        print("The response of TrackerApi->get_tracker_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->get_tracker_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outline** | **str**| Outline is enabled, disabled or any(no filtering will be applied). | [optional] [default to &#39;ANY&#39;]

### Return type

[**List[TrackerTypeReference]**](TrackerTypeReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker types |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tracker_configuration**
> TrackerConfiguration post_tracker_configuration(tracker_configuration)

Create or update tracker configuration

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_configuration import TrackerConfiguration
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_configuration = openapi_client.TrackerConfiguration() # TrackerConfiguration | 

    try:
        # Create or update tracker configuration
        api_response = api_instance.post_tracker_configuration(tracker_configuration)
        print("The response of TrackerApi->post_tracker_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->post_tracker_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_configuration** | [**TrackerConfiguration**](TrackerConfiguration.md)|  | 

### Return type

[**TrackerConfiguration**](TrackerConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker configuration saved |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**422** | Invalid tracker configuration |  -  |
**429** | Too many requests |  -  |
**500** | Tracker update failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker**
> Tracker update_tracker(tracker_id, tracker)

Updates a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker import Tracker
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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | 
    tracker = openapi_client.Tracker() # Tracker | 

    try:
        # Updates a specific tracker
        api_response = api_instance.update_tracker(tracker_id, tracker)
        print("The response of TrackerApi->update_tracker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerApi->update_tracker: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **tracker** | [**Tracker**](Tracker.md)|  | 

### Return type

[**Tracker**](Tracker.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker settings |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_icon**
> update_tracker_icon(tracker_id, icon)

Upload a tracker icon

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
    api_instance = openapi_client.TrackerApi(api_client)
    tracker_id = 56 # int | Id of the tracker
    icon = None # bytearray | Icon image file

    try:
        # Upload a tracker icon
        api_instance.update_tracker_icon(tracker_id, icon)
    except Exception as e:
        print("Exception when calling TrackerApi->update_tracker_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**| Id of the tracker | 
 **icon** | **bytearray**| Icon image file | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker icon uploaded successfully |  -  |
**400** | Could not read image from the request, or it&#39;s the wrong format |  -  |
**401** | Authentication is required |  -  |
**403** | The tracker could not be accessed |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

