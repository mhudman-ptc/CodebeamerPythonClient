# SimpleReportSettings

Settings for a simple report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_permissions** | [**List[ReportPermission]**](ReportPermission.md) | Access permissions for the report. | [optional] 
**cb_ql** | **str** | CbQL query string of the report. | 
**columns** | [**List[ResizableReportColumnSettings]**](ResizableReportColumnSettings.md) | Column definitions. | 
**description** | **str** | Description of the report. | 
**name** | **str** | Name of the report. | 
**report_id** | **int** | Id of a report | [optional] 
**show_all_children** | **bool** | Indicator to ability to collapse/expand all child items. | [optional] 
**show_ancestors** | **bool** | Indicator to show the ancestors of a result item. | [optional] 
**show_descendants** | **bool** | Indicator to show the descendants of a result item. | [optional] 

## Example

```python
from openapi_client.models.simple_report_settings import SimpleReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleReportSettings from a JSON string
simple_report_settings_instance = SimpleReportSettings.from_json(json)
# print the JSON string representation of the object
print(SimpleReportSettings.to_json())

# convert the object into a dict
simple_report_settings_dict = simple_report_settings_instance.to_dict()
# create an instance of SimpleReportSettings from a dict
simple_report_settings_form_dict = simple_report_settings.from_dict(simple_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


