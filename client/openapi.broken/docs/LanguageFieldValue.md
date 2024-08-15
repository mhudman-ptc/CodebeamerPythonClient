# LanguageFieldValue

Value container of a language field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | Language codes | [optional] 

## Example

```python
from openapi_client.models.language_field_value import LanguageFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageFieldValue from a JSON string
language_field_value_instance = LanguageFieldValue.from_json(json)
# print the JSON string representation of the object
print(LanguageFieldValue.to_json())

# convert the object into a dict
language_field_value_dict = language_field_value_instance.to_dict()
# create an instance of LanguageFieldValue from a dict
language_field_value_form_dict = language_field_value.from_dict(language_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


