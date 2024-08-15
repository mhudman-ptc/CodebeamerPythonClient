# ChoiceRepositories

Describes a Repositories Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_filters** | [**List[ReferenceFilterBasedChoiceReferenceFilter]**](ReferenceFilterBasedChoiceReferenceFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_repositories import ChoiceRepositories

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceRepositories from a JSON string
choice_repositories_instance = ChoiceRepositories.from_json(json)
# print the JSON string representation of the object
print(ChoiceRepositories.to_json())

# convert the object into a dict
choice_repositories_dict = choice_repositories_instance.to_dict()
# create an instance of ChoiceRepositories from a dict
choice_repositories_form_dict = choice_repositories.from_dict(choice_repositories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


