# WorkingSetTrackerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_id** | **int** |  | [optional] 
**cbql** | **str** |  | [optional] 
**tracker** | [**TrackerReference**](TrackerReference.md) |  | 

## Example

```python
from openapi_client.models.working_set_tracker_update_request import WorkingSetTrackerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetTrackerUpdateRequest from a JSON string
working_set_tracker_update_request_instance = WorkingSetTrackerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkingSetTrackerUpdateRequest.to_json())

# convert the object into a dict
working_set_tracker_update_request_dict = working_set_tracker_update_request_instance.to_dict()
# create an instance of WorkingSetTrackerUpdateRequest from a dict
working_set_tracker_update_request_form_dict = working_set_tracker_update_request.from_dict(working_set_tracker_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


