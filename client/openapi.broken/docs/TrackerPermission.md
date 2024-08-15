# TrackerPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the permission | [optional] 
**id** | **int** | Id of the entity | [optional] 
**label** | **str** | Variable name of the permission | [optional] 
**name** | **str** | Name of the entity | [optional] 

## Example

```python
from openapi_client.models.tracker_permission import TrackerPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerPermission from a JSON string
tracker_permission_instance = TrackerPermission.from_json(json)
# print the JSON string representation of the object
print(TrackerPermission.to_json())

# convert the object into a dict
tracker_permission_dict = tracker_permission_instance.to_dict()
# create an instance of TrackerPermission from a dict
tracker_permission_form_dict = tracker_permission.from_dict(tracker_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


