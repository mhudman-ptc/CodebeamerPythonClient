# ExportForDeploymentRequest

Request export for deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_file_name** | **str** | Name of the resulting export file (without extension). | [optional] 
**password** | **str** | A password that is used during the project encryption. | [optional] 
**project_settings** | [**List[DeploymentProjectExportSettings]**](DeploymentProjectExportSettings.md) | Project settings | [optional] 
**schema_name** | **str** | Name of deployment settings schema | [optional] [readonly] 
**schema_version** | **str** | Version of deployment settings schema | [optional] [readonly] 

## Example

```python
from openapi_client.models.export_for_deployment_request import ExportForDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportForDeploymentRequest from a JSON string
export_for_deployment_request_instance = ExportForDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(ExportForDeploymentRequest.to_json())

# convert the object into a dict
export_for_deployment_request_dict = export_for_deployment_request_instance.to_dict()
# create an instance of ExportForDeploymentRequest from a dict
export_for_deployment_request_form_dict = export_for_deployment_request.from_dict(export_for_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


