# TextFieldValue

Value container of a text field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Text value | [optional] 

## Example

```python
from openapi_client.models.text_field_value import TextFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of TextFieldValue from a JSON string
text_field_value_instance = TextFieldValue.from_json(json)
# print the JSON string representation of the object
print(TextFieldValue.to_json())

# convert the object into a dict
text_field_value_dict = text_field_value_instance.to_dict()
# create an instance of TextFieldValue from a dict
text_field_value_form_dict = text_field_value.from_dict(text_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


