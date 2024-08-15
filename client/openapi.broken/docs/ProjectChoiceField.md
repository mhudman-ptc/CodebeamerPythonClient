# ProjectChoiceField

Project item type choice field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_values** | **bool** | Multiple values state of a field | [optional] 
**reference_type** | **str** | Type of the contained references | [optional] 

## Example

```python
from openapi_client.models.project_choice_field import ProjectChoiceField

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectChoiceField from a JSON string
project_choice_field_instance = ProjectChoiceField.from_json(json)
# print the JSON string representation of the object
print(ProjectChoiceField.to_json())

# convert the object into a dict
project_choice_field_dict = project_choice_field_instance.to_dict()
# create an instance of ProjectChoiceField from a dict
project_choice_field_form_dict = project_choice_field.from_dict(project_choice_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


