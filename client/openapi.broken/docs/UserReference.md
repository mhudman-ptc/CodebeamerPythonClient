# UserReference

Reference to a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of a referenced user | [optional] 

## Example

```python
from openapi_client.models.user_reference import UserReference

# TODO update the JSON string below
json = "{}"
# create an instance of UserReference from a JSON string
user_reference_instance = UserReference.from_json(json)
# print the JSON string representation of the object
print(UserReference.to_json())

# convert the object into a dict
user_reference_dict = user_reference_instance.to_dict()
# create an instance of UserReference from a dict
user_reference_form_dict = user_reference.from_dict(user_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


