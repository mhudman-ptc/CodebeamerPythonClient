# IntegerFieldValue

Value container of a integer field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Integer value | [optional] 

## Example

```python
from openapi_client.models.integer_field_value import IntegerFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerFieldValue from a JSON string
integer_field_value_instance = IntegerFieldValue.from_json(json)
# print the JSON string representation of the object
print(IntegerFieldValue.to_json())

# convert the object into a dict
integer_field_value_dict = integer_field_value_instance.to_dict()
# create an instance of IntegerFieldValue from a dict
integer_field_value_form_dict = integer_field_value.from_dict(integer_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


