# CountryField

Country field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_options** | **List[str]** |  | [optional] 
**multiple_values** | **bool** | Multiple values state of a field | [optional] 

## Example

```python
from openapi_client.models.country_field import CountryField

# TODO update the JSON string below
json = "{}"
# create an instance of CountryField from a JSON string
country_field_instance = CountryField.from_json(json)
# print the JSON string representation of the object
print(CountryField.to_json())

# convert the object into a dict
country_field_dict = country_field_instance.to_dict()
# create an instance of CountryField from a dict
country_field_form_dict = country_field.from_dict(country_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


