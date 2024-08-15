# openapi_client.WikisCommentApi

All URIs are relative to *https://nvidiatrial.codebeamer.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comment_on_wiki**](WikisCommentApi.md#comment_on_wiki) | **POST** /v3/wikipages/{wikiId}/comments | Comment on a wiki page
[**get_attachment_by_name**](WikisCommentApi.md#get_attachment_by_name) | **GET** /v3/wikipages/{wikiId}/attachments | Get attachment of wiki page by file name


# **comment_on_wiki**
> List[AttachmentReference] comment_on_wiki(wiki_id, comment, attachments=attachments, comment_format=comment_format)

Comment on a wiki page

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.attachment_reference import AttachmentReference
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
    api_instance = openapi_client.WikisCommentApi(api_client)
    wiki_id = 56 # int | 
    comment = 'comment_example' # str | Text of a comment
    attachments = None # bytearray | Attachments of a comment (optional)
    comment_format = 'PlainText' # str | Format of a comment (optional) (default to 'PlainText')

    try:
        # Comment on a wiki page
        api_response = api_instance.comment_on_wiki(wiki_id, comment, attachments=attachments, comment_format=comment_format)
        print("The response of WikisCommentApi->comment_on_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikisCommentApi->comment_on_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**|  | 
 **comment** | **str**| Text of a comment | 
 **attachments** | **bytearray**| Attachments of a comment | [optional] 
 **comment_format** | **str**| Format of a comment | [optional] [default to &#39;PlainText&#39;]

### Return type

[**List[AttachmentReference]**](AttachmentReference.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment created successfully |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Wiki page not found |  -  |
**429** | Too many requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_by_name**
> Attachment get_attachment_by_name(wiki_id, file_name)

Get attachment of wiki page by file name

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
    api_instance = openapi_client.WikisCommentApi(api_client)
    wiki_id = 56 # int | 
    file_name = 'file_name_example' # str | 

    try:
        # Get attachment of wiki page by file name
        api_response = api_instance.get_attachment_by_name(wiki_id, file_name)
        print("The response of WikisCommentApi->get_attachment_by_name:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment of wiki page |  -  |
**400** | Bad Request |  -  |
**401** | Authentication is required |  -  |
**403** | Authorization is required |  -  |
**404** | Wiki page / Attachment not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

