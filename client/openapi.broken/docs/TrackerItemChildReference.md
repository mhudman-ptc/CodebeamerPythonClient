# TrackerItemChildReference

Reference to a child item in the tracker outline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Ordinal in the tracker outline. | 
**item_reference** | [**TrackerItemReference**](TrackerItemReference.md) |  | 

## Example

```python
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemChildReference from a JSON string
tracker_item_child_reference_instance = TrackerItemChildReference.from_json(json)
# print the JSON string representation of the object
print(TrackerItemChildReference.to_json())

# convert the object into a dict
tracker_item_child_reference_dict = tracker_item_child_reference_instance.to_dict()
# create an instance of TrackerItemChildReference from a dict
tracker_item_child_reference_form_dict = tracker_item_child_reference.from_dict(tracker_item_child_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


