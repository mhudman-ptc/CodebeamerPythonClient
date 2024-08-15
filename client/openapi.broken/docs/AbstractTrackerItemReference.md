# AbstractTrackerItemReference

Reference to an item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the reference/association | [optional] 
**item_revision** | [**TrackerItemRevision**](TrackerItemRevision.md) |  | [optional] 
**type** | **str** | Type of the relation | [optional] 

## Example

```python
from openapi_client.models.abstract_tracker_item_reference import AbstractTrackerItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractTrackerItemReference from a JSON string
abstract_tracker_item_reference_instance = AbstractTrackerItemReference.from_json(json)
# print the JSON string representation of the object
print(AbstractTrackerItemReference.to_json())

# convert the object into a dict
abstract_tracker_item_reference_dict = abstract_tracker_item_reference_instance.to_dict()
# create an instance of AbstractTrackerItemReference from a dict
abstract_tracker_item_reference_form_dict = abstract_tracker_item_reference.from_dict(abstract_tracker_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


