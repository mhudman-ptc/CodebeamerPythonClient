# swagger_client.DeploymentApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_for_deployment**](DeploymentApi.md#export_for_deployment) | **POST** /v3/deployment/export | Export projects for deployment
[**upload_deployment**](DeploymentApi.md#upload_deployment) | **POST** /v3/deployment | Start a deployment process

# **export_for_deployment**
> JobReference export_for_deployment(body)

Export projects for deployment

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
api_instance = swagger_client.DeploymentApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExportForDeploymentRequest() # ExportForDeploymentRequest | 

try:
    # Export projects for deployment
    api_response = api_instance.export_for_deployment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->export_for_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportForDeploymentRequest**](ExportForDeploymentRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_deployment**
> JobReference upload_deployment(import_tracker_hierarchy=import_tracker_hierarchy, imports=imports, password=password, skip_refresh_computed_fields=skip_refresh_computed_fields)

Start a deployment process

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
api_instance = swagger_client.DeploymentApi(swagger_client.ApiClient(configuration))
import_tracker_hierarchy = true # bool |  (optional)
imports = 'imports_example' # str |  (optional)
password = 'password_example' # str |  (optional)
skip_refresh_computed_fields = true # bool |  (optional)

try:
    # Start a deployment process
    api_response = api_instance.upload_deployment(import_tracker_hierarchy=import_tracker_hierarchy, imports=imports, password=password, skip_refresh_computed_fields=skip_refresh_computed_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->upload_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_tracker_hierarchy** | **bool**|  | [optional] 
 **imports** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **skip_refresh_computed_fields** | **bool**|  | [optional] 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

