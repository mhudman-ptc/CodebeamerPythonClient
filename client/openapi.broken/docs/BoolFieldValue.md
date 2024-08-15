# BoolFieldValue

Value container of a bool field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | Value of the field | [optional] 

## Example

```python
from openapi_client.models.bool_field_value import BoolFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of BoolFieldValue from a JSON string
bool_field_value_instance = BoolFieldValue.from_json(json)
# print the JSON string representation of the object
print(BoolFieldValue.to_json())

# convert the object into a dict
bool_field_value_dict = bool_field_value_instance.to_dict()
# create an instance of BoolFieldValue from a dict
bool_field_value_form_dict = bool_field_value.from_dict(bool_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


