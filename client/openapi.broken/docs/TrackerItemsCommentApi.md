# openapi_client.TrackerItemsCommentApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comment_on_tracker_item**](TrackerItemsCommentApi.md#comment_on_tracker_item) | **POST** /v3/items/{itemId}/comments | Comment on a tracker item
[**delete_tracker_item_comment**](TrackerItemsCommentApi.md#delete_tracker_item_comment) | **DELETE** /v3/items/{itemId}/comments/{commentId} | Delete comment of tracker item by id
[**delete_tracker_item_comments**](TrackerItemsCommentApi.md#delete_tracker_item_comments) | **DELETE** /v3/items/{itemId}/comments | Delete comments of tracker item by item id
[**edit_comment_on_tracker_item**](TrackerItemsCommentApi.md#edit_comment_on_tracker_item) | **PUT** /v3/items/{itemId}/comments/{commentId} | Edit comment on a tracker item
[**get_tracker_item_comment**](TrackerItemsCommentApi.md#get_tracker_item_comment) | **GET** /v3/items/{itemId}/comments/{commentId} | Get comment of tracker item by id
[**get_tracker_item_comments**](TrackerItemsCommentApi.md#get_tracker_item_comments) | **GET** /v3/items/{itemId}/comments | Get comments of tracker item
[**reply_on_comment_of_tracker_item**](TrackerItemsCommentApi.md#reply_on_comment_of_tracker_item) | **POST** /v3/items/{itemId}/comments/{commentId} | Reply on a comment of a tracker item


# **comment_on_tracker_item**
> Comment comment_on_tracker_item(item_id, comment, attachments=attachments, comment_format=comment_format)

Comment on a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 
    comment = 'comment_example' # str | Text of a comment
    attachments = None # bytearray | Attachments of a comment (optional)
    comment_format = 'PlainText' # str | Format of a comment (optional) (default to 'PlainText')

    try:
        # Comment on a tracker item
        api_response = api_instance.comment_on_tracker_item(item_id, comment, attachments=attachments, comment_format=comment_format)
        print("The response of TrackerItemsCommentApi->comment_on_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->comment_on_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment** | **str**| Text of a comment | 
 **attachments** | **bytearray**| Attachments of a comment | [optional] 
 **comment_format** | **str**| Format of a comment | [optional] [default to &#39;PlainText&#39;]

### Return type

[**Comment**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_comment**
> Comment delete_tracker_item_comment(item_id, comment_id)

Delete comment of tracker item by id

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 
    comment_id = 56 # int | 

    try:
        # Delete comment of tracker item by id
        api_response = api_instance.delete_tracker_item_comment(item_id, comment_id)
        print("The response of TrackerItemsCommentApi->delete_tracker_item_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->delete_tracker_item_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_comments**
> delete_tracker_item_comments(item_id)

Delete comments of tracker item by item id

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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 

    try:
        # Delete comments of tracker item by item id
        api_instance.delete_tracker_item_comments(item_id)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->delete_tracker_item_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

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
**200** | Comments deleted |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_comment_on_tracker_item**
> Comment edit_comment_on_tracker_item(item_id, comment_id, comment, attachments=attachments, comment_format=comment_format)

Edit comment on a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 
    comment_id = 56 # int | 
    comment = 'comment_example' # str | Text of a comment
    attachments = None # bytearray | Attachments of a comment (optional)
    comment_format = 'PlainText' # str | Format of a comment (optional) (default to 'PlainText')

    try:
        # Edit comment on a tracker item
        api_response = api_instance.edit_comment_on_tracker_item(item_id, comment_id, comment, attachments=attachments, comment_format=comment_format)
        print("The response of TrackerItemsCommentApi->edit_comment_on_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->edit_comment_on_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 
 **comment** | **str**| Text of a comment | 
 **attachments** | **bytearray**| Attachments of a comment | [optional] 
 **comment_format** | **str**| Format of a comment | [optional] [default to &#39;PlainText&#39;]

### Return type

[**Comment**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited comment |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_comment**
> Comment get_tracker_item_comment(item_id, comment_id)

Get comment of tracker item by id

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 
    comment_id = 56 # int | 

    try:
        # Get comment of tracker item by id
        api_response = api_instance.get_tracker_item_comment(item_id, comment_id)
        print("The response of TrackerItemsCommentApi->get_tracker_item_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->get_tracker_item_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_comments**
> List[Comment] get_tracker_item_comments(item_id)

Get comments of tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | Id of a tracker item

    try:
        # Get comments of tracker item
        api_response = api_instance.get_tracker_item_comments(item_id)
        print("The response of TrackerItemsCommentApi->get_tracker_item_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->get_tracker_item_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of a tracker item | 

### Return type

[**List[Comment]**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_on_comment_of_tracker_item**
> Comment reply_on_comment_of_tracker_item(item_id, comment_id, comment, attachments=attachments, comment_format=comment_format)

Reply on a comment of a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.comment import Comment
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
    api_instance = openapi_client.TrackerItemsCommentApi(api_client)
    item_id = 56 # int | 
    comment_id = 56 # int | 
    comment = 'comment_example' # str | Text of a comment
    attachments = None # bytearray | Attachments of a comment (optional)
    comment_format = 'PlainText' # str | Format of a comment (optional) (default to 'PlainText')

    try:
        # Reply on a comment of a tracker item
        api_response = api_instance.reply_on_comment_of_tracker_item(item_id, comment_id, comment, attachments=attachments, comment_format=comment_format)
        print("The response of TrackerItemsCommentApi->reply_on_comment_of_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsCommentApi->reply_on_comment_of_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 
 **comment** | **str**| Text of a comment | 
 **attachments** | **bytearray**| Attachments of a comment | [optional] 
 **comment_format** | **str**| Format of a comment | [optional] [default to &#39;PlainText&#39;]

### Return type

[**Comment**](Comment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

