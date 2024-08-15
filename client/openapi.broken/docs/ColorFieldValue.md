# ColorFieldValue

Value container of a color field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Hex code of the color | [optional] 

## Example

```python
from openapi_client.models.color_field_value import ColorFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of ColorFieldValue from a JSON string
color_field_value_instance = ColorFieldValue.from_json(json)
# print the JSON string representation of the object
print(ColorFieldValue.to_json())

# convert the object into a dict
color_field_value_dict = color_field_value_instance.to_dict()
# create an instance of ColorFieldValue from a dict
color_field_value_form_dict = color_field_value.from_dict(color_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


