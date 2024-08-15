# LockInfo

Information about an artifact lock

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **bool** | Whether the lock will expire on its own, eg. if it is a soft lock | [optional] 
**user** | [**UserReference**](UserReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.lock_info import LockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LockInfo from a JSON string
lock_info_instance = LockInfo.from_json(json)
# print the JSON string representation of the object
print(LockInfo.to_json())

# convert the object into a dict
lock_info_dict = lock_info_instance.to_dict()
# create an instance of LockInfo from a dict
lock_info_form_dict = lock_info.from_dict(lock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


