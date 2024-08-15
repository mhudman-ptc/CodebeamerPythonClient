# swagger_client.TrackerItemMoveApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_move_field_mapping**](TrackerItemMoveApi.md#get_item_move_field_mapping) | **GET** /v3/items/move/field-mapping | Gets the default field mapping between two trackers
[**move_tracker_items**](TrackerItemMoveApi.md#move_tracker_items) | **POST** /v3/items/move | Move Tracker Items from the Source Tracker to the Target Tracker

# **get_item_move_field_mapping**
> TrackerItemFieldMappingInfo get_item_move_field_mapping(source_tracker_id, target_tracker_id)

Gets the default field mapping between two trackers

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
api_instance = swagger_client.TrackerItemMoveApi(swagger_client.ApiClient(configuration))
source_tracker_id = 56 # int | The id of the source Tracker
target_tracker_id = 56 # int | The id of the target Tracker

try:
    # Gets the default field mapping between two trackers
    api_response = api_instance.get_item_move_field_mapping(source_tracker_id, target_tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemMoveApi->get_item_move_field_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_tracker_id** | **int**| The id of the source Tracker | 
 **target_tracker_id** | **int**| The id of the target Tracker | 

### Return type

[**TrackerItemFieldMappingInfo**](TrackerItemFieldMappingInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_tracker_items**
> JobReference move_tracker_items(body)

Move Tracker Items from the Source Tracker to the Target Tracker

Move Tracker Items from the Source Tracker to the Target Tracker. The items are optional, if it is not provided all the Tracker Items will be moved from the Source Tracker. All the fields from the Source Tracker must be in the mapping. If you want to ignore one you set the targetField to null in the request.

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
api_instance = swagger_client.TrackerItemMoveApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemMoveRequest() # TrackerItemMoveRequest | 

try:
    # Move Tracker Items from the Source Tracker to the Target Tracker
    api_response = api_instance.move_tracker_items(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemMoveApi->move_tracker_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemMoveRequest**](TrackerItemMoveRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

