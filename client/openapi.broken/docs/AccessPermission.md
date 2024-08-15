# AccessPermission

Access permission of specific role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** | Access level | [optional] 
**field** | [**FieldReference**](FieldReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**role** | [**RoleReference**](RoleReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_permission import AccessPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPermission from a JSON string
access_permission_instance = AccessPermission.from_json(json)
# print the JSON string representation of the object
print(AccessPermission.to_json())

# convert the object into a dict
access_permission_dict = access_permission_instance.to_dict()
# create an instance of AccessPermission from a dict
access_permission_form_dict = access_permission.from_dict(access_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


