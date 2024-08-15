# swagger_client.BaselineApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_baseline**](BaselineApi.md#create_baseline) | **POST** /v3/baselines | Create a project or tracker baseline

# **create_baseline**
> Baseline create_baseline(body)

Create a project or tracker baseline

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
api_instance = swagger_client.BaselineApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateBaselineRequest() # CreateBaselineRequest | 

try:
    # Create a project or tracker baseline
    api_response = api_instance.create_baseline(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BaselineApi->create_baseline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBaselineRequest**](CreateBaselineRequest.md)|  | 

### Return type

[**Baseline**](Baseline.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

