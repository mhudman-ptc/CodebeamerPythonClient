# ReportGroupWithReferencedRows

ReportGroup having rows with references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grouping_level** | **int** |  | [optional] 
**rows** | [**List[ReportReferencedRow]**](ReportReferencedRow.md) |  | [optional] 
**star_row** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.report_group_with_referenced_rows import ReportGroupWithReferencedRows

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGroupWithReferencedRows from a JSON string
report_group_with_referenced_rows_instance = ReportGroupWithReferencedRows.from_json(json)
# print the JSON string representation of the object
print(ReportGroupWithReferencedRows.to_json())

# convert the object into a dict
report_group_with_referenced_rows_dict = report_group_with_referenced_rows_instance.to_dict()
# create an instance of ReportGroupWithReferencedRows from a dict
report_group_with_referenced_rows_form_dict = report_group_with_referenced_rows.from_dict(report_group_with_referenced_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


