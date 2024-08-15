# TrackerItemHistory

Tracker item history containing all versions of an item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[TrackerItemHistoryRevision]**](TrackerItemHistoryRevision.md) | List of version changes. | [optional] 

## Example

```python
from openapi_client.models.tracker_item_history import TrackerItemHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemHistory from a JSON string
tracker_item_history_instance = TrackerItemHistory.from_json(json)
# print the JSON string representation of the object
print(TrackerItemHistory.to_json())

# convert the object into a dict
tracker_item_history_dict = tracker_item_history_instance.to_dict()
# create an instance of TrackerItemHistory from a dict
tracker_item_history_form_dict = tracker_item_history.from_dict(tracker_item_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


