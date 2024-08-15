# SingleFieldPermission

Describes a Single field permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_permissions** | [**List[TrackerFieldPermissionAccessPermission]**](TrackerFieldPermissionAccessPermission.md) |  | [optional] 

## Example

```python
from openapi_client.models.single_field_permission import SingleFieldPermission

# TODO update the JSON string below
json = "{}"
# create an instance of SingleFieldPermission from a JSON string
single_field_permission_instance = SingleFieldPermission.from_json(json)
# print the JSON string representation of the object
print(SingleFieldPermission.to_json())

# convert the object into a dict
single_field_permission_dict = single_field_permission_instance.to_dict()
# create an instance of SingleFieldPermission from a dict
single_field_permission_form_dict = single_field_permission.from_dict(single_field_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


