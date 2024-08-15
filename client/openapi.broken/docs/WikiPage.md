# WikiPage

Wiki page details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_comment** | **str** | Summary of the changes in this wiki page version | [optional] 
**child_pages** | [**List[WikiPageReference]**](WikiPageReference.md) | Child pages of the current Wiki page | [optional] [readonly] 
**comments** | [**List[AttachmentReference]**](AttachmentReference.md) | Comments/attachments associated with the wiki page | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**id** | **int** | Id of the entity | [optional] 
**markup** | **str** | Content markup of the wiki page | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**name** | **str** | Name of the entity | [optional] 
**parent** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**version** | **int** | Version of the wiki page | [optional] 

## Example

```python
from openapi_client.models.wiki_page import WikiPage

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPage from a JSON string
wiki_page_instance = WikiPage.from_json(json)
# print the JSON string representation of the object
print(WikiPage.to_json())

# convert the object into a dict
wiki_page_dict = wiki_page_instance.to_dict()
# create an instance of WikiPage from a dict
wiki_page_form_dict = wiki_page.from_dict(wiki_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


