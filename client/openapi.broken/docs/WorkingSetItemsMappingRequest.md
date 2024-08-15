# WorkingSetItemsMappingRequest

Working-Set Tracker Items mapping request object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Tracker Items on Working-Set or on the Default Working-Set | 
**target_working_set** | [**WorkingSetReference**](WorkingSetReference.md) |  | 

## Example

```python
from openapi_client.models.working_set_items_mapping_request import WorkingSetItemsMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetItemsMappingRequest from a JSON string
working_set_items_mapping_request_instance = WorkingSetItemsMappingRequest.from_json(json)
# print the JSON string representation of the object
print(WorkingSetItemsMappingRequest.to_json())

# convert the object into a dict
working_set_items_mapping_request_dict = working_set_items_mapping_request_instance.to_dict()
# create an instance of WorkingSetItemsMappingRequest from a dict
working_set_items_mapping_request_form_dict = working_set_items_mapping_request.from_dict(working_set_items_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


