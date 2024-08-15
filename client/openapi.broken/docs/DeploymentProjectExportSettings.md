# DeploymentProjectExportSettings

Project export settings for deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_queries** | **bool** | Flag if queries are included. | [optional] 
**include_tracker_items** | **bool** | Flag if tracker items are included. | [optional] 
**include_trackers** | **bool** | Flag if trackers are included. | [optional] 
**project_id** | **int** | Project id | 
**trackers** | [**List[DeploymentTrackerExportSettings]**](DeploymentTrackerExportSettings.md) | Tracker export settings | [optional] 

## Example

```python
from openapi_client.models.deployment_project_export_settings import DeploymentProjectExportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentProjectExportSettings from a JSON string
deployment_project_export_settings_instance = DeploymentProjectExportSettings.from_json(json)
# print the JSON string representation of the object
print(DeploymentProjectExportSettings.to_json())

# convert the object into a dict
deployment_project_export_settings_dict = deployment_project_export_settings_instance.to_dict()
# create an instance of DeploymentProjectExportSettings from a dict
deployment_project_export_settings_form_dict = deployment_project_export_settings.from_dict(deployment_project_export_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


