# ChoiceMembers

Describes a Members Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_type_data_source_types** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.choice_members import ChoiceMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceMembers from a JSON string
choice_members_instance = ChoiceMembers.from_json(json)
# print the JSON string representation of the object
print(ChoiceMembers.to_json())

# convert the object into a dict
choice_members_dict = choice_members_instance.to_dict()
# create an instance of ChoiceMembers from a dict
choice_members_form_dict = choice_members.from_dict(choice_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


