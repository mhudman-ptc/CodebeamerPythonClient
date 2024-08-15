# openapi_client.TrackerReportApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tracker_report**](TrackerReportApi.md#create_tracker_report) | **POST** /v3/trackers/{trackerId}/reports | Creates a report of a specific tracker
[**delete_tracker_report**](TrackerReportApi.md#delete_tracker_report) | **DELETE** /v3/trackers/{trackerId}/reports/{reportId} | Deletes a report of a specific tracker
[**get_tracker_report**](TrackerReportApi.md#get_tracker_report) | **GET** /v3/trackers/{trackerId}/reports/{reportId}/results | Get a report of a specific tracker
[**get_tracker_report_items**](TrackerReportApi.md#get_tracker_report_items) | **GET** /v3/trackers/{trackerId}/reports/{reportId}/items | Get report items of a specific tracker view
[**get_tracker_reports**](TrackerReportApi.md#get_tracker_reports) | **GET** /v3/trackers/{trackerId}/reports | Get all reports of a specific tracker
[**update_tracker_report**](TrackerReportApi.md#update_tracker_report) | **PUT** /v3/trackers/{trackerId}/reports/{reportId} | Updates a report of a specific tracker


# **create_tracker_report**
> TrackerReportSettings create_tracker_report(tracker_id, tracker_report_settings)

Creates a report of a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_report_settings import TrackerReportSettings
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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 
    tracker_report_settings = openapi_client.TrackerReportSettings() # TrackerReportSettings | 

    try:
        # Creates a report of a specific tracker
        api_response = api_instance.create_tracker_report(tracker_id, tracker_report_settings)
        print("The response of TrackerReportApi->create_tracker_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportApi->create_tracker_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **tracker_report_settings** | [**TrackerReportSettings**](TrackerReportSettings.md)|  | 

### Return type

[**TrackerReportSettings**](TrackerReportSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker report settings |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_report**
> delete_tracker_report(tracker_id, report_id)

Deletes a report of a specific tracker

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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 
    report_id = 56 # int | 

    try:
        # Deletes a report of a specific tracker
        api_instance.delete_tracker_report(tracker_id, report_id)
    except Exception as e:
        print("Exception when calling TrackerReportApi->delete_tracker_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **report_id** | **int**|  | 

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
**200** | Tracker report deleted. |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Report not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_report**
> ReportResult get_tracker_report(tracker_id, report_id, page=page, page_size=page_size)

Get a report of a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.report_result import ReportResult
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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 
    report_id = 56 # int | 
    page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items a report page. Max value: 500 (optional) (default to 25)

    try:
        # Get a report of a specific tracker
        api_response = api_instance.get_tracker_report(tracker_id, report_id, page=page, page_size=page_size)
        print("The response of TrackerReportApi->get_tracker_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportApi->get_tracker_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **report_id** | **int**|  | 
 **page** | **int**| Index of a report page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items a report page. Max value: 500 | [optional] [default to 25]

### Return type

[**ReportResult**](ReportResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker report |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Report not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_report_items**
> ReportItemResult get_tracker_report_items(tracker_id, report_id, page=page, page_size=page_size)

Get report items of a specific tracker view

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.report_item_result import ReportItemResult
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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 
    report_id = 56 # int | 
    page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
    page_size = 20 # int | Number of items a report page. Max value: 500 (optional) (default to 20)

    try:
        # Get report items of a specific tracker view
        api_response = api_instance.get_tracker_report_items(tracker_id, report_id, page=page, page_size=page_size)
        print("The response of TrackerReportApi->get_tracker_report_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportApi->get_tracker_report_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **report_id** | **int**|  | 
 **page** | **int**| Index of a report page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items a report page. Max value: 500 | [optional] [default to 20]

### Return type

[**ReportItemResult**](ReportItemResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker report items |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Report not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_reports**
> List[ReportReference] get_tracker_reports(tracker_id)

Get all reports of a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.report_reference import ReportReference
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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 

    try:
        # Get all reports of a specific tracker
        api_response = api_instance.get_tracker_reports(tracker_id)
        print("The response of TrackerReportApi->get_tracker_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportApi->get_tracker_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**List[ReportReference]**](ReportReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker report reference list |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_report**
> TrackerReportSettings update_tracker_report(tracker_id, report_id, tracker_report_settings)

Updates a report of a specific tracker

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_report_settings import TrackerReportSettings
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
    api_instance = openapi_client.TrackerReportApi(api_client)
    tracker_id = 56 # int | 
    report_id = 56 # int | 
    tracker_report_settings = openapi_client.TrackerReportSettings() # TrackerReportSettings | 

    try:
        # Updates a report of a specific tracker
        api_response = api_instance.update_tracker_report(tracker_id, report_id, tracker_report_settings)
        print("The response of TrackerReportApi->update_tracker_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerReportApi->update_tracker_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **report_id** | **int**|  | 
 **tracker_report_settings** | [**TrackerReportSettings**](TrackerReportSettings.md)|  | 

### Return type

[**TrackerReportSettings**](TrackerReportSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker report settings |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Report not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

