# openapi_client.BaselineApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_baseline**](BaselineApi.md#create_baseline) | **POST** /v3/baselines | Create a project or tracker baseline


# **create_baseline**
> Baseline create_baseline(create_baseline_request)

Create a project or tracker baseline

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.baseline import Baseline
from openapi_client.models.create_baseline_request import CreateBaselineRequest
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
    api_instance = openapi_client.BaselineApi(api_client)
    create_baseline_request = openapi_client.CreateBaselineRequest() # CreateBaselineRequest | 

    try:
        # Create a project or tracker baseline
        api_response = api_instance.create_baseline(create_baseline_request)
        print("The response of BaselineApi->create_baseline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaselineApi->create_baseline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_baseline_request** | [**CreateBaselineRequest**](CreateBaselineRequest.md)|  | 

### Return type

[**Baseline**](Baseline.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Baseline created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required or user has no permission |  -  |
**404** | Project or tracker not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

