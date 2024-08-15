# swagger_client.BackgroundJobApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_background_job**](BackgroundJobApi.md#get_background_job) | **GET** /v3/job/{jobId} | Retrieve background job information
[**update_working_set**](BackgroundJobApi.md#update_working_set) | **POST** /v3/jobs/working-set-update | Create background job to update working-set

# **get_background_job**
> BackgroundJob get_background_job(job_id)

Retrieve background job information

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
api_instance = swagger_client.BackgroundJobApi(swagger_client.ApiClient(configuration))
job_id = 56 # int | 

try:
    # Retrieve background job information
    api_response = api_instance.get_background_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundJobApi->get_background_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

[**BackgroundJob**](BackgroundJob.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_working_set**
> JobReference update_working_set(body)

Create background job to update working-set

This API can be used start a Job that merges changes from the source into the target Working-Set replacing the content of the specified target trackers completely.

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
api_instance = swagger_client.BackgroundJobApi(swagger_client.ApiClient(configuration))
body = swagger_client.WorkingSetUpdateRequest() # WorkingSetUpdateRequest | 

try:
    # Create background job to update working-set
    api_response = api_instance.update_working_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundJobApi->update_working_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkingSetUpdateRequest**](WorkingSetUpdateRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

