# ReportCell

Cell value for a column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_ref** | **str** | Column reference | [optional] 
**value** | **object** | Cell value | [optional] 

## Example

```python
from openapi_client.models.report_cell import ReportCell

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCell from a JSON string
report_cell_instance = ReportCell.from_json(json)
# print the JSON string representation of the object
print(ReportCell.to_json())

# convert the object into a dict
report_cell_dict = report_cell_instance.to_dict()
# create an instance of ReportCell from a dict
report_cell_form_dict = report_cell.from_dict(report_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


