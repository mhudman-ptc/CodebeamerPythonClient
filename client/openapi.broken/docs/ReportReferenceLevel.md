# ReportReferenceLevel

Reference results for an item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[ReportColumn]**](ReportColumn.md) | Columns to show on this reference level. | [optional] 
**downstream_reference_rows** | [**List[ReportReferencedRow]**](ReportReferencedRow.md) | Downstream reference results. | [optional] 
**reference_level** | **int** | Reference level. | [optional] 
**upstream_reference_rows** | [**List[ReportReferencedRow]**](ReportReferencedRow.md) | Upstream reference results. | [optional] 

## Example

```python
from openapi_client.models.report_reference_level import ReportReferenceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReferenceLevel from a JSON string
report_reference_level_instance = ReportReferenceLevel.from_json(json)
# print the JSON string representation of the object
print(ReportReferenceLevel.to_json())

# convert the object into a dict
report_reference_level_dict = report_reference_level_instance.to_dict()
# create an instance of ReportReferenceLevel from a dict
report_reference_level_form_dict = report_reference_level.from_dict(report_reference_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


