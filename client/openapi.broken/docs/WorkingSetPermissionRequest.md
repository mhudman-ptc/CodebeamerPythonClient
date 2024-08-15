# WorkingSetPermissionRequest

Request model trackers, roles and permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[TrackerPermissionReference]**](TrackerPermissionReference.md) | Permission references. | [optional] 
**roles** | [**List[RoleReference]**](RoleReference.md) | Role references. | [optional] 
**trackers** | [**List[TrackerReference]**](TrackerReference.md) | Tracker references. | [optional] 

## Example

```python
from openapi_client.models.working_set_permission_request import WorkingSetPermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetPermissionRequest from a JSON string
working_set_permission_request_instance = WorkingSetPermissionRequest.from_json(json)
# print the JSON string representation of the object
print(WorkingSetPermissionRequest.to_json())

# convert the object into a dict
working_set_permission_request_dict = working_set_permission_request_instance.to_dict()
# create an instance of WorkingSetPermissionRequest from a dict
working_set_permission_request_form_dict = working_set_permission_request.from_dict(working_set_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


