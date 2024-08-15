# openapi_client.TrackerItemsAttachmentApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tracker_item_attachment**](TrackerItemsAttachmentApi.md#delete_tracker_item_attachment) | **DELETE** /v3/items/{itemId}/attachments/{attachmentId} | Delete attachment of tracker item by id
[**delete_tracker_item_attachments**](TrackerItemsAttachmentApi.md#delete_tracker_item_attachments) | **DELETE** /v3/items/{itemId}/attachments | Delete attachments of tracker item
[**get_tracker_item_attachment**](TrackerItemsAttachmentApi.md#get_tracker_item_attachment) | **GET** /v3/items/{itemId}/attachments/{attachmentId} | Get attachment of tracker item by id
[**get_tracker_item_attachment_content**](TrackerItemsAttachmentApi.md#get_tracker_item_attachment_content) | **GET** /v3/items/{itemId}/attachments/{attachmentId}/content | Get content of an attachment of tracker item by id
[**get_tracker_item_attachment_contents**](TrackerItemsAttachmentApi.md#get_tracker_item_attachment_contents) | **GET** /v3/items/{itemId}/attachments/content | Get attachments of a tracker item
[**get_tracker_item_attachments**](TrackerItemsAttachmentApi.md#get_tracker_item_attachments) | **GET** /v3/items/{itemId}/attachments | Get attachments of tracker item
[**get_tracker_items_attachment_contents**](TrackerItemsAttachmentApi.md#get_tracker_items_attachment_contents) | **POST** /v3/items/attachments/content | Get attachments of tracker items matching the extension or mime type filters
[**update_attachment_of_tracker_item**](TrackerItemsAttachmentApi.md#update_attachment_of_tracker_item) | **PUT** /v3/items/{itemId}/attachments/{attachmentId}/content | Update content of attachment of tracker item
[**upload_tracker_item_attachment**](TrackerItemsAttachmentApi.md#upload_tracker_item_attachment) | **POST** /v3/items/{itemId}/attachments | Upload an attachment to a tracker item


# **delete_tracker_item_attachment**
> Attachment delete_tracker_item_attachment(item_id, attachment_id, delete_attachment_group=delete_attachment_group)

Delete attachment of tracker item by id

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment import Attachment
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    attachment_id = 56 # int | 
    delete_attachment_group = False # bool | Delete attachment group or delete just the attachment and let the comment there (optional) (default to False)

    try:
        # Delete attachment of tracker item by id
        api_response = api_instance.delete_tracker_item_attachment(item_id, attachment_id, delete_attachment_group=delete_attachment_group)
        print("The response of TrackerItemsAttachmentApi->delete_tracker_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->delete_tracker_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 
 **delete_attachment_group** | **bool**| Delete attachment group or delete just the attachment and let the comment there | [optional] [default to False]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_attachments**
> delete_tracker_item_attachments(item_id, delete_attachment_group=delete_attachment_group)

Delete attachments of tracker item

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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    delete_attachment_group = False # bool | Delete attachment group or delete just the attachment and let the comment there (optional) (default to False)

    try:
        # Delete attachments of tracker item
        api_instance.delete_tracker_item_attachments(item_id, delete_attachment_group=delete_attachment_group)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->delete_tracker_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **delete_attachment_group** | **bool**| Delete attachment group or delete just the attachment and let the comment there | [optional] [default to False]

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
**200** | Attachments of tracker item removed |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment**
> Attachment get_tracker_item_attachment(item_id, attachment_id)

Get attachment of tracker item by id

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment import Attachment
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    attachment_id = 56 # int | 

    try:
        # Get attachment of tracker item by id
        api_response = api_instance.get_tracker_item_attachment(item_id, attachment_id)
        print("The response of TrackerItemsAttachmentApi->get_tracker_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Attachment not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment_content**
> bytearray get_tracker_item_attachment_content(item_id, attachment_id)

Get content of an attachment of tracker item by id

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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    attachment_id = 56 # int | 

    try:
        # Get content of an attachment of tracker item by id
        api_response = api_instance.get_tracker_item_attachment_content(item_id, attachment_id)
        print("The response of TrackerItemsAttachmentApi->get_tracker_item_attachment_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachment_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker / Attachment not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment_contents**
> bytearray get_tracker_item_attachment_contents(item_id)

Get attachments of a tracker item

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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 

    try:
        # Get attachments of a tracker item
        api_response = api_instance.get_tracker_item_attachment_contents(item_id)
        print("The response of TrackerItemsAttachmentApi->get_tracker_item_attachment_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachment_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachments of a tracker item: contains the attachment files prefixed with the attachment id like [attachment-id]_[filename]. |  -  |
**400** | Bad request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachments**
> AttachmentSearchResult get_tracker_item_attachments(item_id, file_name=file_name)

Get attachments of tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment_search_result import AttachmentSearchResult
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | Id of the tracker item
    file_name = 'file_name_example' # str | Filter by part of the filename of the attachments (optional)

    try:
        # Get attachments of tracker item
        api_response = api_instance.get_tracker_item_attachments(item_id, file_name=file_name)
        print("The response of TrackerItemsAttachmentApi->get_tracker_item_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of the tracker item | 
 **file_name** | **str**| Filter by part of the filename of the attachments | [optional] 

### Return type

[**AttachmentSearchResult**](AttachmentSearchResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachments of tracker item |  -  |
**401** | Access denied |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker item not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_items_attachment_contents**
> bytearray get_tracker_items_attachment_contents(tracker_item_attachment_request)

Get attachments of tracker items matching the extension or mime type filters

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.tracker_item_attachment_request import TrackerItemAttachmentRequest
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    tracker_item_attachment_request = openapi_client.TrackerItemAttachmentRequest() # TrackerItemAttachmentRequest | 

    try:
        # Get attachments of tracker items matching the extension or mime type filters
        api_response = api_instance.get_tracker_items_attachment_contents(tracker_item_attachment_request)
        print("The response of TrackerItemsAttachmentApi->get_tracker_items_attachment_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->get_tracker_items_attachment_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracker_item_attachment_request** | [**TrackerItemAttachmentRequest**](TrackerItemAttachmentRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachments of tracker items: each tracker item goes to a subdirectory named as item-id and this directory contains the attachment files prefixed with the attachment id like [attachment-id]_[filename]. |  -  |
**400** | Bad request |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker items not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment_of_tracker_item**
> Attachment update_attachment_of_tracker_item(item_id, attachment_id, content=content, description=description, description_format=description_format)

Update content of attachment of tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment import Attachment
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    attachment_id = 56 # int | 
    content = None # bytearray |  (optional)
    description = 'description_example' # str | Description (optional)
    description_format = 'PlainText' # str | Format of description (optional) (default to 'PlainText')

    try:
        # Update content of attachment of tracker item
        api_response = api_instance.update_attachment_of_tracker_item(item_id, attachment_id, content=content, description=description, description_format=description_format)
        print("The response of TrackerItemsAttachmentApi->update_attachment_of_tracker_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->update_attachment_of_tracker_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 
 **content** | **bytearray**|  | [optional] 
 **description** | **str**| Description | [optional] 
 **description_format** | **str**| Format of description | [optional] [default to &#39;PlainText&#39;]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated attachment |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Tracker item or attachment not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_tracker_item_attachment**
> List[Attachment] upload_tracker_item_attachment(item_id, attachments=attachments)

Upload an attachment to a tracker item

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment import Attachment
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
    api_instance = openapi_client.TrackerItemsAttachmentApi(api_client)
    item_id = 56 # int | 
    attachments = None # bytearray | Attachments of a comment (optional)

    try:
        # Upload an attachment to a tracker item
        api_response = api_instance.upload_tracker_item_attachment(item_id, attachments=attachments)
        print("The response of TrackerItemsAttachmentApi->upload_tracker_item_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackerItemsAttachmentApi->upload_tracker_item_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachments** | **bytearray**| Attachments of a comment | [optional] 

### Return type

[**List[Attachment]**](Attachment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment of tracker item by id |  -  |
**403** | Authentication is required |  -  |
**404** | Tracker not found |  -  |
**423** | Tracker item is locked |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

