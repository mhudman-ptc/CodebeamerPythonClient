# TrackerItemRevision

Tracker item revision identifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Tracker item id | [optional] 
**version** | **int** | Tracker item version | [optional] 

## Example

```python
from openapi_client.models.tracker_item_revision import TrackerItemRevision

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemRevision from a JSON string
tracker_item_revision_instance = TrackerItemRevision.from_json(json)
# print the JSON string representation of the object
print(TrackerItemRevision.to_json())

# convert the object into a dict
tracker_item_revision_dict = tracker_item_revision_instance.to_dict()
# create an instance of TrackerItemRevision from a dict
tracker_item_revision_form_dict = tracker_item_revision.from_dict(tracker_item_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


