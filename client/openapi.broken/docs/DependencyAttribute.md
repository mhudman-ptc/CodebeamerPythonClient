# DependencyAttribute

Information on how and where references were found in source project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookup_direction** | **str** | Direction in which dependency finder discovered the reference. | [optional] 
**path** | [**List[DependencyEntityReference]**](DependencyEntityReference.md) | Trace in source project model where the reference was found. | [optional] 

## Example

```python
from openapi_client.models.dependency_attribute import DependencyAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyAttribute from a JSON string
dependency_attribute_instance = DependencyAttribute.from_json(json)
# print the JSON string representation of the object
print(DependencyAttribute.to_json())

# convert the object into a dict
dependency_attribute_dict = dependency_attribute_instance.to_dict()
# create an instance of DependencyAttribute from a dict
dependency_attribute_form_dict = dependency_attribute.from_dict(dependency_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


