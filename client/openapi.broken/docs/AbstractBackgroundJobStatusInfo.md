# AbstractBackgroundJobStatusInfo

Status information of a background job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress_percentage** | **int** | Progress in percentage (calculated based on pre-set weights) | [optional] 
**step_in_progress** | **str** | Step currently in progress | [optional] 
**type** | **str** | Type of status info object | [optional] 

## Example

```python
from openapi_client.models.abstract_background_job_status_info import AbstractBackgroundJobStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractBackgroundJobStatusInfo from a JSON string
abstract_background_job_status_info_instance = AbstractBackgroundJobStatusInfo.from_json(json)
# print the JSON string representation of the object
print(AbstractBackgroundJobStatusInfo.to_json())

# convert the object into a dict
abstract_background_job_status_info_dict = abstract_background_job_status_info_instance.to_dict()
# create an instance of AbstractBackgroundJobStatusInfo from a dict
abstract_background_job_status_info_form_dict = abstract_background_job_status_info.from_dict(abstract_background_job_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


