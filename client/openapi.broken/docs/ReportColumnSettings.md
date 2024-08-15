# ReportColumnSettings

Settings for a column definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_index** | **int** | Index of the column in the report table. | 
**field** | [**FieldReference**](FieldReference.md) |  | 

## Example

```python
from openapi_client.models.report_column_settings import ReportColumnSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ReportColumnSettings from a JSON string
report_column_settings_instance = ReportColumnSettings.from_json(json)
# print the JSON string representation of the object
print(ReportColumnSettings.to_json())

# convert the object into a dict
report_column_settings_dict = report_column_settings_instance.to_dict()
# create an instance of ReportColumnSettings from a dict
report_column_settings_form_dict = report_column_settings.from_dict(report_column_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


