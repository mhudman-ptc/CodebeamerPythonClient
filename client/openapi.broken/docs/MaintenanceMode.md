# MaintenanceMode

Basic properties of maintenance mode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**MaintenanceModeProperties**](MaintenanceModeProperties.md) |  | [optional] 
**system_mode** | **str** | System mode | [optional] 

## Example

```python
from openapi_client.models.maintenance_mode import MaintenanceMode

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceMode from a JSON string
maintenance_mode_instance = MaintenanceMode.from_json(json)
# print the JSON string representation of the object
print(MaintenanceMode.to_json())

# convert the object into a dict
maintenance_mode_dict = maintenance_mode_instance.to_dict()
# create an instance of MaintenanceMode from a dict
maintenance_mode_form_dict = maintenance_mode.from_dict(maintenance_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


