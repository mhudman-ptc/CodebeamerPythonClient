# TrackerItemRowChange

Change item for a tracker item field row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_number** | **int** | Index of the changed row | [optional] 

## Example

```python
from openapi_client.models.tracker_item_row_change import TrackerItemRowChange

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemRowChange from a JSON string
tracker_item_row_change_instance = TrackerItemRowChange.from_json(json)
# print the JSON string representation of the object
print(TrackerItemRowChange.to_json())

# convert the object into a dict
tracker_item_row_change_dict = tracker_item_row_change_instance.to_dict()
# create an instance of TrackerItemRowChange from a dict
tracker_item_row_change_form_dict = tracker_item_row_change.from_dict(tracker_item_row_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


