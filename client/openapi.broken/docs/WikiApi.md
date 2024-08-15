# openapi_client.WikiApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_wiki_page_lock**](WikiApi.md#check_wiki_page_lock) | **GET** /v3/wikipages/{wikiId}/lock | Check whether a wiki page is locked, and if it is, retrieve the details of the lock
[**create_wiki_page**](WikiApi.md#create_wiki_page) | **POST** /v3/wikipages | Create a new wiki page
[**delete_wiki_page**](WikiApi.md#delete_wiki_page) | **DELETE** /v3/wikipages/{wikiId} | Delete a wiki page by its ID
[**get_wiki_page**](WikiApi.md#get_wiki_page) | **GET** /v3/wikipages/{wikiId} | Get wiki page
[**get_wiki_page_history**](WikiApi.md#get_wiki_page_history) | **GET** /v3/wikipages/{wikiId}/history | Returns the change history of the specified wiki page
[**get_wiki_permissions**](WikiApi.md#get_wiki_permissions) | **GET** /v3/wikipages/{wikiId}/permissions | Get permissions of a wiki page
[**lock_wiki_page**](WikiApi.md#lock_wiki_page) | **PUT** /v3/wikipages/{wikiId}/lock | Lock a wiki page
[**render_wiki_markup**](WikiApi.md#render_wiki_markup) | **POST** /v3/projects/{projectId}/wiki2html | Render a wiki page as HTML in a specific context
[**render_wiki_page**](WikiApi.md#render_wiki_page) | **GET** /v3/wikipages/{wikiId}/html | Render a wiki page as HTML
[**restore_wiki_page_content**](WikiApi.md#restore_wiki_page_content) | **PUT** /v3/wikipages/{wikiId}/restorecontent | Restores the content from a previous version of a wiki page
[**set_wiki_permissions**](WikiApi.md#set_wiki_permissions) | **PUT** /v3/wikipages/{wikiId}/permissions | Set permissions of a wiki page
[**unlock_wiki_page**](WikiApi.md#unlock_wiki_page) | **DELETE** /v3/wikipages/{wikiId}/lock | Unlock a wiki page
[**update_wiki_page**](WikiApi.md#update_wiki_page) | **PUT** /v3/wikipages/{itemId} | Update and/or move a wiki page


# **check_wiki_page_lock**
> LockInfo check_wiki_page_lock(wiki_id)

Check whether a wiki page is locked, and if it is, retrieve the details of the lock

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.lock_info import LockInfo
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id

    try:
        # Check whether a wiki page is locked, and if it is, retrieve the details of the lock
        api_response = api_instance.check_wiki_page_lock(wiki_id)
        print("The response of WikiApi->check_wiki_page_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->check_wiki_page_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

[**LockInfo**](LockInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the lock, or an empty response |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wiki_page**
> WikiPage create_wiki_page(wiki_page)

Create a new wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wiki_page import WikiPage
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_page = openapi_client.WikiPage() # WikiPage | 

    try:
        # Create a new wiki page
        api_response = api_instance.create_wiki_page(wiki_page)
        print("The response of WikiApi->create_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->create_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_page** | [**WikiPage**](WikiPage.md)|  | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Properties of the created wikipage |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wiki_page**
> delete_wiki_page(wiki_id)

Delete a wiki page by its ID

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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | ID of the wiki page

    try:
        # Delete a wiki page by its ID
        api_instance.delete_wiki_page(wiki_id)
    except Exception as e:
        print("Exception when calling WikiApi->delete_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| ID of the wiki page | 

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
**200** | The wiki page has been deleted successfully |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | The wiki page does not exist, or the artifact is not a wiki page |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_page**
> WikiPage get_wiki_page(wiki_id, version=version)

Get wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wiki_page import WikiPage
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | ID of the wiki page
    version = 56 # int | Version of the wiki page (optional)

    try:
        # Get wiki page
        api_response = api_instance.get_wiki_page(wiki_id, version=version)
        print("The response of WikiApi->get_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->get_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| ID of the wiki page | 
 **version** | **int**| Version of the wiki page | [optional] 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wiki page |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | The wiki page does not exist, or the artifact is not a wiki page |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_page_history**
> ArtifactRevisionSearchResult get_wiki_page_history(wiki_id, page=page, page_size=page_size)

Returns the change history of the specified wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.artifact_revision_search_result import ArtifactRevisionSearchResult
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | 
    page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
    page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

    try:
        # Returns the change history of the specified wiki page
        api_response = api_instance.get_wiki_page_history(wiki_id, page=page, page_size=page_size)
        print("The response of WikiApi->get_wiki_page_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->get_wiki_page_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**|  | 
 **page** | **int**| Index of the result page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items in a result page. Max value: 500 | [optional] [default to 25]

### Return type

[**ArtifactRevisionSearchResult**](ArtifactRevisionSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wiki page history |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_permissions**
> List[AccessPermission] get_wiki_permissions(wiki_id)

Get permissions of a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.access_permission import AccessPermission
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id

    try:
        # Get permissions of a wiki page
        api_response = api_instance.get_wiki_permissions(wiki_id)
        print("The response of WikiApi->get_wiki_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->get_wiki_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

[**List[AccessPermission]**](AccessPermission.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions of the wiki page |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_wiki_page**
> lock_wiki_page(wiki_id, lock_request)

Lock a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.lock_request import LockRequest
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id
    lock_request = openapi_client.LockRequest() # LockRequest | 

    try:
        # Lock a wiki page
        api_instance.lock_wiki_page(wiki_id, lock_request)
    except Exception as e:
        print("Exception when calling WikiApi->lock_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 
 **lock_request** | [**LockRequest**](LockRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lock acquired successfully |  -  |
**400** | Bad request, request validation error |  -  |
**401** | Authentication is required |  -  |
**403** | Could not acquire lock |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_wiki_markup**
> str render_wiki_markup(project_id, wiki_render_request)

Render a wiki page as HTML in a specific context

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wiki_render_request import WikiRenderRequest
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
    api_instance = openapi_client.WikiApi(api_client)
    project_id = 56 # int | 
    wiki_render_request = openapi_client.WikiRenderRequest() # WikiRenderRequest | 

    try:
        # Render a wiki page as HTML in a specific context
        api_response = api_instance.render_wiki_markup(project_id, wiki_render_request)
        print("The response of WikiApi->render_wiki_markup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->render_wiki_markup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **wiki_render_request** | [**WikiRenderRequest**](WikiRenderRequest.md)|  | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wiki content rendered as HTML |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | The wiki page does not exist, or the artifact is not a wiki page |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_wiki_page**
> str render_wiki_page(wiki_id, version=version)

Render a wiki page as HTML

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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | ID of the wiki page
    version = 56 # int | version of the wiki page (optional)

    try:
        # Render a wiki page as HTML
        api_response = api_instance.render_wiki_page(wiki_id, version=version)
        print("The response of WikiApi->render_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->render_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| ID of the wiki page | 
 **version** | **int**| version of the wiki page | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wiki content rendered as HTML |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | The wiki page does not exist, or the artifact is not a wiki page |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_wiki_page_content**
> WikiPage restore_wiki_page_content(wiki_id, version)

Restores the content from a previous version of a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wiki_page import WikiPage
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id
    version = 56 # int | The version to be restored

    try:
        # Restores the content from a previous version of a wiki page
        api_response = api_instance.restore_wiki_page_content(wiki_id, version)
        print("The response of WikiApi->restore_wiki_page_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->restore_wiki_page_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 
 **version** | **int**| The version to be restored | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wiki page has been restored |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | Wiki page or version not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_wiki_permissions**
> List[AccessPermission] set_wiki_permissions(wiki_id, access_permissions_request, recursive=recursive)

Set permissions of a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.access_permission import AccessPermission
from openapi_client.models.access_permissions_request import AccessPermissionsRequest
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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id
    access_permissions_request = openapi_client.AccessPermissionsRequest() # AccessPermissionsRequest | 
    recursive = False # bool | Set permissions of children recursively (optional) (default to False)

    try:
        # Set permissions of a wiki page
        api_response = api_instance.set_wiki_permissions(wiki_id, access_permissions_request, recursive=recursive)
        print("The response of WikiApi->set_wiki_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->set_wiki_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 
 **access_permissions_request** | [**AccessPermissionsRequest**](AccessPermissionsRequest.md)|  | 
 **recursive** | **bool**| Set permissions of children recursively | [optional] [default to False]

### Return type

[**List[AccessPermission]**](AccessPermission.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permissions of the wiki page |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_wiki_page**
> unlock_wiki_page(wiki_id)

Unlock a wiki page

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
    api_instance = openapi_client.WikiApi(api_client)
    wiki_id = 56 # int | Wiki page id

    try:
        # Unlock a wiki page
        api_instance.unlock_wiki_page(wiki_id)
    except Exception as e:
        print("Exception when calling WikiApi->unlock_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unlock successful |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Could not unlock |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wiki_page**
> WikiPage update_wiki_page(item_id, wiki_page)

Update and/or move a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.wiki_page import WikiPage
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
    api_instance = openapi_client.WikiApi(api_client)
    item_id = 56 # int | Id of the wiki page to update
    wiki_page = openapi_client.WikiPage() # WikiPage | 

    try:
        # Update and/or move a wiki page
        api_response = api_instance.update_wiki_page(item_id, wiki_page)
        print("The response of WikiApi->update_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikiApi->update_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the wiki page to update | 
 **wiki_page** | [**WikiPage**](WikiPage.md)|  | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Properties of the updated wikipage |  -  |
**400** | Request cannot be processed |  -  |
**401** | Authentication is required |  -  |
**403** | Access denied |  -  |
**404** | Wikipage not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

