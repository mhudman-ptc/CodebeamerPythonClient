# swagger_client.TrackerItemsCommentApi

All URIs are relative to *https://ptc.codebeamer.com/api*

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
> Comment comment_on_tracker_item(item_id, attachments=attachments, comment=comment, comment_format=comment_format)

Comment on a tracker item

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
attachments = 'attachments_example' # str |  (optional)
comment = 'comment_example' # str |  (optional)
comment_format = 'comment_format_example' # str |  (optional)

try:
    # Comment on a tracker item
    api_response = api_instance.comment_on_tracker_item(item_id, attachments=attachments, comment=comment, comment_format=comment_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsCommentApi->comment_on_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **attachments** | **str**|  | [optional] 
 **comment** | **str**|  | [optional] 
 **comment_format** | **str**|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_comment**
> Comment delete_tracker_item_comment(item_id, comment_id)

Delete comment of tracker item by id

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
comment_id = 56 # int | 

try:
    # Delete comment of tracker item by id
    api_response = api_instance.delete_tracker_item_comment(item_id, comment_id)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracker_item_comments**
> delete_tracker_item_comments(item_id)

Delete comments of tracker item by item id

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 

try:
    # Delete comments of tracker item by item id
    api_instance.delete_tracker_item_comments(item_id)
except ApiException as e:
    print("Exception when calling TrackerItemsCommentApi->delete_tracker_item_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_comment_on_tracker_item**
> Comment edit_comment_on_tracker_item(item_id, comment_id, attachments=attachments, comment=comment, comment_format=comment_format)

Edit comment on a tracker item

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
comment_id = 56 # int | 
attachments = 'attachments_example' # str |  (optional)
comment = 'comment_example' # str |  (optional)
comment_format = 'comment_format_example' # str |  (optional)

try:
    # Edit comment on a tracker item
    api_response = api_instance.edit_comment_on_tracker_item(item_id, comment_id, attachments=attachments, comment=comment, comment_format=comment_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsCommentApi->edit_comment_on_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 
 **attachments** | **str**|  | [optional] 
 **comment** | **str**|  | [optional] 
 **comment_format** | **str**|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_comment**
> Comment get_tracker_item_comment(item_id, comment_id)

Get comment of tracker item by id

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
comment_id = 56 # int | 

try:
    # Get comment of tracker item by id
    api_response = api_instance.get_tracker_item_comment(item_id, comment_id)
    pprint(api_response)
except ApiException as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracker_item_comments**
> list[Comment] get_tracker_item_comments(item_id)

Get comments of tracker item

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | Id of a tracker item

try:
    # Get comments of tracker item
    api_response = api_instance.get_tracker_item_comments(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsCommentApi->get_tracker_item_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| Id of a tracker item | 

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_on_comment_of_tracker_item**
> Comment reply_on_comment_of_tracker_item(item_id, comment_id, attachments=attachments, comment=comment, comment_format=comment_format)

Reply on a comment of a tracker item

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
api_instance = swagger_client.TrackerItemsCommentApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | 
comment_id = 56 # int | 
attachments = 'attachments_example' # str |  (optional)
comment = 'comment_example' # str |  (optional)
comment_format = 'comment_format_example' # str |  (optional)

try:
    # Reply on a comment of a tracker item
    api_response = api_instance.reply_on_comment_of_tracker_item(item_id, comment_id, attachments=attachments, comment=comment, comment_format=comment_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackerItemsCommentApi->reply_on_comment_of_tracker_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **comment_id** | **int**|  | 
 **attachments** | **str**|  | [optional] 
 **comment** | **str**|  | [optional] 
 **comment_format** | **str**|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

