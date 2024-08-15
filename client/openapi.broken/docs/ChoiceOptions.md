# ChoiceOptions

Describes a Options Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choice_options** | [**List[ChoiceOptionsChoiceOption]**](ChoiceOptionsChoiceOption.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_options import ChoiceOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceOptions from a JSON string
choice_options_instance = ChoiceOptions.from_json(json)
# print the JSON string representation of the object
print(ChoiceOptions.to_json())

# convert the object into a dict
choice_options_dict = choice_options_instance.to_dict()
# create an instance of ChoiceOptions from a dict
choice_options_form_dict = choice_options.from_dict(choice_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


