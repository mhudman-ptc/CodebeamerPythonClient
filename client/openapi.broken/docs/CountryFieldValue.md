# CountryFieldValue

Value container of a country field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** | Country codes | [optional] 

## Example

```python
from openapi_client.models.country_field_value import CountryFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of CountryFieldValue from a JSON string
country_field_value_instance = CountryFieldValue.from_json(json)
# print the JSON string representation of the object
print(CountryFieldValue.to_json())

# convert the object into a dict
country_field_value_dict = country_field_value_instance.to_dict()
# create an instance of CountryFieldValue from a dict
country_field_value_form_dict = country_field_value.from_dict(country_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


