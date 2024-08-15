# swagger_client.WikisCommentApi

All URIs are relative to *https://ptc.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comment_on_wiki**](WikisCommentApi.md#comment_on_wiki) | **POST** /v3/wikipages/{wikiId}/comments | Comment on a wiki page
[**get_attachment_by_name**](WikisCommentApi.md#get_attachment_by_name) | **GET** /v3/wikipages/{wikiId}/attachments | Get attachment of wiki page by file name

# **comment_on_wiki**
> list[AttachmentReference] comment_on_wiki(wiki_id, attachments=attachments, comment=comment, comment_format=comment_format)

Comment on a wiki page

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
api_instance = swagger_client.WikisCommentApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | 
attachments = 'attachments_example' # str |  (optional)
comment = 'comment_example' # str |  (optional)
comment_format = 'comment_format_example' # str |  (optional)

try:
    # Comment on a wiki page
    api_response = api_instance.comment_on_wiki(wiki_id, attachments=attachments, comment=comment, comment_format=comment_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikisCommentApi->comment_on_wiki: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**|  | 
 **attachments** | **str**|  | [optional] 
 **comment** | **str**|  | [optional] 
 **comment_format** | **str**|  | [optional] 

### Return type

[**list[AttachmentReference]**](AttachmentReference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_by_name**
> Attachment get_attachment_by_name(wiki_id, file_name)

Get attachment of wiki page by file name

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
api_instance = swagger_client.WikisCommentApi(swagger_client.ApiClient(configuration))
wiki_id = 56 # int | 
file_name = 'file_name_example' # str | 

try:
    # Get attachment of wiki page by file name
    api_response = api_instance.get_attachment_by_name(wiki_id, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WikisCommentApi->get_attachment_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**|  | 
 **file_name** | **str**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

