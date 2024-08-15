# AccessPermissionsRequest

Request model to provide permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[AccessPermission]**](AccessPermission.md) | List of access permissions. | [optional] 

## Example

```python
from openapi_client.models.access_permissions_request import AccessPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPermissionsRequest from a JSON string
access_permissions_request_instance = AccessPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(AccessPermissionsRequest.to_json())

# convert the object into a dict
access_permissions_request_dict = access_permissions_request_instance.to_dict()
# create an instance of AccessPermissionsRequest from a dict
access_permissions_request_form_dict = access_permissions_request.from_dict(access_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


