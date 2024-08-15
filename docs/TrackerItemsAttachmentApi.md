# swagger_client.TrackerItemsAttachmentApi

All URIs are relative to *https://alm.codebeamer.com/api*

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachment_id = 56 # int | 
delete_attachment_group = false # bool | Delete attachment group or delete just the attachment and let the comment there (optional) (default to false)

try:
    # Delete attachment of tracker item by id
    api_response = api_instance.delete_tracker_item_attachment(item_id, attachment_id, delete_attachment_group=delete_attachment_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->delete_tracker_item_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 
 **delete_attachment_group** | **bool**| Delete attachment group or delete just the attachment and let the comment there | [optional] [default to false]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_attachments**
> delete_tracker_item_attachments(item_id, delete_attachment_group=delete_attachment_group)

Delete attachments of tracker item

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
delete_attachment_group = false # bool | Delete attachment group or delete just the attachment and let the comment there (optional) (default to false)

try:
    # Delete attachments of tracker item
    api_instance.delete_tracker_item_attachments(item_id, delete_attachment_group=delete_attachment_group)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->delete_tracker_item_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **delete_attachment_group** | **bool**| Delete attachment group or delete just the attachment and let the comment there | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment**
> Attachment get_tracker_item_attachment(item_id, attachment_id)

Get attachment of tracker item by id

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachment_id = 56 # int | 

try:
    # Get attachment of tracker item by id
    api_response = api_instance.get_tracker_item_attachment(item_id, attachment_id)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment_content**
> str get_tracker_item_attachment_content(item_id, attachment_id)

Get content of an attachment of tracker item by id

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachment_id = 56 # int | 

try:
    # Get content of an attachment of tracker item by id
    api_response = api_instance.get_tracker_item_attachment_content(item_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachment_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachment_contents**
> str get_tracker_item_attachment_contents(item_id)

Get attachments of a tracker item

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Get attachments of a tracker item
    api_response = api_instance.get_tracker_item_attachment_contents(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->get_tracker_item_attachment_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_attachments**
> AttachmentSearchResult get_tracker_item_attachments(item_id, file_name=file_name)

Get attachments of tracker item

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | Id of the tracker item
file_name = 'file_name_example' # str | Filter by part of the filename of the attachments (optional)

try:
    # Get attachments of tracker item
    api_response = api_instance.get_tracker_item_attachments(item_id, file_name=file_name)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_items_attachment_contents**
> str get_tracker_items_attachment_contents(body)

Get attachments of tracker items matching the extension or mime type filters

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrackerItemAttachmentRequest() # TrackerItemAttachmentRequest | 

try:
    # Get attachments of tracker items matching the extension or mime type filters
    api_response = api_instance.get_tracker_items_attachment_contents(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->get_tracker_items_attachment_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackerItemAttachmentRequest**](TrackerItemAttachmentRequest.md)|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment_of_tracker_item**
> Attachment update_attachment_of_tracker_item(item_id, attachment_id, content=content, description=description, description_format=description_format)

Update content of attachment of tracker item

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachment_id = 56 # int | 
content = 'content_example' # str |  (optional)
description = 'description_example' # str |  (optional)
description_format = 'description_format_example' # str |  (optional)

try:
    # Update content of attachment of tracker item
    api_response = api_instance.update_attachment_of_tracker_item(item_id, attachment_id, content=content, description=description, description_format=description_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->update_attachment_of_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachment_id** | **int**|  | 
 **content** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **description_format** | **str**|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_tracker_item_attachment**
> list[Attachment] upload_tracker_item_attachment(item_id, attachments=attachments)

Upload an attachment to a tracker item

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
api_instance = swagger_client.TrackerItemsAttachmentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachments = 'attachments_example' # str |  (optional)

try:
    # Upload an attachment to a tracker item
    api_response = api_instance.upload_tracker_item_attachment(item_id, attachments=attachments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsAttachmentApi->upload_tracker_item_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachments** | **str**|  | [optional] 

### Return type

[**list[Attachment]**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

