# TraceabilityInitialLevelFilter

Settings to filter items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cb_ql** | **str** | cbQL | 
**history_baseline_id** | **int** | Snapshot view of given baseline | [optional] 
**history_date** | **datetime** | Snapshot view of given date | [optional] 
**show_ancestor_items** | **bool** | Show ancestor items | [optional] [default to False]
**show_descendant_items** | **bool** | Show descendant items | [optional] [default to False]

## Example

```python
from openapi_client.models.traceability_initial_level_filter import TraceabilityInitialLevelFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TraceabilityInitialLevelFilter from a JSON string
traceability_initial_level_filter_instance = TraceabilityInitialLevelFilter.from_json(json)
# print the JSON string representation of the object
print(TraceabilityInitialLevelFilter.to_json())

# convert the object into a dict
traceability_initial_level_filter_dict = traceability_initial_level_filter_instance.to_dict()
# create an instance of TraceabilityInitialLevelFilter from a dict
traceability_initial_level_filter_form_dict = traceability_initial_level_filter.from_dict(traceability_initial_level_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


