# CountryFieldMultiValue

This model holds country field values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_selection** | **bool** | Is field applicable for multiple select. | [optional] 
**values** | **List[str]** | Country codes | [optional] 

## Example

```python
from openapi_client.models.country_field_multi_value import CountryFieldMultiValue

# TODO update the JSON string below
json = "{}"
# create an instance of CountryFieldMultiValue from a JSON string
country_field_multi_value_instance = CountryFieldMultiValue.from_json(json)
# print the JSON string representation of the object
print(CountryFieldMultiValue.to_json())

# convert the object into a dict
country_field_multi_value_dict = country_field_multi_value_instance.to_dict()
# create an instance of CountryFieldMultiValue from a dict
country_field_multi_value_form_dict = country_field_multi_value.from_dict(country_field_multi_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


