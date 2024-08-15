# TrackerReportSettings

Settings of a report on a tracker.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cb_ql** | **str** | CbQL query string of the report. | 
**columns** | [**List[ResizableReportColumnSettings]**](ResizableReportColumnSettings.md) | Column definitions. | 
**description** | **str** | Description of the report. | 
**is_public** | **bool** | Public report indicator. | 
**name** | **str** | Name of the report. | 
**reference_level_settings** | [**List[ReportReferenceLevelSettings]**](ReportReferenceLevelSettings.md) | Reference level setting for Intelligent Table View. | [optional] 
**rendering_method** | **str** | Rendering method for Intelligent Table View. | [optional] 
**report_id** | **int** | Id of a report | [optional] 
**show_all_children** | **bool** | Indicator to ability to collapse/expand all child items. | [optional] 
**show_ancestors** | **bool** | Indicator to show the ancestors of a result item. | [optional] 
**show_descendants** | **bool** | Indicator to show the descendants of a result item. | [optional] 
**tracker** | [**TrackerReference**](TrackerReference.md) |  | 

## Example

```python
from openapi_client.models.tracker_report_settings import TrackerReportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerReportSettings from a JSON string
tracker_report_settings_instance = TrackerReportSettings.from_json(json)
# print the JSON string representation of the object
print(TrackerReportSettings.to_json())

# convert the object into a dict
tracker_report_settings_dict = tracker_report_settings_instance.to_dict()
# create an instance of TrackerReportSettings from a dict
tracker_report_settings_form_dict = tracker_report_settings.from_dict(tracker_report_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


