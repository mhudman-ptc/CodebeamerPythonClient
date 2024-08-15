# ChoiceOptionsChoiceOption

Describes a Choice Option item configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**default_in_statuses** | **List[int]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**meanings** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**restricted_to_statuses** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.choice_options_choice_option import ChoiceOptionsChoiceOption

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceOptionsChoiceOption from a JSON string
choice_options_choice_option_instance = ChoiceOptionsChoiceOption.from_json(json)
# print the JSON string representation of the object
print(ChoiceOptionsChoiceOption.to_json())

# convert the object into a dict
choice_options_choice_option_dict = choice_options_choice_option_instance.to_dict()
# create an instance of ChoiceOptionsChoiceOption from a dict
choice_options_choice_option_form_dict = choice_options_choice_option.from_dict(choice_options_choice_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


