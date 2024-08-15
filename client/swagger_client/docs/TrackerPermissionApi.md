# swagger_client.TrackerPermissionApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tracker_permission**](TrackerPermissionApi.md#get_tracker_permission) | **GET** /v3/trackers/permissions/{trackerPermissionId} | Get the immutable definition of a tracker permission
[**get_tracker_permissions**](TrackerPermissionApi.md#get_tracker_permissions) | **GET** /v3/trackers/permissions | Get available tracker permissions
[**get_tracker_permissions_with_roles**](TrackerPermissionApi.md#get_tracker_permissions_with_roles) | **GET** /v3/trackers/{trackerId}/permissions | List tracker permissions per role
[**remove_permissions**](TrackerPermissionApi.md#remove_permissions) | **DELETE** /v3/trackers/{trackerId}/roles/{roleId}/permissions | Removes all tracker permissions from a specific role
[**update_permission**](TrackerPermissionApi.md#update_permission) | **PUT** /v3/trackers/{trackerId}/roles/{roleId}/permissions | Set the tracker permissions for a specific role

# **get_tracker_permission**
> TrackerPermission get_tracker_permission(tracker_permission_id)

Get the immutable definition of a tracker permission

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
api_instance = swagger_client.TrackerPermissionApi(swagger_client.ApiClient(configuration))
tracker_permission_id = 56 # int | 

try:
    # Get the immutable definition of a tracker permission
    api_response = api_instance.get_tracker_permission(tracker_permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerPermissionApi->get_tracker_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_permission_id** | **int**|  | 

### Return type

[**TrackerPermission**](TrackerPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_permissions**
> list[TrackerPermissionReference] get_tracker_permissions()

Get available tracker permissions

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
api_instance = swagger_client.TrackerPermissionApi(swagger_client.ApiClient(configuration))

try:
    # Get available tracker permissions
    api_response = api_instance.get_tracker_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerPermissionApi->get_tracker_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TrackerPermissionReference]**](TrackerPermissionReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_permissions_with_roles**
> list[RoleWithPermissions] get_tracker_permissions_with_roles(tracker_id, user_id=user_id, role_id=role_id)

List tracker permissions per role

API can be used to list tracker permissions per roles, filtering is possible by user, user and on of the user's role, or just by role

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
api_instance = swagger_client.TrackerPermissionApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
user_id = 56 # int |  (optional)
role_id = 56 # int |  (optional)

try:
    # List tracker permissions per role
    api_response = api_instance.get_tracker_permissions_with_roles(tracker_id, user_id=user_id, role_id=role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerPermissionApi->get_tracker_permissions_with_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **user_id** | **int**|  | [optional] 
 **role_id** | **int**|  | [optional] 

### Return type

[**list[RoleWithPermissions]**](RoleWithPermissions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permissions**
> remove_permissions(tracker_id, role_id)

Removes all tracker permissions from a specific role

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
api_instance = swagger_client.TrackerPermissionApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | 
role_id = 56 # int | 

try:
    # Removes all tracker permissions from a specific role
    api_instance.remove_permissions(tracker_id, role_id)
except ApiException as e:
    print("Exception when calling TrackerPermissionApi->remove_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **role_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission**
> list[RoleWithPermissions] update_permission(body, tracker_id, role_id)

Set the tracker permissions for a specific role

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
api_instance = swagger_client.TrackerPermissionApi(swagger_client.ApiClient(configuration))
body = swagger_client.PermissionIdsRequest() # PermissionIdsRequest | 
tracker_id = 56 # int | 
role_id = 56 # int | 

try:
    # Set the tracker permissions for a specific role
    api_response = api_instance.update_permission(body, tracker_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerPermissionApi->update_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionIdsRequest**](PermissionIdsRequest.md)|  | 
 **tracker_id** | **int**|  | 
 **role_id** | **int**|  | 

### Return type

[**list[RoleWithPermissions]**](RoleWithPermissions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

