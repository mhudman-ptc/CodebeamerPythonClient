# FieldLayoutSettings

fieldLayoutSettingsModels of a tracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[FieldLayoutGroups]**](FieldLayoutGroups.md) | groupsModels of a fieldLayoutSettingsModel | [optional] 
**name** | **str** | name of a fieldLayoutSettingsModel | [optional] 
**show_default** | **bool** | showDefault of a fieldLayoutSettingsModel | [optional] 

## Example

```python
from openapi_client.models.field_layout_settings import FieldLayoutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FieldLayoutSettings from a JSON string
field_layout_settings_instance = FieldLayoutSettings.from_json(json)
# print the JSON string representation of the object
print(FieldLayoutSettings.to_json())

# convert the object into a dict
field_layout_settings_dict = field_layout_settings_instance.to_dict()
# create an instance of FieldLayoutSettings from a dict
field_layout_settings_form_dict = field_layout_settings.from_dict(field_layout_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


