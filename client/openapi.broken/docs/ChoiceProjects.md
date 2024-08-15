# ChoiceProjects

Describes a Projects Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_filters** | [**List[ReferenceFilterBasedChoiceReferenceFilter]**](ReferenceFilterBasedChoiceReferenceFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_projects import ChoiceProjects

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceProjects from a JSON string
choice_projects_instance = ChoiceProjects.from_json(json)
# print the JSON string representation of the object
print(ChoiceProjects.to_json())

# convert the object into a dict
choice_projects_dict = choice_projects_instance.to_dict()
# create an instance of ChoiceProjects from a dict
choice_projects_form_dict = choice_projects.from_dict(choice_projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


