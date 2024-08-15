# TableFieldValue

Value container of a table field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[List[AbstractFieldValue]]** | Table values | [optional] 

## Example

```python
from openapi_client.models.table_field_value import TableFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of TableFieldValue from a JSON string
table_field_value_instance = TableFieldValue.from_json(json)
# print the JSON string representation of the object
print(TableFieldValue.to_json())

# convert the object into a dict
table_field_value_dict = table_field_value_instance.to_dict()
# create an instance of TableFieldValue from a dict
table_field_value_form_dict = table_field_value.from_dict(table_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


