# openapi_client.DeploymentApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_for_deployment**](DeploymentApi.md#export_for_deployment) | **POST** /v3/deployment/export | Export projects for deployment
[**upload_deployment**](DeploymentApi.md#upload_deployment) | **POST** /v3/deployment | Start a deployment process


# **export_for_deployment**
> JobReference export_for_deployment(export_for_deployment_request)

Export projects for deployment

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.export_for_deployment_request import ExportForDeploymentRequest
from openapi_client.models.job_reference import JobReference
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
    api_instance = openapi_client.DeploymentApi(api_client)
    export_for_deployment_request = openapi_client.ExportForDeploymentRequest() # ExportForDeploymentRequest | 

    try:
        # Export projects for deployment
        api_response = api_instance.export_for_deployment(export_for_deployment_request)
        print("The response of DeploymentApi->export_for_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->export_for_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_for_deployment_request** | [**ExportForDeploymentRequest**](ExportForDeploymentRequest.md)|  | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export job has been scheduled successfully |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**429** | Too many requests |  -  |
**501** | Project Configuration Deployment is disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_deployment**
> JobReference upload_deployment(imports, import_tracker_hierarchy=import_tracker_hierarchy, password=password, skip_refresh_computed_fields=skip_refresh_computed_fields)

Start a deployment process

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.job_reference import JobReference
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
    api_instance = openapi_client.DeploymentApi(api_client)
    imports = None # bytearray | Deployment files
    import_tracker_hierarchy = True # bool | Import tracker inheritance. This is controlled by Application Configuration. Can be true if this configuration is enabled. (optional)
    password = 'password_example' # str | Import file password (optional)
    skip_refresh_computed_fields = True # bool | Skip refresh computed fields on tracker items (optional)

    try:
        # Start a deployment process
        api_response = api_instance.upload_deployment(imports, import_tracker_hierarchy=import_tracker_hierarchy, password=password, skip_refresh_computed_fields=skip_refresh_computed_fields)
        print("The response of DeploymentApi->upload_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentApi->upload_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imports** | **bytearray**| Deployment files | 
 **import_tracker_hierarchy** | **bool**| Import tracker inheritance. This is controlled by Application Configuration. Can be true if this configuration is enabled. | [optional] 
 **password** | **str**| Import file password | [optional] 
 **skip_refresh_computed_fields** | **bool**| Skip refresh computed fields on tracker items | [optional] 

### Return type

[**JobReference**](JobReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment is executed |  -  |
**400** | Bad request |  -  |
**401** | Authentication is required |  -  |
**403** | Authentication is required |  -  |
**429** | Too many requests |  -  |
**501** | Project Configuration Deployment is disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

