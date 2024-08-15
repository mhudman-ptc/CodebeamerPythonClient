# UserGroup

Group of a codebeamer user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**description** | **str** | Description of a user group | [optional] 
**id** | **int** | Id of the entity | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**name** | **str** | Name of the entity | [optional] 

## Example

```python
from openapi_client.models.user_group import UserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroup from a JSON string
user_group_instance = UserGroup.from_json(json)
# print the JSON string representation of the object
print(UserGroup.to_json())

# convert the object into a dict
user_group_dict = user_group_instance.to_dict()
# create an instance of UserGroup from a dict
user_group_form_dict = user_group.from_dict(user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


