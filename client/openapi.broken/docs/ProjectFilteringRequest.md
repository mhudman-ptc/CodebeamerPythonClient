# ProjectFilteringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | Key name of the project | 

## Example

```python
from openapi_client.models.project_filtering_request import ProjectFilteringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectFilteringRequest from a JSON string
project_filtering_request_instance = ProjectFilteringRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectFilteringRequest.to_json())

# convert the object into a dict
project_filtering_request_dict = project_filtering_request_instance.to_dict()
# create an instance of ProjectFilteringRequest from a dict
project_filtering_request_form_dict = project_filtering_request.from_dict(project_filtering_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


