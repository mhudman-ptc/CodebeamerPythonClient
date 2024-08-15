# TableField

Table field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[AbstractField]**](AbstractField.md) | Columns of a table | [optional] 

## Example

```python
from openapi_client.models.table_field import TableField

# TODO update the JSON string below
json = "{}"
# create an instance of TableField from a JSON string
table_field_instance = TableField.from_json(json)
# print the JSON string representation of the object
print(TableField.to_json())

# convert the object into a dict
table_field_dict = table_field_instance.to_dict()
# create an instance of TableField from a dict
table_field_form_dict = table_field.from_dict(table_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


