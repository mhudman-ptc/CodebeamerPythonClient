# UserFilteringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the user | [optional] 
**first_name** | **str** | First name of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**name** | **str** | Name of the user | [optional] 
**project_id** | **int** | Id of the project where the user is a member | [optional] 
**user_status** | **str** | Status of the user | [optional] 

## Example

```python
from openapi_client.models.user_filtering_request import UserFilteringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFilteringRequest from a JSON string
user_filtering_request_instance = UserFilteringRequest.from_json(json)
# print the JSON string representation of the object
print(UserFilteringRequest.to_json())

# convert the object into a dict
user_filtering_request_dict = user_filtering_request_instance.to_dict()
# create an instance of UserFilteringRequest from a dict
user_filtering_request_form_dict = user_filtering_request.from_dict(user_filtering_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


