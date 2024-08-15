# TrackerItemHistoryRevision

Revision history entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**List[AbstractTrackerItemChange]**](AbstractTrackerItemChange.md) | Changes happened between the previous and current revision. | [optional] 
**item_revision** | [**TrackerItemRevision**](TrackerItemRevision.md) |  | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_history_revision import TrackerItemHistoryRevision

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemHistoryRevision from a JSON string
tracker_item_history_revision_instance = TrackerItemHistoryRevision.from_json(json)
# print the JSON string representation of the object
print(TrackerItemHistoryRevision.to_json())

# convert the object into a dict
tracker_item_history_revision_dict = tracker_item_history_revision_instance.to_dict()
# create an instance of TrackerItemHistoryRevision from a dict
tracker_item_history_revision_form_dict = tracker_item_history_revision.from_dict(tracker_item_history_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


