# openapi_client.ExportApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_tracker_item_reviews**](ExportApi.md#batch_get_tracker_item_reviews) | **POST** /v3/export/tracker-item-reviews | Get tracker item reviews by a list of tracker item IDs
[**export**](ExportApi.md#export) | **POST** /v3/projects/{projectId}/content | Exports the specified project to a zip file
[**export_to_word**](ExportApi.md#export_to_word) | **POST** /v3/export/exportToWord | Exports items to Word
[**get_tracker_items**](ExportApi.md#get_tracker_items) | **POST** /v3/export/items | Get tracker items


# **batch_get_tracker_item_reviews**
> List[TrackerItemWithTrackerItemReviewsExport] batch_get_tracker_item_reviews(batch_get_tracker_item_reviews_request)

Get tracker item reviews by a list of tracker item IDs

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.batch_get_tracker_item_reviews_request import BatchGetTrackerItemReviewsRequest
from openapi_client.models.tracker_item_with_tracker_item_reviews_export import TrackerItemWithTrackerItemReviewsExport
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
    api_instance = openapi_client.ExportApi(api_client)
    batch_get_tracker_item_reviews_request = openapi_client.BatchGetTrackerItemReviewsRequest() # BatchGetTrackerItemReviewsRequest | 

    try:
        # Get tracker item reviews by a list of tracker item IDs
        api_response = api_instance.batch_get_tracker_item_reviews(batch_get_tracker_item_reviews_request)
        print("The response of ExportApi->batch_get_tracker_item_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->batch_get_tracker_item_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_get_tracker_item_reviews_request** | [**BatchGetTrackerItemReviewsRequest**](BatchGetTrackerItemReviewsRequest.md)|  | 

### Return type

[**List[TrackerItemWithTrackerItemReviewsExport]**](TrackerItemWithTrackerItemReviewsExport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tracker item reviews for each tracker item |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Tracker item reviews are disabled, or access to them is denied |  -  |
**404** | There is no baseline accessible with the supplied ID |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> bytearray export(project_id, export_project)

Exports the specified project to a zip file

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.export_project import ExportProject
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
    api_instance = openapi_client.ExportApi(api_client)
    project_id = 56 # int | 
    export_project = openapi_client.ExportProject() # ExportProject | 

    try:
        # Exports the specified project to a zip file
        api_response = api_instance.export(project_id, export_project)
        print("The response of ExportApi->export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **export_project** | [**ExportProject**](ExportProject.md)|  | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The exported project contents in a zip file. |  -  |
**400** | Bad request |  -  |
**403** | Authentication is required |  -  |
**404** | Project not found |  -  |
**429** | Too many requests |  -  |
**500** | Error during the project export |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_word**
> JobReference export_to_word(export_to_word_request)

Exports items to Word

API can be used for exporting items to Word

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.export_to_word_request import ExportToWordRequest
from openapi_client.models.job_reference import JobReference
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
    api_instance = openapi_client.ExportApi(api_client)
    export_to_word_request = openapi_client.ExportToWordRequest() # ExportToWordRequest | 

    try:
        # Exports items to Word
        api_response = api_instance.export_to_word(export_to_word_request)
        print("The response of ExportApi->export_to_word:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->export_to_word: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_to_word_request** | [**ExportToWordRequest**](ExportToWordRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | It returns a job reference. |  -  |
**400** | Invalid request |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_items**
> List[TrackerItem] get_tracker_items(tracker_items_request, baseline_id=baseline_id)

Get tracker items

API can be used for fetching basic information of tracker items

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item import TrackerItem
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
    api_instance = openapi_client.ExportApi(api_client)
    tracker_items_request = openapi_client.TrackerItemsRequest() # TrackerItemsRequest | 
    baseline_id = 56 # int |  (optional)

    try:
        # Get tracker items
        api_response = api_instance.get_tracker_items(tracker_items_request, baseline_id=baseline_id)
        print("The response of ExportApi->get_tracker_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->get_tracker_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_items_request** | [**TrackerItemsRequest**](TrackerItemsRequest.md)|  | 
 **baseline_id** | **int**|  | [optional] 

### Return type

[**List[TrackerItem]**](TrackerItem.md)

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

