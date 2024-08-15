# CrossProjectDependency

Dependency information between two projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_from** | [**List[DependencyAttribute]**](DependencyAttribute.md) | Information on where references were found in source project. | [optional] 
**source_project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**target_project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.cross_project_dependency import CrossProjectDependency

# TODO update the JSON string below
json = "{}"
# create an instance of CrossProjectDependency from a JSON string
cross_project_dependency_instance = CrossProjectDependency.from_json(json)
# print the JSON string representation of the object
print(CrossProjectDependency.to_json())

# convert the object into a dict
cross_project_dependency_dict = cross_project_dependency_instance.to_dict()
# create an instance of CrossProjectDependency from a dict
cross_project_dependency_form_dict = cross_project_dependency.from_dict(cross_project_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


