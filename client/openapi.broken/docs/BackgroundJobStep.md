# BackgroundJobStep

Information about a background job step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the background job step | [optional] 
**name** | **str** | Name of the background job step | [optional] 
**result** | **str** | Result of a background job step | [optional] 
**result_message** | **str** | Result message of the background job step | [optional] 
**status** | **str** | Status of a background job step | [optional] 

## Example

```python
from openapi_client.models.background_job_step import BackgroundJobStep

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJobStep from a JSON string
background_job_step_instance = BackgroundJobStep.from_json(json)
# print the JSON string representation of the object
print(BackgroundJobStep.to_json())

# convert the object into a dict
background_job_step_dict = background_job_step_instance.to_dict()
# create an instance of BackgroundJobStep from a dict
background_job_step_form_dict = background_job_step.from_dict(background_job_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


