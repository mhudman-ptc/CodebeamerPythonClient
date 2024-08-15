# swagger_client.TraceabilityApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_traceability_initial_item_ids**](TraceabilityApi.md#get_traceability_initial_item_ids) | **POST** /v3/traceability/items | Get initial ids
[**get_traceability_level_item_ids**](TraceabilityApi.md#get_traceability_level_item_ids) | **POST** /v3/traceability/relations | Get traceability level item ids

# **get_traceability_initial_item_ids**
> list[TraceabilityItem] get_traceability_initial_item_ids(body, page_size=page_size, page_no=page_no)

Get initial ids

Get traceability initial ids!

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
api_instance = swagger_client.TraceabilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.TraceabilityInitialLevelFilter() # TraceabilityInitialLevelFilter | 
page_size = 56 # int | Number of items in a result page. (optional)
page_no = 56 # int | Index of the result page. (optional)

try:
    # Get initial ids
    api_response = api_instance.get_traceability_initial_item_ids(body, page_size=page_size, page_no=page_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TraceabilityApi->get_traceability_initial_item_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TraceabilityInitialLevelFilter**](TraceabilityInitialLevelFilter.md)|  | 
 **page_size** | **int**| Number of items in a result page. | [optional] 
 **page_no** | **int**| Index of the result page. | [optional] 

### Return type

[**list[TraceabilityItem]**](TraceabilityItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_traceability_level_item_ids**
> TraceabilityResult get_traceability_level_item_ids(body, items_on_level=items_on_level, items_from_previous_item=items_from_previous_item)

Get traceability level item ids

Get traceability item ids!

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
api_instance = swagger_client.TraceabilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.TraceabilityLevelFilter() # TraceabilityLevelFilter | 
items_on_level = 56 # int | Number of items per level. (optional)
items_from_previous_item = 56 # int | Number of items per item. (optional)

try:
    # Get traceability level item ids
    api_response = api_instance.get_traceability_level_item_ids(body, items_on_level=items_on_level, items_from_previous_item=items_from_previous_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TraceabilityApi->get_traceability_level_item_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TraceabilityLevelFilter**](TraceabilityLevelFilter.md)|  | 
 **items_on_level** | **int**| Number of items per level. | [optional] 
 **items_from_previous_item** | **int**| Number of items per item. | [optional] 

### Return type

[**TraceabilityResult**](TraceabilityResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

