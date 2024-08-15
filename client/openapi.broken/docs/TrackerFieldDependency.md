# TrackerFieldDependency

Describes a Field Dependency configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependent_field_id** | **int** |  | [optional] 
**value_combinations** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_dependency import TrackerFieldDependency

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldDependency from a JSON string
tracker_field_dependency_instance = TrackerFieldDependency.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldDependency.to_json())

# convert the object into a dict
tracker_field_dependency_dict = tracker_field_dependency_instance.to_dict()
# create an instance of TrackerFieldDependency from a dict
tracker_field_dependency_form_dict = tracker_field_dependency.from_dict(tracker_field_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


