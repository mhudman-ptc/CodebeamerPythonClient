# BackgroundJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_job_status** | **str** | Status of a background job | [optional] 
**background_job_type** | **str** | Type of job | [optional] 
**created_at** | **datetime** | Creation time of job | [optional] 
**description** | **str** | Description of job | [optional] 
**finished_at** | **datetime** | Completion time of job | [optional] 
**id** | **int** | ID of job | [optional] 
**status_info** | [**AbstractBackgroundJobStatusInfo**](AbstractBackgroundJobStatusInfo.md) |  | [optional] 
**steps** | [**list[BackgroundJobStep]**](BackgroundJobStep.md) | Sub-steps of a job | [optional] 
**submitted_by** | [**UserReference**](UserReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

