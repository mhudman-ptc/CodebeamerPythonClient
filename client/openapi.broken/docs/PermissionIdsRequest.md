# PermissionIdsRequest

Request model for multiple items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[TrackerPermissionReference]**](TrackerPermissionReference.md) | Permission references. | [optional] 

## Example

```python
from openapi_client.models.permission_ids_request import PermissionIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionIdsRequest from a JSON string
permission_ids_request_instance = PermissionIdsRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionIdsRequest.to_json())

# convert the object into a dict
permission_ids_request_dict = permission_ids_request_instance.to_dict()
# create an instance of PermissionIdsRequest from a dict
permission_ids_request_form_dict = permission_ids_request.from_dict(permission_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


