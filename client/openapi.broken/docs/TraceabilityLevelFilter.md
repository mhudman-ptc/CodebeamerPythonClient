# TraceabilityLevelFilter

Traceability level filter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cb_ql** | **str** | cbQL | 
**folders_and_information** | **bool** | Show folders and information | [optional] [default to False]
**history_baseline_id** | **int** | History Baseline Id - Snapshot view of the given baseline | [optional] 
**history_date** | **datetime** | History Date - Snapshot view of the given date | [optional] 
**incoming_association** | **bool** | Show incoming association | [optional] [default to True]
**incoming_reference** | **bool** | Show incoming references | [optional] [default to True]
**outgoing_association** | **bool** | Show outgoing association | [optional] [default to True]
**outgoing_reference** | **bool** | Show outgoing references | [optional] [default to True]
**previous_level_items** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) | Previous Level Items | [optional] 
**show_test_step_references** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.traceability_level_filter import TraceabilityLevelFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TraceabilityLevelFilter from a JSON string
traceability_level_filter_instance = TraceabilityLevelFilter.from_json(json)
# print the JSON string representation of the object
print(TraceabilityLevelFilter.to_json())

# convert the object into a dict
traceability_level_filter_dict = traceability_level_filter_instance.to_dict()
# create an instance of TraceabilityLevelFilter from a dict
traceability_level_filter_form_dict = traceability_level_filter.from_dict(traceability_level_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


