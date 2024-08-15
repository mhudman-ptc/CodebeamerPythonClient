# WorkingSetTracker

Tracker information in Working-Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**AbstractBaselineReferenceModel**](AbstractBaselineReferenceModel.md) |  | [optional] 
**created_at** | **datetime** | Date of creation (Working-Set creation date for shared trackers, the date when the branch was created for included trackers) | [optional] 
**deleted** | **bool** | Is the Tracker deleted or not | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**shared** | **bool** | Shared in Working-Set | [optional] 
**type** | **str** | Type of a referenced object | [optional] 

## Example

```python
from openapi_client.models.working_set_tracker import WorkingSetTracker

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetTracker from a JSON string
working_set_tracker_instance = WorkingSetTracker.from_json(json)
# print the JSON string representation of the object
print(WorkingSetTracker.to_json())

# convert the object into a dict
working_set_tracker_dict = working_set_tracker_instance.to_dict()
# create an instance of WorkingSetTracker from a dict
working_set_tracker_form_dict = working_set_tracker.from_dict(working_set_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


