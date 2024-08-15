# TrackerBasicInformation

General Tracker information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_use_quick_transitions** | **bool** |  | [optional] 
**color** | **str** |  | [optional] 
**default_layout** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**inbox_id** | **int** |  | [optional] 
**issue_type_id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**only_workflow_actions_can_create_new_referring_items** | **bool** |  | [optional] 
**project_id** | **int** |  | [optional] 
**shared_in_working_sets** | **bool** |  | [optional] 
**show_ancestor_items** | **bool** |  | [optional] 
**show_descendant_items** | **bool** |  | [optional] 
**template** | **bool** |  | [optional] 
**template_id** | **int** |  | [optional] 
**tracker_id** | **int** |  | [optional] 
**workflow_is_active** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_basic_information import TrackerBasicInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerBasicInformation from a JSON string
tracker_basic_information_instance = TrackerBasicInformation.from_json(json)
# print the JSON string representation of the object
print(TrackerBasicInformation.to_json())

# convert the object into a dict
tracker_basic_information_dict = tracker_basic_information_instance.to_dict()
# create an instance of TrackerBasicInformation from a dict
tracker_basic_information_form_dict = tracker_basic_information.from_dict(tracker_basic_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


