# ChoiceWorkConfigItems

Describes a Work Config Items Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_filters** | [**List[ReferenceFilterBasedChoiceReferenceFilter]**](ReferenceFilterBasedChoiceReferenceFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_work_config_items import ChoiceWorkConfigItems

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceWorkConfigItems from a JSON string
choice_work_config_items_instance = ChoiceWorkConfigItems.from_json(json)
# print the JSON string representation of the object
print(ChoiceWorkConfigItems.to_json())

# convert the object into a dict
choice_work_config_items_dict = choice_work_config_items_instance.to_dict()
# create an instance of ChoiceWorkConfigItems from a dict
choice_work_config_items_form_dict = choice_work_config_items.from_dict(choice_work_config_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


