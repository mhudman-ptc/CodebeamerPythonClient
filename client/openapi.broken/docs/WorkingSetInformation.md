# WorkingSetInformation

Information of a Working-Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[WorkingSetReference]**](WorkingSetReference.md) | The children of the given Working-Set | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**deleted** | **bool** | Is the Working-Set deleted or not | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**parent** | [**WorkingSetReference**](WorkingSetReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**root** | [**WorkingSetReference**](WorkingSetReference.md) |  | [optional] 
**type** | **str** | Type of a referenced object | [optional] 

## Example

```python
from openapi_client.models.working_set_information import WorkingSetInformation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetInformation from a JSON string
working_set_information_instance = WorkingSetInformation.from_json(json)
# print the JSON string representation of the object
print(WorkingSetInformation.to_json())

# convert the object into a dict
working_set_information_dict = working_set_information_instance.to_dict()
# create an instance of WorkingSetInformation from a dict
working_set_information_form_dict = working_set_information.from_dict(working_set_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


