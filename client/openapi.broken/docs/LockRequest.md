# LockRequest

Requested lock configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | If not a hard lock, the duration specified in time notation | [optional] 
**hard** | **bool** | Whether the lock should be hard | [optional] 

## Example

```python
from openapi_client.models.lock_request import LockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockRequest from a JSON string
lock_request_instance = LockRequest.from_json(json)
# print the JSON string representation of the object
print(LockRequest.to_json())

# convert the object into a dict
lock_request_dict = lock_request_instance.to_dict()
# create an instance of LockRequest from a dict
lock_request_form_dict = lock_request.from_dict(lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


