# AttachmentSearchResult

One page of attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) | Found attachments | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.attachment_search_result import AttachmentSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSearchResult from a JSON string
attachment_search_result_instance = AttachmentSearchResult.from_json(json)
# print the JSON string representation of the object
print(AttachmentSearchResult.to_json())

# convert the object into a dict
attachment_search_result_dict = attachment_search_result_instance.to_dict()
# create an instance of AttachmentSearchResult from a dict
attachment_search_result_form_dict = attachment_search_result.from_dict(attachment_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


