# ReportReferencedRow

Result row having references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**List[ReportCell]**](ReportCell.md) | Cells in a row. | [optional] 
**is_real_result** | **bool** | Indicator if the item is a real query result (e.g. not an ancestor item). | [optional] 
**item_ref** | [**ReportItemReference**](ReportItemReference.md) |  | [optional] 
**outline_level** | **int** | Item&#39;s level in the tracker outline. | [optional] 
**references** | [**ReportReferenceLevel**](ReportReferenceLevel.md) |  | [optional] 

## Example

```python
from openapi_client.models.report_referenced_row import ReportReferencedRow

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReferencedRow from a JSON string
report_referenced_row_instance = ReportReferencedRow.from_json(json)
# print the JSON string representation of the object
print(ReportReferencedRow.to_json())

# convert the object into a dict
report_referenced_row_dict = report_referenced_row_instance.to_dict()
# create an instance of ReportReferencedRow from a dict
report_referenced_row_form_dict = report_referenced_row.from_dict(report_referenced_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


