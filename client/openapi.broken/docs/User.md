# User

Properties of a codebeamer user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of a user | [optional] 
**city** | **str** | City of a user | [optional] 
**company** | **str** | Company of a user | [optional] 
**country** | **str** | Country of a user in ISO 3166-1 alpha-2 format | [optional] 
**date_format** | **str** | Date format of a user | [optional] 
**email** | **str** | Email of a user | [optional] 
**first_name** | **str** | First name of a user | [optional] 
**id** | **int** | Id of the entity | [optional] 
**language** | **str** | Language of a user in ISO 639-1 format | [optional] 
**last_login_date** | **datetime** | Last login date of a user | [optional] 
**last_name** | **str** | Last name of a user | [optional] 
**mobile** | **str** | Mobile number of a user | [optional] 
**name** | **str** | Name of the entity | [optional] 
**phone** | **str** | Phone number of a user | [optional] 
**registry_date** | **datetime** | Registration date of a user | [optional] 
**skills** | **str** | Skills of a user | [optional] 
**state** | **str** | State / providence of a user | [optional] 
**status** | **str** | Status of a user | [optional] 
**time_zone** | **str** | Time zone of a user | [optional] 
**title** | **str** | Title of a user | [optional] 
**zip** | **str** | Zip of a user | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


