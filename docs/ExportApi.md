# swagger_client.ExportApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_get_tracker_item_reviews**](ExportApi.md#batch_get_tracker_item_reviews) | **POST** /v3/export/tracker-item-reviews | Get tracker item reviews by a list of tracker item IDs
[**export**](ExportApi.md#export) | **POST** /v3/projects/{projectId}/content | Exports the specified project to a zip file
[**export_to_word**](ExportApi.md#export_to_word) | **POST** /v3/export/exportToWord | Exports items to Word
[**get_tracker_items**](ExportApi.md#get_tracker_items) | **POST** /v3/export/items | Get tracker items

# **batch_get_tracker_item_reviews**
> list[TrackerItemWithTrackerItemReviewsExport] batch_get_tracker_item_reviews(body)

Get tracker item reviews by a list of tracker item IDs

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
api_instance = swagger_client.ExportApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchGetTrackerItemReviewsRequest() # BatchGetTrackerItemReviewsRequest | 

try:
    # Get tracker item reviews by a list of tracker item IDs
    api_response = api_instance.batch_get_tracker_item_reviews(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->batch_get_tracker_item_reviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchGetTrackerItemReviewsRequest**](BatchGetTrackerItemReviewsRequest.md)|  | 

### Return type

[**list[TrackerItemWithTrackerItemReviewsExport]**](TrackerItemWithTrackerItemReviewsExport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> str export(body, project_id)

Exports the specified project to a zip file

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
api_instance = swagger_client.ExportApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExportProject() # ExportProject | 
project_id = 56 # int | 

try:
    # Exports the specified project to a zip file
    api_response = api_instance.export(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportProject**](ExportProject.md)|  | 
 **project_id** | **int**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_word**
> JobReference export_to_word(body)

Exports items to Word

API can be used for exporting items to Word

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
api_instance = swagger_client.ExportApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExportToWordRequest() # ExportToWordRequest | 

try:
    # Exports items to Word
    api_response = api_instance.export_to_word(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->export_to_word: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportToWordRequest**](ExportToWordRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_items**
> list[TrackerItem] get_tracker_items(body, baseline_id=baseline_id)

Get tracker items

API can be used for fetching basic information of tracker items

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
api_instance = swagger_client.ExportApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemsRequest() # TrackerItemsRequest | 
baseline_id = 56 # int |  (optional)

try:
    # Get tracker items
    api_response = api_instance.get_tracker_items(body, baseline_id=baseline_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_tracker_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemsRequest**](TrackerItemsRequest.md)|  | 
 **baseline_id** | **int**|  | [optional] 

### Return type

[**list[TrackerItem]**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

