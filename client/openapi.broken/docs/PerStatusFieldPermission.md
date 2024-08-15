# PerStatusFieldPermission

Describes a Per Status field permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_permissions_per_status_map** | **Dict[str, List[TrackerFieldPermissionAccessPermission]]** |  | [optional] 

## Example

```python
from openapi_client.models.per_status_field_permission import PerStatusFieldPermission

# TODO update the JSON string below
json = "{}"
# create an instance of PerStatusFieldPermission from a JSON string
per_status_field_permission_instance = PerStatusFieldPermission.from_json(json)
# print the JSON string representation of the object
print(PerStatusFieldPermission.to_json())

# convert the object into a dict
per_status_field_permission_dict = per_status_field_permission_instance.to_dict()
# create an instance of PerStatusFieldPermission from a dict
per_status_field_permission_form_dict = per_status_field_permission.from_dict(per_status_field_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


