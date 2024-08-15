# DependencyEntityReference

Reference to an entity in dependency path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **int** | Type ID of entity | [optional] 

## Example

```python
from openapi_client.models.dependency_entity_reference import DependencyEntityReference

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyEntityReference from a JSON string
dependency_entity_reference_instance = DependencyEntityReference.from_json(json)
# print the JSON string representation of the object
print(DependencyEntityReference.to_json())

# convert the object into a dict
dependency_entity_reference_dict = dependency_entity_reference_instance.to_dict()
# create an instance of DependencyEntityReference from a dict
dependency_entity_reference_form_dict = dependency_entity_reference.from_dict(dependency_entity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


