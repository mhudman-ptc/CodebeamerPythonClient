# WikiTextField

Wiki text field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Max length of value of a field | [optional] 
**min** | **int** | Minimum length of value of a field | [optional] 

## Example

```python
from openapi_client.models.wiki_text_field import WikiTextField

# TODO update the JSON string below
json = "{}"
# create an instance of WikiTextField from a JSON string
wiki_text_field_instance = WikiTextField.from_json(json)
# print the JSON string representation of the object
print(WikiTextField.to_json())

# convert the object into a dict
wiki_text_field_dict = wiki_text_field_instance.to_dict()
# create an instance of WikiTextField from a dict
wiki_text_field_form_dict = wiki_text_field.from_dict(wiki_text_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


