# openapi_client.TestRunApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_run_for_test_case**](TestRunApi.md#create_test_run_for_test_case) | **POST** /v3/trackers/{testRunTrackerId}/testruns | Create a new test run for test cases or test sets
[**create_test_run_for_test_sets**](TestRunApi.md#create_test_run_for_test_sets) | **POST** /v3/trackers/{testRunTrackerId}/testruns/generatefromtestset | Create a new test run for test cases or test sets
[**update_test_run_result**](TestRunApi.md#update_test_run_result) | **PUT** /v3/testruns/{testRunId} | Update result of a Test Run. 
[**upload_automated_test_results**](TestRunApi.md#upload_automated_test_results) | **POST** /v3/trackers/{testRunTrackerId}/automatedtestruns | Create a new test run for large number of automated test cases


# **create_test_run_for_test_case**
> TrackerItem create_test_run_for_test_case(test_run_tracker_id, create_test_run_request)

Create a new test run for test cases or test sets

For multiple test sets please use trackers/{testRunTrackerId}/testruns/generatefromtestset endpoint.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_test_run_request import CreateTestRunRequest
from openapi_client.models.tracker_item import TrackerItem
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
    api_instance = openapi_client.TestRunApi(api_client)
    test_run_tracker_id = 56 # int | 
    create_test_run_request = openapi_client.CreateTestRunRequest() # CreateTestRunRequest | 

    try:
        # Create a new test run for test cases or test sets
        api_response = api_instance.create_test_run_for_test_case(test_run_tracker_id, create_test_run_request)
        print("The response of TestRunApi->create_test_run_for_test_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestRunApi->create_test_run_for_test_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_tracker_id** | **int**|  | 
 **create_test_run_request** | [**CreateTestRunRequest**](CreateTestRunRequest.md)|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created test run |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_run_for_test_sets**
> TestRunResult create_test_run_for_test_sets(test_run_tracker_id, create_test_run_from_test_sets_request)

Create a new test run for test cases or test sets

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.create_test_run_from_test_sets_request import CreateTestRunFromTestSetsRequest
from openapi_client.models.test_run_result import TestRunResult
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
    api_instance = openapi_client.TestRunApi(api_client)
    test_run_tracker_id = 56 # int | 
    create_test_run_from_test_sets_request = openapi_client.CreateTestRunFromTestSetsRequest() # CreateTestRunFromTestSetsRequest | 

    try:
        # Create a new test run for test cases or test sets
        api_response = api_instance.create_test_run_for_test_sets(test_run_tracker_id, create_test_run_from_test_sets_request)
        print("The response of TestRunApi->create_test_run_for_test_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestRunApi->create_test_run_for_test_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_tracker_id** | **int**|  | 
 **create_test_run_from_test_sets_request** | [**CreateTestRunFromTestSetsRequest**](CreateTestRunFromTestSetsRequest.md)|  | 

### Return type

[**TestRunResult**](TestRunResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created test run |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Tracker is not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_run_result**
> TrackerItem update_test_run_result(test_run_id, update_test_run_request)

Update result of a Test Run. 

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item import TrackerItem
from openapi_client.models.update_test_run_request import UpdateTestRunRequest
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
    api_instance = openapi_client.TestRunApi(api_client)
    test_run_id = 56 # int | 
    update_test_run_request = openapi_client.UpdateTestRunRequest() # UpdateTestRunRequest | 

    try:
        # Update result of a Test Run. 
        api_response = api_instance.update_test_run_result(test_run_id, update_test_run_request)
        print("The response of TestRunApi->update_test_run_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestRunApi->update_test_run_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **int**|  | 
 **update_test_run_request** | [**UpdateTestRunRequest**](UpdateTestRunRequest.md)|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Test Run item |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | Test run not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_automated_test_results**
> TrackerItem upload_automated_test_results(test_run_tracker_id, automated_test_run_request)

Create a new test run for large number of automated test cases

Upload large amount of automated test case run results into a single test run. This process may take a while, please check your proxy settings to prevent timeout.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.automated_test_run_request import AutomatedTestRunRequest
from openapi_client.models.tracker_item import TrackerItem
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
    api_instance = openapi_client.TestRunApi(api_client)
    test_run_tracker_id = 56 # int | 
    automated_test_run_request = openapi_client.AutomatedTestRunRequest() # AutomatedTestRunRequest | 

    try:
        # Create a new test run for large number of automated test cases
        api_response = api_instance.upload_automated_test_results(test_run_tracker_id, automated_test_run_request)
        print("The response of TestRunApi->upload_automated_test_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestRunApi->upload_automated_test_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_tracker_id** | **int**|  | 
 **automated_test_run_request** | [**AutomatedTestRunRequest**](AutomatedTestRunRequest.md)|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created test run |  -  |
**400** | Bad request |  -  |
**401** | Authorization is required |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

