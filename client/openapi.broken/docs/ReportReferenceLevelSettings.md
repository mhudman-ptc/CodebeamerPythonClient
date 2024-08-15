# ReportReferenceLevelSettings

Reference level settings for Intelligent Table View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[ReportColumnSettings]**](ReportColumnSettings.md) | Columns to show on this reference level. | 
**downstream_reference** | **bool** | Include downstream references indicator. | 
**level** | **int** | Level of the reference layer | 
**reference_tracker_types** | [**List[TrackerTypeReference]**](TrackerTypeReference.md) | Tracker types to include on this level. | [optional] 
**reference_trackers** | [**List[TrackerReference]**](TrackerReference.md) | Trackers to include on this level. | [optional] 
**upstream_reference** | **bool** | Include upstream references indicator. | 

## Example

```python
from openapi_client.models.report_reference_level_settings import ReportReferenceLevelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReferenceLevelSettings from a JSON string
report_reference_level_settings_instance = ReportReferenceLevelSettings.from_json(json)
# print the JSON string representation of the object
print(ReportReferenceLevelSettings.to_json())

# convert the object into a dict
report_reference_level_settings_dict = report_reference_level_settings_instance.to_dict()
# create an instance of ReportReferenceLevelSettings from a dict
report_reference_level_settings_form_dict = report_reference_level_settings.from_dict(report_reference_level_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


