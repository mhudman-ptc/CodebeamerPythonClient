# RepositoryChoiceField

Repository type choice field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_values** | **bool** | Multiple values state of a field | [optional] 
**reference_type** | **str** | Type of the contained references | [optional] 

## Example

```python
from openapi_client.models.repository_choice_field import RepositoryChoiceField

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryChoiceField from a JSON string
repository_choice_field_instance = RepositoryChoiceField.from_json(json)
# print the JSON string representation of the object
print(RepositoryChoiceField.to_json())

# convert the object into a dict
repository_choice_field_dict = repository_choice_field_instance.to_dict()
# create an instance of RepositoryChoiceField from a dict
repository_choice_field_form_dict = repository_choice_field.from_dict(repository_choice_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

