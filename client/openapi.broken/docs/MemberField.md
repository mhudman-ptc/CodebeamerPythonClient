# MemberField

Member field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_types** | **List[str]** | Supported member type of a member field | [optional] 
**multiple_values** | **bool** | Multiple values state of a field | [optional] 

## Example

```python
from openapi_client.models.member_field import MemberField

# TODO update the JSON string below
json = "{}"
# create an instance of MemberField from a JSON string
member_field_instance = MemberField.from_json(json)
# print the JSON string representation of the object
print(MemberField.to_json())

# convert the object into a dict
member_field_dict = member_field_instance.to_dict()
# create an instance of MemberField from a dict
member_field_form_dict = member_field.from_dict(member_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


