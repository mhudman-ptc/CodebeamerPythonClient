# WorkingSetUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_baseline_id** | **int** |  | [optional] 
**source** | [**WorkingSetReference**](WorkingSetReference.md) |  | 
**target** | [**WorkingSetReference**](WorkingSetReference.md) |  | 
**trackers** | [**List[WorkingSetTrackerUpdateRequest]**](WorkingSetTrackerUpdateRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.working_set_update_request import WorkingSetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetUpdateRequest from a JSON string
working_set_update_request_instance = WorkingSetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkingSetUpdateRequest.to_json())

# convert the object into a dict
working_set_update_request_dict = working_set_update_request_instance.to_dict()
# create an instance of WorkingSetUpdateRequest from a dict
working_set_update_request_form_dict = working_set_update_request.from_dict(working_set_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


