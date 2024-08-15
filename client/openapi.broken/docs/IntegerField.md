# IntegerField

Integer field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Maximum value of a field | [optional] 
**min** | **int** | Minimum value of a field | [optional] 

## Example

```python
from openapi_client.models.integer_field import IntegerField

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerField from a JSON string
integer_field_instance = IntegerField.from_json(json)
# print the JSON string representation of the object
print(IntegerField.to_json())

# convert the object into a dict
integer_field_dict = integer_field_instance.to_dict()
# create an instance of IntegerField from a dict
integer_field_form_dict = integer_field.from_dict(integer_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


