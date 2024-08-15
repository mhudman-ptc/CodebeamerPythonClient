# swagger_client.WikiApi

All URIs are relative to *https://ptc.codebeamer.com/api*

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | Wiki page id

try:
    # Check whether a wiki page is locked, and if it is, retrieve the details of the lock
    api_response = api_instance.check_wiki_page_lock(wiki_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->check_wiki_page_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

[**LockInfo**](LockInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wiki_page**
> WikiPage create_wiki_page(body)

Create a new wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WikiPage() # WikiPage | 

try:
    # Create a new wiki page
    api_response = api_instance.create_wiki_page(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->create_wiki_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WikiPage**](WikiPage.md)|  | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wiki_page**
> delete_wiki_page(wiki_id)

Delete a wiki page by its ID

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | ID of the wiki page

try:
    # Delete a wiki page by its ID
    api_instance.delete_wiki_page(wiki_id)
except ApiException as e:
    print("Exception when calling WikiApi->delete_wiki_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| ID of the wiki page | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_page**
> WikiPage get_wiki_page(wiki_id, version=version)

Get wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | ID of the wiki page
version = 56 # int | Version of the wiki page (optional)

try:
    # Get wiki page
    api_response = api_instance.get_wiki_page(wiki_id, version=version)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_page_history**
> ArtifactRevisionSearchResult get_wiki_page_history(wiki_id, page=page, page_size=page_size)

Returns the change history of the specified wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Returns the change history of the specified wiki page
    api_response = api_instance.get_wiki_page_history(wiki_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_permissions**
> list[AccessPermission] get_wiki_permissions(wiki_id)

Get permissions of a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | Wiki page id

try:
    # Get permissions of a wiki page
    api_response = api_instance.get_wiki_permissions(wiki_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->get_wiki_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

[**list[AccessPermission]**](AccessPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_wiki_page**
> lock_wiki_page(body, wiki_id)

Lock a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
body = swagger_client.LockRequest() # LockRequest | 
wiki_id = 56 # int | Wiki page id

try:
    # Lock a wiki page
    api_instance.lock_wiki_page(body, wiki_id)
except ApiException as e:
    print("Exception when calling WikiApi->lock_wiki_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LockRequest**](LockRequest.md)|  | 
 **wiki_id** | **int**| Wiki page id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_wiki_markup**
> str render_wiki_markup(body, project_id)

Render a wiki page as HTML in a specific context

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WikiRenderRequest() # WikiRenderRequest | 
project_id = 56 # int | 

try:
    # Render a wiki page as HTML in a specific context
    api_response = api_instance.render_wiki_markup(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->render_wiki_markup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WikiRenderRequest**](WikiRenderRequest.md)|  | 
 **project_id** | **int**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_wiki_page**
> str render_wiki_page(wiki_id, version=version)

Render a wiki page as HTML

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | ID of the wiki page
version = 56 # int | version of the wiki page (optional)

try:
    # Render a wiki page as HTML
    api_response = api_instance.render_wiki_page(wiki_id, version=version)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_wiki_page_content**
> WikiPage restore_wiki_page_content(wiki_id, version)

Restores the content from a previous version of a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | Wiki page id
version = 56 # int | The version to be restored

try:
    # Restores the content from a previous version of a wiki page
    api_response = api_instance.restore_wiki_page_content(wiki_id, version)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_wiki_permissions**
> list[AccessPermission] set_wiki_permissions(body, wiki_id, recursive=recursive)

Set permissions of a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessPermissionsRequest() # AccessPermissionsRequest | 
wiki_id = 56 # int | Wiki page id
recursive = false # bool | Set permissions of children recursively (optional) (default to false)

try:
    # Set permissions of a wiki page
    api_response = api_instance.set_wiki_permissions(body, wiki_id, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->set_wiki_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPermissionsRequest**](AccessPermissionsRequest.md)|  | 
 **wiki_id** | **int**| Wiki page id | 
 **recursive** | **bool**| Set permissions of children recursively | [optional] [default to false]

### Return type

[**list[AccessPermission]**](AccessPermission.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_wiki_page**
> unlock_wiki_page(wiki_id)

Unlock a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | Wiki page id

try:
    # Unlock a wiki page
    api_instance.unlock_wiki_page(wiki_id)
except ApiException as e:
    print("Exception when calling WikiApi->unlock_wiki_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| Wiki page id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wiki_page**
> WikiPage update_wiki_page(body, item_id)

Update and/or move a wiki page

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
api_instance = swagger_client.WikiApi(swagger_client.ApiClient(configuration))
body = swagger_client.WikiPage() # WikiPage | 
item_id = 56 # int | Id of the wiki page to update

try:
    # Update and/or move a wiki page
    api_response = api_instance.update_wiki_page(body, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikiApi->update_wiki_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WikiPage**](WikiPage.md)|  | 
 **item_id** | **int**| Id of the wiki page to update | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

