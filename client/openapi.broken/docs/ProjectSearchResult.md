# ProjectSearchResult

One page of artifact revisions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**projects** | [**List[Project]**](Project.md) | Found projects | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.project_search_result import ProjectSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSearchResult from a JSON string
project_search_result_instance = ProjectSearchResult.from_json(json)
# print the JSON string representation of the object
print(ProjectSearchResult.to_json())

# convert the object into a dict
project_search_result_dict = project_search_result_instance.to_dict()
# create an instance of ProjectSearchResult from a dict
project_search_result_form_dict = project_search_result.from_dict(project_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


