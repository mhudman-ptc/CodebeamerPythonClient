# swagger_client.RepositoryItemApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_scm_repository**](RepositoryItemApi.md#create_external_scm_repository) | **POST** /v3/trackers/projects/{projectId}/repository | Create an external scm repository item
[**update_external_scm_repository**](RepositoryItemApi.md#update_external_scm_repository) | **PUT** /v3/trackers/projects/{projectId}/repository/{repositoryId} | Update an external scm repository item

# **create_external_scm_repository**
> int create_external_scm_repository(body, project_id)

Create an external scm repository item

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
api_instance = swagger_client.RepositoryItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalScmRepositoryRequest() # ExternalScmRepositoryRequest | 
project_id = 56 # int | CB project id

try:
    # Create an external scm repository item
    api_response = api_instance.create_external_scm_repository(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryItemApi->create_external_scm_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalScmRepositoryRequest**](ExternalScmRepositoryRequest.md)|  | 
 **project_id** | **int**| CB project id | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_scm_repository**
> int update_external_scm_repository(body, project_id, repository_id)

Update an external scm repository item

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
api_instance = swagger_client.RepositoryItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalScmRepositoryRequest() # ExternalScmRepositoryRequest | 
project_id = 56 # int | CB project id
repository_id = 56 # int | CB repository id

try:
    # Update an external scm repository item
    api_response = api_instance.update_external_scm_repository(body, project_id, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryItemApi->update_external_scm_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalScmRepositoryRequest**](ExternalScmRepositoryRequest.md)|  | 
 **project_id** | **int**| CB project id | 
 **repository_id** | **int**| CB repository id | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

