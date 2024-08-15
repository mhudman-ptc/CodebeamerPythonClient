# UpdateTrackerItemChildrenRequest

Tracker item child update request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Child items to update | [optional] 

## Example

```python
from openapi_client.models.update_tracker_item_children_request import UpdateTrackerItemChildrenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrackerItemChildrenRequest from a JSON string
update_tracker_item_children_request_instance = UpdateTrackerItemChildrenRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTrackerItemChildrenRequest.to_json())

# convert the object into a dict
update_tracker_item_children_request_dict = update_tracker_item_children_request_instance.to_dict()
# create an instance of UpdateTrackerItemChildrenRequest from a dict
update_tracker_item_children_request_form_dict = update_tracker_item_children_request.from_dict(update_tracker_item_children_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


