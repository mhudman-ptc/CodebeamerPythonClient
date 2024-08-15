# DeploymentTrackerExportSettings

Tracker export settings for deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_included** | **bool** | Flag if tracker items are included. | [optional] 
**tracker_id** | **int** | Project id | 

## Example

```python
from openapi_client.models.deployment_tracker_export_settings import DeploymentTrackerExportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentTrackerExportSettings from a JSON string
deployment_tracker_export_settings_instance = DeploymentTrackerExportSettings.from_json(json)
# print the JSON string representation of the object
print(DeploymentTrackerExportSettings.to_json())

# convert the object into a dict
deployment_tracker_export_settings_dict = deployment_tracker_export_settings_instance.to_dict()
# create an instance of DeploymentTrackerExportSettings from a dict
deployment_tracker_export_settings_form_dict = deployment_tracker_export_settings.from_dict(deployment_tracker_export_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


