# BackgroundJob

Information about a background job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_job_status** | **str** | Status of a background job | [optional] 
**background_job_type** | **str** | Type of a background job | [optional] 
**created_at** | **datetime** | Creation time of job | [optional] 
**description** | **str** | Description of job | [optional] 
**finished_at** | **datetime** | Completion time of job | [optional] 
**id** | **int** | ID of job | [optional] 
**status_info** | [**AbstractBackgroundJobStatusInfo**](AbstractBackgroundJobStatusInfo.md) |  | [optional] 
**steps** | [**List[BackgroundJobStep]**](BackgroundJobStep.md) | Sub-steps of a job | [optional] 
**submitted_by** | [**UserReference**](UserReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.background_job import BackgroundJob

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJob from a JSON string
background_job_instance = BackgroundJob.from_json(json)
# print the JSON string representation of the object
print(BackgroundJob.to_json())

# convert the object into a dict
background_job_dict = background_job_instance.to_dict()
# create an instance of BackgroundJob from a dict
background_job_form_dict = background_job.from_dict(background_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


