# DateFieldValue

Value container of a date field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | Date value | [optional] 

## Example

```python
from openapi_client.models.date_field_value import DateFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of DateFieldValue from a JSON string
date_field_value_instance = DateFieldValue.from_json(json)
# print the JSON string representation of the object
print(DateFieldValue.to_json())

# convert the object into a dict
date_field_value_dict = date_field_value_instance.to_dict()
# create an instance of DateFieldValue from a dict
date_field_value_form_dict = date_field_value.from_dict(date_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


