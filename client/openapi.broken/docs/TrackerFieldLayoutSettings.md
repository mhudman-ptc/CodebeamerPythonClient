# TrackerFieldLayoutSettings

The field group layouts setting is used when rendering the edit view for a specific tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_layout** | **str** | defaultLayout of a tracker | [optional] 
**layouts** | [**List[FieldLayoutSettings]**](FieldLayoutSettings.md) | fieldLayoutSettingsModels of a tracker | [optional] 
**status_layout** | [**List[StatusLayout]**](StatusLayout.md) | statusLayout of a tracker | [optional] 

## Example

```python
from openapi_client.models.tracker_field_layout_settings import TrackerFieldLayoutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldLayoutSettings from a JSON string
tracker_field_layout_settings_instance = TrackerFieldLayoutSettings.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldLayoutSettings.to_json())

# convert the object into a dict
tracker_field_layout_settings_dict = tracker_field_layout_settings_instance.to_dict()
# create an instance of TrackerFieldLayoutSettings from a dict
tracker_field_layout_settings_form_dict = tracker_field_layout_settings.from_dict(tracker_field_layout_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


