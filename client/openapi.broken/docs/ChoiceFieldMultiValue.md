# ChoiceFieldMultiValue

This model holds choice field values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_selection** | **bool** | Is field applicable for multiple select. | [optional] 
**values** | [**List[AbstractReference]**](AbstractReference.md) | Values of the choice option field | [optional] 

## Example

```python
from openapi_client.models.choice_field_multi_value import ChoiceFieldMultiValue

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceFieldMultiValue from a JSON string
choice_field_multi_value_instance = ChoiceFieldMultiValue.from_json(json)
# print the JSON string representation of the object
print(ChoiceFieldMultiValue.to_json())

# convert the object into a dict
choice_field_multi_value_dict = choice_field_multi_value_instance.to_dict()
# create an instance of ChoiceFieldMultiValue from a dict
choice_field_multi_value_form_dict = choice_field_multi_value.from_dict(choice_field_multi_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


