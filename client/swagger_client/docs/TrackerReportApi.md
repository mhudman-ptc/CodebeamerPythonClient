# swagger_client.TrackerReportApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tracker_report**](TrackerReportApi.md#create_tracker_report) | **POST** /v3/trackers/{trackerId}/reports | Creates a report of a specific tracker
[**delete_tracker_report**](TrackerReportApi.md#delete_tracker_report) | **DELETE** /v3/trackers/{trackerId}/reports/{reportId} | Deletes a report of a specific tracker
[**get_tracker_report**](TrackerReportApi.md#get_tracker_report) | **GET** /v3/trackers/{trackerId}/reports/{reportId}/results | Get a report of a specific tracker
[**get_tracker_report_items**](TrackerReportApi.md#get_tracker_report_items) | **GET** /v3/trackers/{trackerId}/reports/{reportId}/items | Get report items of a specific tracker view
[**get_tracker_reports**](TrackerReportApi.md#get_tracker_reports) | **GET** /v3/trackers/{trackerId}/reports | Get all reports of a specific tracker
[**update_tracker_report**](TrackerReportApi.md#update_tracker_report) | **PUT** /v3/trackers/{trackerId}/reports/{reportId} | Updates a report of a specific tracker

# **create_tracker_report**
> TrackerReportSettings create_tracker_report(body, tracker_id)

Creates a report of a specific tracker

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerReportSettings() # TrackerReportSettings | 
tracker_id = 56 # int | 

try:
    # Creates a report of a specific tracker
    api_response = api_instance.create_tracker_report(body, tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerReportApi->create_tracker_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerReportSettings**](TrackerReportSettings.md)|  | 
 **tracker_id** | **int**|  | 

### Return type

[**TrackerReportSettings**](TrackerReportSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_report**
> delete_tracker_report(tracker_id, report_id)

Deletes a report of a specific tracker

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
report_id = 56 # int | 

try:
    # Deletes a report of a specific tracker
    api_instance.delete_tracker_report(tracker_id, report_id)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_report**
> ReportResult get_tracker_report(tracker_id, report_id, page=page, page_size=page_size)

Get a report of a specific tracker

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
report_id = 56 # int | 
page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items a report page. Max value: 500 (optional) (default to 25)

try:
    # Get a report of a specific tracker
    api_response = api_instance.get_tracker_report(tracker_id, report_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_report_items**
> ReportItemResult get_tracker_report_items(tracker_id, report_id, page=page, page_size=page_size)

Get report items of a specific tracker view

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
report_id = 56 # int | 
page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
page_size = 20 # int | Number of items a report page. Max value: 500 (optional) (default to 20)

try:
    # Get report items of a specific tracker view
    api_response = api_instance.get_tracker_report_items(tracker_id, report_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_reports**
> list[ReportReference] get_tracker_reports(tracker_id)

Get all reports of a specific tracker

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 

try:
    # Get all reports of a specific tracker
    api_response = api_instance.get_tracker_reports(tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerReportApi->get_tracker_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 

### Return type

[**list[ReportReference]**](ReportReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracker_report**
> TrackerReportSettings update_tracker_report(body, tracker_id, report_id)

Updates a report of a specific tracker

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
api_instance = swagger_client.TrackerReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerReportSettings() # TrackerReportSettings | 
tracker_id = 56 # int | 
report_id = 56 # int | 

try:
    # Updates a report of a specific tracker
    api_response = api_instance.update_tracker_report(body, tracker_id, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerReportApi->update_tracker_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerReportSettings**](TrackerReportSettings.md)|  | 
 **tracker_id** | **int**|  | 
 **report_id** | **int**|  | 

### Return type

[**TrackerReportSettings**](TrackerReportSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

