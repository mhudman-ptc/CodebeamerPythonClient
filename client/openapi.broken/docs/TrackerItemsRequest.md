# TrackerItemsRequest

Request model for multiple items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Item references. | [optional] 
**type** | **str** | Type of a ItemsRequest | [optional] 

## Example

```python
from openapi_client.models.tracker_items_request import TrackerItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemsRequest from a JSON string
tracker_items_request_instance = TrackerItemsRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerItemsRequest.to_json())

# convert the object into a dict
tracker_items_request_dict = tracker_items_request_instance.to_dict()
# create an instance of TrackerItemsRequest from a dict
tracker_items_request_form_dict = tracker_items_request.from_dict(tracker_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


