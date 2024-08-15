# WorkingSetItemMapping

Working-Set Tracker Item mapping object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TrackerItemReference**](TrackerItemReference.md) |  | [optional] 
**target** | [**TrackerItemReference**](TrackerItemReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.working_set_item_mapping import WorkingSetItemMapping

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetItemMapping from a JSON string
working_set_item_mapping_instance = WorkingSetItemMapping.from_json(json)
# print the JSON string representation of the object
print(WorkingSetItemMapping.to_json())

# convert the object into a dict
working_set_item_mapping_dict = working_set_item_mapping_instance.to_dict()
# create an instance of WorkingSetItemMapping from a dict
working_set_item_mapping_form_dict = working_set_item_mapping.from_dict(working_set_item_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


