# ReportColumn

Column definition for a report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_index** | **int** | Column position index in the report. | [optional] 
**column_ref** | **str** | Column reference | [optional] 
**column_width_percentage** | **float** | Column width in percentage | [optional] 
**field** | [**FieldReference**](FieldReference.md) |  | [optional] 
**name** | **str** | Column name | [optional] 
**type** | **str** | Column type | [optional] 

## Example

```python
from openapi_client.models.report_column import ReportColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ReportColumn from a JSON string
report_column_instance = ReportColumn.from_json(json)
# print the JSON string representation of the object
print(ReportColumn.to_json())

# convert the object into a dict
report_column_dict = report_column_instance.to_dict()
# create an instance of ReportColumn from a dict
report_column_form_dict = report_column.from_dict(report_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


