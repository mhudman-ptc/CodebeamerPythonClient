# openapi_client.TestManagementApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_apply_step_reuses**](TestManagementApi.md#auto_apply_step_reuses) | **POST** /v3/testcases/autoApplyStepReuses | Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses


# **auto_apply_step_reuses**
> List[TrackerItemReference] auto_apply_step_reuses(auto_apply_test_step_reuses)

Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.auto_apply_test_step_reuses import AutoApplyTestStepReuses
from openapi_client.models.tracker_item_reference import TrackerItemReference
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
    api_instance = openapi_client.TestManagementApi(api_client)
    auto_apply_test_step_reuses = openapi_client.AutoApplyTestStepReuses() # AutoApplyTestStepReuses | 

    try:
        # Find duplicate TestSteps in a set of TestCases and converting duplicates to Reuses
        api_response = api_instance.auto_apply_step_reuses(auto_apply_test_step_reuses)
        print("The response of TestManagementApi->auto_apply_step_reuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestManagementApi->auto_apply_step_reuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_apply_test_step_reuses** | [**AutoApplyTestStepReuses**](AutoApplyTestStepReuses.md)|  | 

### Return type

[**List[TrackerItemReference]**](TrackerItemReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The item-references of the modified tracker-items where duplicate Test Steps was found and converted to Reuses |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

