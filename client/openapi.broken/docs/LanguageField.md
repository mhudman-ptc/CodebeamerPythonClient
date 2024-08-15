# LanguageField

Language field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_options** | **List[str]** |  | [optional] 
**multiple_values** | **bool** | Multiple values state of a field | [optional] 

## Example

```python
from openapi_client.models.language_field import LanguageField

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageField from a JSON string
language_field_instance = LanguageField.from_json(json)
# print the JSON string representation of the object
print(LanguageField.to_json())

# convert the object into a dict
language_field_dict = language_field_instance.to_dict()
# create an instance of LanguageField from a dict
language_field_form_dict = language_field.from_dict(language_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


