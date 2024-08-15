# WikiTextFieldMultiValue

This model holds wiki text field values along with plain text value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plain_text_value** | **str** | Plain text value of wiki text field. | [optional] 
**value** | **str** | Wiki text value | [optional] 

## Example

```python
from openapi_client.models.wiki_text_field_multi_value import WikiTextFieldMultiValue

# TODO update the JSON string below
json = "{}"
# create an instance of WikiTextFieldMultiValue from a JSON string
wiki_text_field_multi_value_instance = WikiTextFieldMultiValue.from_json(json)
# print the JSON string representation of the object
print(WikiTextFieldMultiValue.to_json())

# convert the object into a dict
wiki_text_field_multi_value_dict = wiki_text_field_multi_value_instance.to_dict()
# create an instance of WikiTextFieldMultiValue from a dict
wiki_text_field_multi_value_form_dict = wiki_text_field_multi_value.from_dict(wiki_text_field_multi_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


