# TrackerFieldPermissions

Tracker field permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_permissions** | [**List[TrackerFieldStatusPermissions]**](TrackerFieldStatusPermissions.md) | Permissions for the given field | [optional] 
**field_reference** | [**FieldReference**](FieldReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_permissions import TrackerFieldPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldPermissions from a JSON string
tracker_field_permissions_instance = TrackerFieldPermissions.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldPermissions.to_json())

# convert the object into a dict
tracker_field_permissions_dict = tracker_field_permissions_instance.to_dict()
# create an instance of TrackerFieldPermissions from a dict
tracker_field_permissions_form_dict = tracker_field_permissions.from_dict(tracker_field_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


