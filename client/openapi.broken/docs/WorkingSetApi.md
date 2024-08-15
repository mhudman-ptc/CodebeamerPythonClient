# openapi_client.WorkingSetApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_mapping_in_working_set**](WorkingSetApi.md#get_items_mapping_in_working_set) | **POST** /v3/working-sets/items-mapping | Maps Tracker Items in Working-Set
[**get_tracker_working_sets**](WorkingSetApi.md#get_tracker_working_sets) | **GET** /v3/trackers/{trackerId}/working-sets | Lists Working-Sets
[**get_working_set_information**](WorkingSetApi.md#get_working_set_information) | **GET** /v3/working-sets/{workingSetId} | Working-Set information
[**get_working_set_trackers**](WorkingSetApi.md#get_working_set_trackers) | **GET** /v3/working-sets/{workingSetId}/trackers |  Lists the trackers in a Working-Set
[**list_working_sets_of_project**](WorkingSetApi.md#list_working_sets_of_project) | **GET** /v3/projects/{projectId}/working-sets | Project level Working-Sets information


# **get_items_mapping_in_working_set**
> List[WorkingSetItemMapping] get_items_mapping_in_working_set(working_set_items_mapping_request)

Maps Tracker Items in Working-Set

Maps Tracker Items to the corresponding Tracker Items in target Working-Set.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.working_set_item_mapping import WorkingSetItemMapping
from openapi_client.models.working_set_items_mapping_request import WorkingSetItemsMappingRequest
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
    api_instance = openapi_client.WorkingSetApi(api_client)
    working_set_items_mapping_request = openapi_client.WorkingSetItemsMappingRequest() # WorkingSetItemsMappingRequest | 

    try:
        # Maps Tracker Items in Working-Set
        api_response = api_instance.get_items_mapping_in_working_set(working_set_items_mapping_request)
        print("The response of WorkingSetApi->get_items_mapping_in_working_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingSetApi->get_items_mapping_in_working_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_set_items_mapping_request** | [**WorkingSetItemsMappingRequest**](WorkingSetItemsMappingRequest.md)|  | 

### Return type

[**List[WorkingSetItemMapping]**](WorkingSetItemMapping.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping of Tracker Items in target Working-Set |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_working_sets**
> List[TrackerWorkingSet] get_tracker_working_sets(tracker_id, include_deleted=include_deleted)

Lists Working-Sets

Lists Working-Sets that contain the given Tracker or Branch.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_working_set import TrackerWorkingSet
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
    api_instance = openapi_client.WorkingSetApi(api_client)
    tracker_id = 56 # int | Tracker or Branch id
    include_deleted = True # bool | Find Tracker or Branch if deleted and the result contains the deleted Working-Sets (optional)

    try:
        # Lists Working-Sets
        api_response = api_instance.get_tracker_working_sets(tracker_id, include_deleted=include_deleted)
        print("The response of WorkingSetApi->get_tracker_working_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingSetApi->get_tracker_working_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**| Tracker or Branch id | 
 **include_deleted** | **bool**| Find Tracker or Branch if deleted and the result contains the deleted Working-Sets | [optional] 

### Return type

[**List[TrackerWorkingSet]**](TrackerWorkingSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Working-Sets that contain the given tracker. |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_working_set_information**
> WorkingSetInformation get_working_set_information(working_set_id, include_deleted=include_deleted)

Working-Set information

Gets the Working-Set information for the given id.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.working_set_information import WorkingSetInformation
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
    api_instance = openapi_client.WorkingSetApi(api_client)
    working_set_id = 56 # int | Id of the Working-Set
    include_deleted = True # bool | The result contains the deleted Working-Sets (optional)

    try:
        # Working-Set information
        api_response = api_instance.get_working_set_information(working_set_id, include_deleted=include_deleted)
        print("The response of WorkingSetApi->get_working_set_information:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Working-Set information |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_working_set_trackers**
> List[WorkingSetTracker] get_working_set_trackers(working_set_id, include_deleted=include_deleted)

 Lists the trackers in a Working-Set

Lists the trackers (shared and included) in the given Working-Set.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.working_set_tracker import WorkingSetTracker
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
    api_instance = openapi_client.WorkingSetApi(api_client)
    working_set_id = 56 # int | Working-Set id
    include_deleted = True # bool | The result contains the deleted Trackers (optional)

    try:
        #  Lists the trackers in a Working-Set
        api_response = api_instance.get_working_set_trackers(working_set_id, include_deleted=include_deleted)
        print("The response of WorkingSetApi->get_working_set_trackers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingSetApi->get_working_set_trackers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_set_id** | **int**| Working-Set id | 
 **include_deleted** | **bool**| The result contains the deleted Trackers | [optional] 

### Return type

[**List[WorkingSetTracker]**](WorkingSetTracker.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of trackers |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_working_sets_of_project**
> List[WorkingSetMinimal] list_working_sets_of_project(project_id, include_deleted=include_deleted)

Project level Working-Sets information

Lists top-level Working-Sets minimal information for the given project.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.working_set_minimal import WorkingSetMinimal
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
    api_instance = openapi_client.WorkingSetApi(api_client)
    project_id = 56 # int | The id of the project
    include_deleted = True # bool | The result lists the deleted Working-Sets (optional)

    try:
        # Project level Working-Sets information
        api_response = api_instance.list_working_sets_of_project(project_id, include_deleted=include_deleted)
        print("The response of WorkingSetApi->list_working_sets_of_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkingSetApi->list_working_sets_of_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The id of the project | 
 **include_deleted** | **bool**| The result lists the deleted Working-Sets | [optional] 

### Return type

[**List[WorkingSetMinimal]**](WorkingSetMinimal.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of top-level Working-Set |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Resource not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

