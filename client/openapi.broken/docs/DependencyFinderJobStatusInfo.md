# DependencyFinderJobStatusInfo

Status information of a dependency finder job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_project_warnings** | **List[str]** | Warnings due to closed projects. | [optional] 
**dependencies** | [**List[CrossProjectDependency]**](CrossProjectDependency.md) | Dependencies found among projects. | [optional] 
**missing_permission_warnings** | **List[str]** | Permission warnings. | [optional] 
**projects_checked** | **int** | Number of projects already checked for dependencies | [optional] 
**projects_scheduled** | **int** | Number of projects scheduled for dependency collection | [optional] 

## Example

```python
from openapi_client.models.dependency_finder_job_status_info import DependencyFinderJobStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyFinderJobStatusInfo from a JSON string
dependency_finder_job_status_info_instance = DependencyFinderJobStatusInfo.from_json(json)
# print the JSON string representation of the object
print(DependencyFinderJobStatusInfo.to_json())

# convert the object into a dict
dependency_finder_job_status_info_dict = dependency_finder_job_status_info_instance.to_dict()
# create an instance of DependencyFinderJobStatusInfo from a dict
dependency_finder_job_status_info_form_dict = dependency_finder_job_status_info.from_dict(dependency_finder_job_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


