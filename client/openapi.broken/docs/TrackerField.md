# TrackerField

This model represents a whole Tracker Field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_rule** | **str** | The Aggregation Rule for a specific Field. | [optional] 
**choice_option_setting** | [**BaseTrackerFieldChoiceOption**](BaseTrackerFieldChoiceOption.md) |  | [optional] 
**computed_as** | **str** |  | [optional] 
**computed_field_references** | [**List[TrackerFieldComputedFieldReference]**](TrackerFieldComputedFieldReference.md) |  | [optional] 
**date_field_settings** | [**TrackerFieldDateFieldSettings**](TrackerFieldDateFieldSettings.md) |  | [optional] 
**default_values_in_statuses** | **Dict[str, str]** |  | [optional] 
**dependency** | [**TrackerFieldDependency**](TrackerFieldDependency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**digits** | **int** |  | [optional] 
**distribution_rule** | **str** | The Distribution Rule of a specific Field. | [optional] 
**global_type_ids** | **List[int]** |  | [optional] 
**height** | **int** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**hide_if_formula** | **str** |  | [optional] 
**hide_if_formula_same_as_field_id** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**listable** | **bool** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**mandatory_if_formula** | **str** |  | [optional] 
**mandatory_if_formula_same_as_field_id** | **int** |  | [optional] 
**max_value** | **str** |  | [optional] 
**min_value** | **str** |  | [optional] 
**multiple_selection** | **bool** |  | [optional] 
**new_line** | **bool** |  | [optional] 
**omit_merge** | **bool** |  | [optional] 
**omit_suspected_when_change** | **bool** |  | [optional] 
**permission** | [**BaseTrackerFieldPermission**](BaseTrackerFieldPermission.md) |  | [optional] 
**position** | **int** |  | [optional] 
**propagate_dependencies** | **bool** |  | [optional] 
**propagate_suspect** | **bool** |  | [optional] 
**reference_id** | **int** |  | [optional] 
**reversed_suspect** | **bool** |  | [optional] 
**service_desk_field** | [**TrackerFieldServiceDeskField**](TrackerFieldServiceDeskField.md) |  | [optional] 
**span** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type_id** | **int** |  | [optional] 
**union** | **bool** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field import TrackerField

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerField from a JSON string
tracker_field_instance = TrackerField.from_json(json)
# print the JSON string representation of the object
print(TrackerField.to_json())

# convert the object into a dict
tracker_field_dict = tracker_field_instance.to_dict()
# create an instance of TrackerField from a dict
tracker_field_form_dict = tracker_field.from_dict(tracker_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


