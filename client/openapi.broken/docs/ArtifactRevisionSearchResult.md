# ArtifactRevisionSearchResult

One page of artifact revisions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**revisions** | [**List[ArtifactRevision]**](ArtifactRevision.md) | Found artifact revision | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.artifact_revision_search_result import ArtifactRevisionSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRevisionSearchResult from a JSON string
artifact_revision_search_result_instance = ArtifactRevisionSearchResult.from_json(json)
# print the JSON string representation of the object
print(ArtifactRevisionSearchResult.to_json())

# convert the object into a dict
artifact_revision_search_result_dict = artifact_revision_search_result_instance.to_dict()
# create an instance of ArtifactRevisionSearchResult from a dict
artifact_revision_search_result_form_dict = artifact_revision_search_result.from_dict(artifact_revision_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


