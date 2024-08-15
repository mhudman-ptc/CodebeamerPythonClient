# ResizableReportColumnSettings

Settings for a resizeable column definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_index** | **int** | Index of the column in the report table. | 
**column_width_percentage** | **float** | Width of the column in percentage. | [optional] 
**field** | [**FieldReference**](FieldReference.md) |  | 

## Example

```python
from openapi_client.models.resizable_report_column_settings import ResizableReportColumnSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ResizableReportColumnSettings from a JSON string
resizable_report_column_settings_instance = ResizableReportColumnSettings.from_json(json)
# print the JSON string representation of the object
print(ResizableReportColumnSettings.to_json())

# convert the object into a dict
resizable_report_column_settings_dict = resizable_report_column_settings_instance.to_dict()
# create an instance of ResizableReportColumnSettings from a dict
resizable_report_column_settings_form_dict = resizable_report_column_settings.from_dict(resizable_report_column_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


