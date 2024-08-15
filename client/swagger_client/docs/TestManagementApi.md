# swagger_client.TestManagementApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_apply_step_reuses**](TestManagementApi.md#auto_apply_step_reuses) | **POST** /v3/testcases/autoApplyStepReuses | Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses

# **auto_apply_step_reuses**
> list[TrackerItemReference] auto_apply_step_reuses(body)

Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses

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
api_instance = swagger_client.TestManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutoApplyTestStepReuses() # AutoApplyTestStepReuses | 

try:
    # Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses
    api_response = api_instance.auto_apply_step_reuses(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestManagementApi->auto_apply_step_reuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutoApplyTestStepReuses**](AutoApplyTestStepReuses.md)|  | 

### Return type

[**list[TrackerItemReference]**](TrackerItemReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

