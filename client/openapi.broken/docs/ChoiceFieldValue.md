# ChoiceFieldValue

Reference container of a choice option field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AbstractReference]**](AbstractReference.md) | Values of the choice option field | [optional] 

## Example

```python
from openapi_client.models.choice_field_value import ChoiceFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceFieldValue from a JSON string
choice_field_value_instance = ChoiceFieldValue.from_json(json)
# print the JSON string representation of the object
print(ChoiceFieldValue.to_json())

# convert the object into a dict
choice_field_value_dict = choice_field_value_instance.to_dict()
# create an instance of ChoiceFieldValue from a dict
choice_field_value_form_dict = choice_field_value.from_dict(choice_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


