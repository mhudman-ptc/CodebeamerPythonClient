# DurationFieldValue

Value container of a duration field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Duration value in milliseconds | [optional] 

## Example

```python
from openapi_client.models.duration_field_value import DurationFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of DurationFieldValue from a JSON string
duration_field_value_instance = DurationFieldValue.from_json(json)
# print the JSON string representation of the object
print(DurationFieldValue.to_json())

# convert the object into a dict
duration_field_value_dict = duration_field_value_instance.to_dict()
# create an instance of DurationFieldValue from a dict
duration_field_value_form_dict = duration_field_value.from_dict(duration_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


