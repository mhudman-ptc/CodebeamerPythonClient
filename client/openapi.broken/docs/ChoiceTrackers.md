# ChoiceTrackers

Describes a Trackers Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_filters** | [**List[ReferenceFilterBasedChoiceReferenceFilter]**](ReferenceFilterBasedChoiceReferenceFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_trackers import ChoiceTrackers

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceTrackers from a JSON string
choice_trackers_instance = ChoiceTrackers.from_json(json)
# print the JSON string representation of the object
print(ChoiceTrackers.to_json())

# convert the object into a dict
choice_trackers_dict = choice_trackers_instance.to_dict()
# create an instance of ChoiceTrackers from a dict
choice_trackers_form_dict = choice_trackers.from_dict(choice_trackers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


