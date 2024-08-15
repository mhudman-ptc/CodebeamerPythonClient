# TextField

Text field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Max length of value of a field | [optional] 
**min** | **int** | Minimum length of value of a field | [optional] 

## Example

```python
from openapi_client.models.text_field import TextField

# TODO update the JSON string below
json = "{}"
# create an instance of TextField from a JSON string
text_field_instance = TextField.from_json(json)
# print the JSON string representation of the object
print(TextField.to_json())

# convert the object into a dict
text_field_dict = text_field_instance.to_dict()
# create an instance of TextField from a dict
text_field_form_dict = text_field.from_dict(text_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


