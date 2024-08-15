# DecimalField

Decimal field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **float** | Maximum value of a field | [optional] 
**min** | **float** | Minimum value of a field | [optional] 

## Example

```python
from openapi_client.models.decimal_field import DecimalField

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalField from a JSON string
decimal_field_instance = DecimalField.from_json(json)
# print the JSON string representation of the object
print(DecimalField.to_json())

# convert the object into a dict
decimal_field_dict = decimal_field_instance.to_dict()
# create an instance of DecimalField from a dict
decimal_field_form_dict = decimal_field.from_dict(decimal_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


