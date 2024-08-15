# WorkingSetMinimal

Minimal information of a Working-Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date when the Working-Set was created | [optional] 
**deleted** | **bool** | Is the Working-Set deleted or not | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**type** | **str** | Type of a referenced object | [optional] 

## Example

```python
from openapi_client.models.working_set_minimal import WorkingSetMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingSetMinimal from a JSON string
working_set_minimal_instance = WorkingSetMinimal.from_json(json)
# print the JSON string representation of the object
print(WorkingSetMinimal.to_json())

# convert the object into a dict
working_set_minimal_dict = working_set_minimal_instance.to_dict()
# create an instance of WorkingSetMinimal from a dict
working_set_minimal_form_dict = working_set_minimal.from_dict(working_set_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


