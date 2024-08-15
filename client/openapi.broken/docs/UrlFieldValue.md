# UrlFieldValue

Value container of an url field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the field | [optional] 

## Example

```python
from openapi_client.models.url_field_value import UrlFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of UrlFieldValue from a JSON string
url_field_value_instance = UrlFieldValue.from_json(json)
# print the JSON string representation of the object
print(UrlFieldValue.to_json())

# convert the object into a dict
url_field_value_dict = url_field_value_instance.to_dict()
# create an instance of UrlFieldValue from a dict
url_field_value_form_dict = url_field_value.from_dict(url_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


