# TrackerItemReferenceData

Properties of a tracker item reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suspect_propagation** | **str** | Type of suspect propagation | [optional] 

## Example

```python
from openapi_client.models.tracker_item_reference_data import TrackerItemReferenceData

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReferenceData from a JSON string
tracker_item_reference_data_instance = TrackerItemReferenceData.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReferenceData.to_json())

# convert the object into a dict
tracker_item_reference_data_dict = tracker_item_reference_data_instance.to_dict()
# create an instance of TrackerItemReferenceData from a dict
tracker_item_reference_data_form_dict = tracker_item_reference_data.from_dict(tracker_item_reference_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


