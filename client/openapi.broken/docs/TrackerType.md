# TrackerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branchable** | **bool** | True if tracker type is branchable | [optional] 
**color** | **str** | Color of a tracker type | [optional] 
**doc_edit_view** | **bool** | True if tracker type has document view | [optional] 
**editor_url** | **str** | Editor URL of a tracker type | [optional] 
**id** | **int** | Id of the entity | [optional] 
**item_icon_url** | **str** | Item icon URL of a tracker type | [optional] 
**name** | **str** | Name of the entity | [optional] 
**outline** | **bool** | True if outline is enabled | [optional] 
**tracker_icon_url** | **str** | Tracker icon URL of a tracker type | [optional] 
**url_link_format** | **str** | URL link format of a tracker type | [optional] 
**var_name** | **str** | Internal/variable name of a tracker type | [optional] 

## Example

```python
from openapi_client.models.tracker_type import TrackerType

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerType from a JSON string
tracker_type_instance = TrackerType.from_json(json)
# print the JSON string representation of the object
print(TrackerType.to_json())

# convert the object into a dict
tracker_type_dict = tracker_type_instance.to_dict()
# create an instance of TrackerType from a dict
tracker_type_form_dict = tracker_type.from_dict(tracker_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


