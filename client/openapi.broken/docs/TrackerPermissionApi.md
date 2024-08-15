# openapi_client.TrackerPermissionApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

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

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_permission import TrackerPermission
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
    api_instance = openapi_client.TrackerPermissionApi(api_client)
    tracker_permission_id = 56 # int | 

    try:
        # Get the immutable definition of a tracker permission
        api_response = api_instance.get_tracker_permission(tracker_permission_id)
        print("The response of TrackerPermissionApi->get_tracker_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerPermissionApi->get_tracker_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_permission_id** | **int**|  | 

### Return type

[**TrackerPermission**](TrackerPermission.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker permission. |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required. |  -  |
**404** | Resource is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_permissions**
> List[TrackerPermissionReference] get_tracker_permissions()

Get available tracker permissions

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_permission_reference import TrackerPermissionReference
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
    api_instance = openapi_client.TrackerPermissionApi(api_client)

    try:
        # Get available tracker permissions
        api_response = api_instance.get_tracker_permissions()
        print("The response of TrackerPermissionApi->get_tracker_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerPermissionApi->get_tracker_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TrackerPermissionReference]**](TrackerPermissionReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker permissions. |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required. |  -  |
**404** | Tracker permission is not found. |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_permissions_with_roles**
> List[RoleWithPermissions] get_tracker_permissions_with_roles(tracker_id, user_id=user_id, role_id=role_id)

List tracker permissions per role

API can be used to list tracker permissions per roles, filtering is possible by user, user and on of the user's role, or just by role

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.role_with_permissions import RoleWithPermissions
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
    api_instance = openapi_client.TrackerPermissionApi(api_client)
    tracker_id = 56 # int | 
    user_id = 56 # int |  (optional)
    role_id = 56 # int |  (optional)

    try:
        # List tracker permissions per role
        api_response = api_instance.get_tracker_permissions_with_roles(tracker_id, user_id=user_id, role_id=role_id)
        print("The response of TrackerPermissionApi->get_tracker_permissions_with_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerPermissionApi->get_tracker_permissions_with_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **user_id** | **int**|  | [optional] 
 **role_id** | **int**|  | [optional] 

### Return type

[**List[RoleWithPermissions]**](RoleWithPermissions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker permissions by role. |  -  |
**400** | No access permission for this resource |  -  |
**403** | Authentication is required. |  -  |
**404** | Tracker is not found. |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permissions**
> remove_permissions(tracker_id, role_id)

Removes all tracker permissions from a specific role

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
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
    api_instance = openapi_client.TrackerPermissionApi(api_client)
    tracker_id = 56 # int | 
    role_id = 56 # int | 

    try:
        # Removes all tracker permissions from a specific role
        api_instance.remove_permissions(tracker_id, role_id)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker permissions were removed. |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker/role is not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission**
> List[RoleWithPermissions] update_permission(tracker_id, role_id, permission_ids_request)

Set the tracker permissions for a specific role

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.permission_ids_request import PermissionIdsRequest
from openapi_client.models.role_with_permissions import RoleWithPermissions
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
    api_instance = openapi_client.TrackerPermissionApi(api_client)
    tracker_id = 56 # int | 
    role_id = 56 # int | 
    permission_ids_request = openapi_client.PermissionIdsRequest() # PermissionIdsRequest | 

    try:
        # Set the tracker permissions for a specific role
        api_response = api_instance.update_permission(tracker_id, role_id, permission_ids_request)
        print("The response of TrackerPermissionApi->update_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerPermissionApi->update_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_id** | **int**|  | 
 **role_id** | **int**|  | 
 **permission_ids_request** | [**PermissionIdsRequest**](PermissionIdsRequest.md)|  | 

### Return type

[**List[RoleWithPermissions]**](RoleWithPermissions.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tracker permissions are set |  -  |
**400** | Bad Request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / permission / roles not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

