# DecimalFieldValue

Value container of a double field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Double value | [optional] 

## Example

```python
from openapi_client.models.decimal_field_value import DecimalFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalFieldValue from a JSON string
decimal_field_value_instance = DecimalFieldValue.from_json(json)
# print the JSON string representation of the object
print(DecimalFieldValue.to_json())

# convert the object into a dict
decimal_field_value_dict = decimal_field_value_instance.to_dict()
# create an instance of DecimalFieldValue from a dict
decimal_field_value_form_dict = decimal_field_value.from_dict(decimal_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


