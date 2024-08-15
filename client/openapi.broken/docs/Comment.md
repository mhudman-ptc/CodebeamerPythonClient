# Comment

Comment of a tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Attachment]**](Attachment.md) | Attachments of a comment | [optional] 
**comment** | **str** | Text of a comment | [optional] 
**comment_format** | **str** | Format of a comment | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**id** | **int** | Id of the entity | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**name** | **str** | Name of the entity | [optional] 
**parent** | [**CommentReference**](CommentReference.md) |  | [optional] 
**version** | **int** | Version of a comment | [optional] 

## Example

```python
from openapi_client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_form_dict = comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


