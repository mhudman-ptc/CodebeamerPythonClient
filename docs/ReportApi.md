# swagger_client.ReportApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportApi.md#create_report) | **POST** /v3/reports | Create a report
[**get_report_by_id**](ReportApi.md#get_report_by_id) | **GET** /v3/reports/{reportId}/results | Get a report results by id of the report
[**get_report_items_by_id**](ReportApi.md#get_report_items_by_id) | **GET** /v3/reports/{reportId}/items | Get a report items by id of the report
[**update_report**](ReportApi.md#update_report) | **PUT** /v3/reports/{reportId} | Update report settings

# **create_report**
> SimpleReportSettings create_report(body)

Create a report

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimpleReportSettings() # SimpleReportSettings | 

try:
    # Create a report
    api_response = api_instance.create_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleReportSettings**](SimpleReportSettings.md)|  | 

### Return type

[**SimpleReportSettings**](SimpleReportSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_id**
> ReportResult get_report_by_id(report_id, page=page, page_size=page_size)

Get a report results by id of the report

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
report_id = 56 # int | Id of a report
page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items a report page. Max value: 500 (optional) (default to 25)

try:
    # Get a report results by id of the report
    api_response = api_instance.get_report_by_id(report_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| Id of a report | 
 **page** | **int**| Index of a report page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items a report page. Max value: 500 | [optional] [default to 25]

### Return type

[**ReportResult**](ReportResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_items_by_id**
> ReportItemResult get_report_items_by_id(report_id, page=page, page_size=page_size)

Get a report items by id of the report

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
report_id = 56 # int | Id of a report
page = 1 # int | Index of a report page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items a report page. Max value: 500 (optional) (default to 25)

try:
    # Get a report items by id of the report
    api_response = api_instance.get_report_items_by_id(report_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report_items_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| Id of a report | 
 **page** | **int**| Index of a report page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items a report page. Max value: 500 | [optional] [default to 25]

### Return type

[**ReportItemResult**](ReportItemResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report**
> SimpleReportSettings update_report(body, report_id)

Update report settings

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
api_instance = swagger_client.ReportApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimpleReportSettings() # SimpleReportSettings | 
report_id = 56 # int | Id of a report

try:
    # Update report settings
    api_response = api_instance.update_report(body, report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->update_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleReportSettings**](SimpleReportSettings.md)|  | 
 **report_id** | **int**| Id of a report | 

### Return type

[**SimpleReportSettings**](SimpleReportSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

