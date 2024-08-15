# swagger_client.SystemApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_status**](SystemApi.md#get_system_status) | **GET** /v3/system/maintenance | Get system maintenance status
[**set_system_status**](SystemApi.md#set_system_status) | **PUT** /v3/system/maintenance | Set system maintenance status

# **get_system_status**
> SystemStatus get_system_status()

Get system maintenance status

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))

try:
    # Get system maintenance status
    api_response = api_instance.get_system_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStatus**](SystemStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_system_status**
> SystemStatus set_system_status(body)

Set system maintenance status

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
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(configuration))
body = swagger_client.MaintenanceMode() # MaintenanceMode | 

try:
    # Set system maintenance status
    api_response = api_instance.set_system_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->set_system_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceMode**](MaintenanceMode.md)|  | 

### Return type

[**SystemStatus**](SystemStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

