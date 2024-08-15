# OptionChoiceField

Option type choice field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_values** | **bool** | Multiple values state of a field | [optional] 
**options** | [**List[ChoiceOptionReference]**](ChoiceOptionReference.md) | Available options of a choice field | [optional] 
**reference_type** | **str** | Type of the contained references | [optional] 

## Example

```python
from openapi_client.models.option_choice_field import OptionChoiceField

# TODO update the JSON string below
json = "{}"
# create an instance of OptionChoiceField from a JSON string
option_choice_field_instance = OptionChoiceField.from_json(json)
# print the JSON string representation of the object
print(OptionChoiceField.to_json())

# convert the object into a dict
option_choice_field_dict = option_choice_field_instance.to_dict()
# create an instance of OptionChoiceField from a dict
option_choice_field_form_dict = option_choice_field.from_dict(option_choice_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


