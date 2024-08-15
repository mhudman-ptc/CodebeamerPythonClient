# TrackerFieldPermissionAccessPermission

Describes an atomic permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | The level of the access. | [optional] 
**subject_id** | **int** |  | [optional] 
**subject_type** | **str** | The type of the subject of the permission. | [optional] 

## Example

```python
from openapi_client.models.tracker_field_permission_access_permission import TrackerFieldPermissionAccessPermission

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldPermissionAccessPermission from a JSON string
tracker_field_permission_access_permission_instance = TrackerFieldPermissionAccessPermission.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldPermissionAccessPermission.to_json())

# convert the object into a dict
tracker_field_permission_access_permission_dict = tracker_field_permission_access_permission_instance.to_dict()
# create an instance of TrackerFieldPermissionAccessPermission from a dict
tracker_field_permission_access_permission_form_dict = tracker_field_permission_access_permission.from_dict(tracker_field_permission_access_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


