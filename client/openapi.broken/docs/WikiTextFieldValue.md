# WikiTextFieldValue

Value container of a wiki text field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Wiki text value | [optional] 

## Example

```python
from openapi_client.models.wiki_text_field_value import WikiTextFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of WikiTextFieldValue from a JSON string
wiki_text_field_value_instance = WikiTextFieldValue.from_json(json)
# print the JSON string representation of the object
print(WikiTextFieldValue.to_json())

# convert the object into a dict
wiki_text_field_value_dict = wiki_text_field_value_instance.to_dict()
# create an instance of WikiTextFieldValue from a dict
wiki_text_field_value_form_dict = wiki_text_field_value.from_dict(wiki_text_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


