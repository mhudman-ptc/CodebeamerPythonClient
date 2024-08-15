# TrackerItemReference

Reference to a tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angular_icon** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**propagate_suspects** | **bool** |  | [optional] 
**reference_data** | [**TrackerItemReferenceData**](TrackerItemReferenceData.md) |  | [optional] 
**test_step_reuse** | **bool** |  | [optional] 
**tracker_key** | **str** |  | [optional] 
**tracker_type_id** | **int** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_reference import TrackerItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReference from a JSON string
tracker_item_reference_instance = TrackerItemReference.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReference.to_json())

# convert the object into a dict
tracker_item_reference_dict = tracker_item_reference_instance.to_dict()
# create an instance of TrackerItemReference from a dict
tracker_item_reference_form_dict = tracker_item_reference.from_dict(tracker_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


