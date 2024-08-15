# TrackerWorkingSet

Working-Set information where the Tracker exists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline** | [**TrackerBaselineReference**](TrackerBaselineReference.md) |  | [optional] 
**branch** | [**BranchReference**](BranchReference.md) |  | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**deleted** | **bool** | Is the Working-Set deleted or not | [optional] 
**shared_in_working_set** | **bool** | The Tracker is shared in Working-Set | [optional] 
**working_set** | [**WorkingSetReference**](WorkingSetReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_working_set import TrackerWorkingSet

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerWorkingSet from a JSON string
tracker_working_set_instance = TrackerWorkingSet.from_json(json)
# print the JSON string representation of the object
print(TrackerWorkingSet.to_json())

# convert the object into a dict
tracker_working_set_dict = tracker_working_set_instance.to_dict()
# create an instance of TrackerWorkingSet from a dict
tracker_working_set_form_dict = tracker_working_set.from_dict(tracker_working_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


