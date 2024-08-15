# TrackerFieldsStatusPermissions

All field permissions by role for specific status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[TrackerFieldPermissions]**](TrackerFieldPermissions.md) | Permissions | [optional] 

## Example

```python
from openapi_client.models.tracker_fields_status_permissions import TrackerFieldsStatusPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldsStatusPermissions from a JSON string
tracker_fields_status_permissions_instance = TrackerFieldsStatusPermissions.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldsStatusPermissions.to_json())

# convert the object into a dict
tracker_fields_status_permissions_dict = tracker_fields_status_permissions_instance.to_dict()
# create an instance of TrackerFieldsStatusPermissions from a dict
tracker_fields_status_permissions_form_dict = tracker_fields_status_permissions.from_dict(tracker_fields_status_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


