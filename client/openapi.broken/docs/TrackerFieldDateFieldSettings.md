# TrackerFieldDateFieldSettings

Describes the settings of a date type Field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_day** | **bool** |  | [optional] 
**display_month** | **bool** |  | [optional] 
**display_time** | **bool** |  | [optional] 
**display_year** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_date_field_settings import TrackerFieldDateFieldSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldDateFieldSettings from a JSON string
tracker_field_date_field_settings_instance = TrackerFieldDateFieldSettings.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldDateFieldSettings.to_json())

# convert the object into a dict
tracker_field_date_field_settings_dict = tracker_field_date_field_settings_instance.to_dict()
# create an instance of TrackerFieldDateFieldSettings from a dict
tracker_field_date_field_settings_form_dict = tracker_field_date_field_settings.from_dict(tracker_field_date_field_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


