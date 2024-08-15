# TrackerItemMoveRequest

Request for Tracker Items move.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_mapping** | [**List[TrackerItemFieldMappingPair]**](TrackerItemFieldMappingPair.md) | Field mappings between the Source Tacker and the Target Tracker. | 
**items** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Optional Tracker Item list. If not provided all Tracker Items from the Source Tracker are moved. | [optional] 
**source_tracker** | [**TrackerReference**](TrackerReference.md) |  | 
**target_tracker** | [**TrackerReference**](TrackerReference.md) |  | 

## Example

```python
from openapi_client.models.tracker_item_move_request import TrackerItemMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemMoveRequest from a JSON string
tracker_item_move_request_instance = TrackerItemMoveRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerItemMoveRequest.to_json())

# convert the object into a dict
tracker_item_move_request_dict = tracker_item_move_request_instance.to_dict()
# create an instance of TrackerItemMoveRequest from a dict
tracker_item_move_request_form_dict = tracker_item_move_request.from_dict(tracker_item_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


