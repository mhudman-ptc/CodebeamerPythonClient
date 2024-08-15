# ReferenceFilterBasedChoiceReferenceFilter

Describes a Choice Option Field's Reference Filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **int** |  | [optional] 
**domain_type** | **str** |  | [optional] 
**filter_id** | **int** |  | [optional] 
**filter_status_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**target_ids** | **List[int]** |  | [optional] 
**target_permissions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.reference_filter_based_choice_reference_filter import ReferenceFilterBasedChoiceReferenceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceFilterBasedChoiceReferenceFilter from a JSON string
reference_filter_based_choice_reference_filter_instance = ReferenceFilterBasedChoiceReferenceFilter.from_json(json)
# print the JSON string representation of the object
print(ReferenceFilterBasedChoiceReferenceFilter.to_json())

# convert the object into a dict
reference_filter_based_choice_reference_filter_dict = reference_filter_based_choice_reference_filter_instance.to_dict()
# create an instance of ReferenceFilterBasedChoiceReferenceFilter from a dict
reference_filter_based_choice_reference_filter_form_dict = reference_filter_based_choice_reference_filter.from_dict(reference_filter_based_choice_reference_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


