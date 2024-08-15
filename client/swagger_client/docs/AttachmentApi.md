# swagger_client.AttachmentApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachment**](AttachmentApi.md#delete_attachment) | **DELETE** /v3/attachments/{attachmentId} | Deletes an attachment
[**get_attachment**](AttachmentApi.md#get_attachment) | **GET** /v3/attachments/{attachmentId} | Get attachment by id
[**get_attachment_content**](AttachmentApi.md#get_attachment_content) | **GET** /v3/attachments/{attachmentId}/content | Get content of an attachment by id
[**get_attachment_history**](AttachmentApi.md#get_attachment_history) | **GET** /v3/attachments/{attachmentId}/history | Returns the change history of the specified attachment
[**restore_attachment**](AttachmentApi.md#restore_attachment) | **PUT** /v3/attachments/{attachmentId}/restore | Restore attachment to previous version
[**update_attachment**](AttachmentApi.md#update_attachment) | **PUT** /v3/attachments/{attachmentId}/content | Update attachment

# **delete_attachment**
> delete_attachment(attachment_id)

Deletes an attachment

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 

try:
    # Deletes an attachment
    api_instance.delete_attachment(attachment_id)
except ApiException as e:
    print("Exception when calling AttachmentApi->delete_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> Attachment get_attachment(attachment_id, version=version)

Get attachment by id

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 
version = 56 # int |  (optional)

try:
    # Get attachment by id
    api_response = api_instance.get_attachment(attachment_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  | 
 **version** | **int**|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_content**
> str get_attachment_content(attachment_id, version=version)

Get content of an attachment by id

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 
version = 56 # int |  (optional)

try:
    # Get content of an attachment by id
    api_response = api_instance.get_attachment_content(attachment_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->get_attachment_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  | 
 **version** | **int**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_history**
> ArtifactRevisionSearchResult get_attachment_history(attachment_id, page=page, page_size=page_size)

Returns the change history of the specified attachment

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 
page = 1 # int | Index of the result page starting from 1. (optional) (default to 1)
page_size = 25 # int | Number of items in a result page. Max value: 500 (optional) (default to 25)

try:
    # Returns the change history of the specified attachment
    api_response = api_instance.get_attachment_history(attachment_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->get_attachment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  | 
 **page** | **int**| Index of the result page starting from 1. | [optional] [default to 1]
 **page_size** | **int**| Number of items in a result page. Max value: 500 | [optional] [default to 25]

### Return type

[**ArtifactRevisionSearchResult**](ArtifactRevisionSearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_attachment**
> Attachment restore_attachment(attachment_id, version)

Restore attachment to previous version

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 
version = 56 # int | 

try:
    # Restore attachment to previous version
    api_response = api_instance.restore_attachment(attachment_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->restore_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **int**|  | 
 **version** | **int**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attachment**
> Attachment update_attachment(attachment_id, content=content, description=description, description_format=description_format)

Update attachment

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
api_instance = swagger_client.AttachmentApi(swagger_client.ApiClient(configuration))
attachment_id = 56 # int | 
content = 'content_example' # str |  (optional)
description = 'description_example' # str |  (optional)
description_format = 'description_format_example' # str |  (optional)

try:
    # Update attachment
    api_response = api_instance.update_attachment(attachment_id, content=content, description=description, description_format=description_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->update_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

