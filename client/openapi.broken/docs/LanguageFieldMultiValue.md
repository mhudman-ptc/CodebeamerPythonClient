# LanguageFieldMultiValue

This model holds language field values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_selection** | **bool** | Is field applicable for multiple select. | [optional] 
**values** | **List[str]** | Language codes | [optional] 

## Example

```python
from openapi_client.models.language_field_multi_value import LanguageFieldMultiValue

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageFieldMultiValue from a JSON string
language_field_multi_value_instance = LanguageFieldMultiValue.from_json(json)
# print the JSON string representation of the object
print(LanguageFieldMultiValue.to_json())

# convert the object into a dict
language_field_multi_value_dict = language_field_multi_value_instance.to_dict()
# create an instance of LanguageFieldMultiValue from a dict
language_field_multi_value_form_dict = language_field_multi_value.from_dict(language_field_multi_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


