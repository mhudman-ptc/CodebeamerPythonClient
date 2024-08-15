# DependencyFinderJobStatusInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_project_warnings** | **list[str]** | Warnings due to closed projects. | [optional] 
**dependencies** | [**list[CrossProjectDependency]**](CrossProjectDependency.md) | Dependencies found among projects. | [optional] 
**missing_permission_warnings** | **list[str]** | Permission warnings. | [optional] 
**projects_checked** | **int** | Number of projects already checked for dependencies | [optional] 
**projects_scheduled** | **int** | Number of projects scheduled for dependency collection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

