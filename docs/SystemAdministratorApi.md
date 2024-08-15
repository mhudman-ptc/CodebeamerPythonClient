# swagger_client.SystemAdministratorApi

All URIs are relative to *https://alm.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_permissions**](SystemAdministratorApi.md#get_audit_permissions) | **POST** /v3/sysadmin/audit/permissions | Get audit permission entries

# **get_audit_permissions**
> PaginatedAuditPermissionsResponse get_audit_permissions(body, page=page, page_size=page_size)

Get audit permission entries

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
api_instance = swagger_client.SystemAdministratorApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuditPermissionsRequest() # AuditPermissionsRequest | 
page = 1 # int | Index of page, starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items per page. Max value: 100 (optional) (default to 25)

try:
    # Get audit permission entries
    api_response = api_instance.get_audit_permissions(body, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministratorApi->get_audit_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditPermissionsRequest**](AuditPermissionsRequest.md)|  | 
 **page** | **int**| Index of page, starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page. Max value: 100 | [optional] [default to 25]

### Return type

[**PaginatedAuditPermissionsResponse**](PaginatedAuditPermissionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

