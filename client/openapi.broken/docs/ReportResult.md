# ReportResult

Report data model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cb_ql** | **str** | CbQL query behind the report | [optional] 
**columns** | [**List[ReportColumn]**](ReportColumn.md) | Column information | [optional] 
**data** | [**ReportGroup**](ReportGroup.md) |  | [optional] 
**paging_information** | [**ReportPagingInformation**](ReportPagingInformation.md) |  | [optional] 
**report** | [**ReportReference**](ReportReference.md) |  | [optional] 
**show_all_children** | **bool** | Indicator to ability to collapse/expand all child items. | [optional] 

## Example

```python
from openapi_client.models.report_result import ReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResult from a JSON string
report_result_instance = ReportResult.from_json(json)
# print the JSON string representation of the object
print(ReportResult.to_json())

# convert the object into a dict
report_result_dict = report_result_instance.to_dict()
# create an instance of ReportResult from a dict
report_result_form_dict = report_result.from_dict(report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


