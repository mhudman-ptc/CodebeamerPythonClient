# UserChoiceField

User item type choice field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_values** | **bool** | Multiple values state of a field | [optional] 
**reference_type** | **str** | Type of the contained references | [optional] 

## Example

```python
from openapi_client.models.user_choice_field import UserChoiceField

# TODO update the JSON string below
json = "{}"
# create an instance of UserChoiceField from a JSON string
user_choice_field_instance = UserChoiceField.from_json(json)
# print the JSON string representation of the object
print(UserChoiceField.to_json())

# convert the object into a dict
user_choice_field_dict = user_choice_field_instance.to_dict()
# create an instance of UserChoiceField from a dict
user_choice_field_form_dict = user_choice_field.from_dict(user_choice_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


