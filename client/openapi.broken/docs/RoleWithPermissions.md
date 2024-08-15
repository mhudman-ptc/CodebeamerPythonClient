# RoleWithPermissions

Model that contains permissions connected to roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**RoleReference**](RoleReference.md) |  | [optional] 
**tracker_permissions** | [**List[TrackerPermissionReference]**](TrackerPermissionReference.md) | Permission for the role | [optional] 

## Example

```python
from openapi_client.models.role_with_permissions import RoleWithPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of RoleWithPermissions from a JSON string
role_with_permissions_instance = RoleWithPermissions.from_json(json)
# print the JSON string representation of the object
print(RoleWithPermissions.to_json())

# convert the object into a dict
role_with_permissions_dict = role_with_permissions_instance.to_dict()
# create an instance of RoleWithPermissions from a dict
role_with_permissions_form_dict = role_with_permissions.from_dict(role_with_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


