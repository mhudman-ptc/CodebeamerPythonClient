# ProjectMemberPermissions

Project member permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[RoleReference]**](RoleReference.md) | Role references | [optional] 

## Example

```python
from openapi_client.models.project_member_permissions import ProjectMemberPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMemberPermissions from a JSON string
project_member_permissions_instance = ProjectMemberPermissions.from_json(json)
# print the JSON string representation of the object
print(ProjectMemberPermissions.to_json())

# convert the object into a dict
project_member_permissions_dict = project_member_permissions_instance.to_dict()
# create an instance of ProjectMemberPermissions from a dict
project_member_permissions_form_dict = project_member_permissions.from_dict(project_member_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


