# swagger_client.TestRunApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_run_for_test_case**](TestRunApi.md#create_test_run_for_test_case) | **POST** /v3/trackers/{testRunTrackerId}/testruns | Create a new test run for test cases or test sets
[**create_test_run_for_test_sets**](TestRunApi.md#create_test_run_for_test_sets) | **POST** /v3/trackers/{testRunTrackerId}/testruns/generatefromtestset | Create a new test run for test cases or test sets
[**update_test_run_result**](TestRunApi.md#update_test_run_result) | **PUT** /v3/testruns/{testRunId} | Update result of a Test Run. 
[**upload_automated_test_results**](TestRunApi.md#upload_automated_test_results) | **POST** /v3/trackers/{testRunTrackerId}/automatedtestruns | Create a new test run for large number of automated test cases

# **create_test_run_for_test_case**
> TrackerItem create_test_run_for_test_case(body, test_run_tracker_id)

Create a new test run for test cases or test sets

For multiple test sets please use trackers/{testRunTrackerId}/testruns/generatefromtestset endpoint.

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTestRunRequest() # CreateTestRunRequest | 
test_run_tracker_id = 56 # int | 

try:
    # Create a new test run for test cases or test sets
    api_response = api_instance.create_test_run_for_test_case(body, test_run_tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->create_test_run_for_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTestRunRequest**](CreateTestRunRequest.md)|  | 
 **test_run_tracker_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_run_for_test_sets**
> TestRunResult create_test_run_for_test_sets(body, test_run_tracker_id)

Create a new test run for test cases or test sets

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTestRunFromTestSetsRequest() # CreateTestRunFromTestSetsRequest | 
test_run_tracker_id = 56 # int | 

try:
    # Create a new test run for test cases or test sets
    api_response = api_instance.create_test_run_for_test_sets(body, test_run_tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->create_test_run_for_test_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTestRunFromTestSetsRequest**](CreateTestRunFromTestSetsRequest.md)|  | 
 **test_run_tracker_id** | **int**|  | 

### Return type

[**TestRunResult**](TestRunResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_run_result**
> TrackerItem update_test_run_result(body, test_run_id)

Update result of a Test Run. 

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTestRunRequest() # UpdateTestRunRequest | 
test_run_id = 56 # int | 

try:
    # Update result of a Test Run. 
    api_response = api_instance.update_test_run_result(body, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->update_test_run_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTestRunRequest**](UpdateTestRunRequest.md)|  | 
 **test_run_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_automated_test_results**
> TrackerItem upload_automated_test_results(body, test_run_tracker_id)

Create a new test run for large number of automated test cases

Upload large amount of automated test case run results into a single test run. This process may take a while, please check your proxy settings to prevent timeout.

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
api_instance = swagger_client.TestRunApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutomatedTestRunRequest() # AutomatedTestRunRequest | 
test_run_tracker_id = 56 # int | 

try:
    # Create a new test run for large number of automated test cases
    api_response = api_instance.upload_automated_test_results(body, test_run_tracker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRunApi->upload_automated_test_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomatedTestRunRequest**](AutomatedTestRunRequest.md)|  | 
 **test_run_tracker_id** | **int**|  | 

### Return type

[**TrackerItem**](TrackerItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

