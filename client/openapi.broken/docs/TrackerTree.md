# TrackerTree

Properties of tracker tree

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TrackerTree]**](TrackerTree.md) |  | [optional] 
**is_folder** | **bool** | Folder or tracker | [optional] 
**text** | **str** | Name of a folder | [optional] 
**tracker_id** | **int** | Id of the tracker | [optional] 

## Example

```python
from openapi_client.models.tracker_tree import TrackerTree

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerTree from a JSON string
tracker_tree_instance = TrackerTree.from_json(json)
# print the JSON string representation of the object
print(TrackerTree.to_json())

# convert the object into a dict
tracker_tree_dict = tracker_tree_instance.to_dict()
# create an instance of TrackerTree from a dict
tracker_tree_form_dict = tracker_tree.from_dict(tracker_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


