# MaintenanceModeProperties

Extra properties for maintenance mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_error_text** | **str** | Error text shown during login | 
**login_text** | **str** | Text shown on login screen | 
**notification_text** | **str** | Notification text | 
**slogan** | **str** | Slogan text | 
**welcome_text** | **str** | Welcome text | 

## Example

```python
from openapi_client.models.maintenance_mode_properties import MaintenanceModeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceModeProperties from a JSON string
maintenance_mode_properties_instance = MaintenanceModeProperties.from_json(json)
# print the JSON string representation of the object
print(MaintenanceModeProperties.to_json())

# convert the object into a dict
maintenance_mode_properties_dict = maintenance_mode_properties_instance.to_dict()
# create an instance of MaintenanceModeProperties from a dict
maintenance_mode_properties_form_dict = maintenance_mode_properties.from_dict(maintenance_mode_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


