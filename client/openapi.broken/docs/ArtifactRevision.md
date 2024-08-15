# ArtifactRevision

Model for a specific version of an artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_summary** | **str** | Summary of the change | [optional] 
**id** | **int** | Id of the entity | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**version** | **int** | Version of the artifact | [optional] 

## Example

```python
from openapi_client.models.artifact_revision import ArtifactRevision

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRevision from a JSON string
artifact_revision_instance = ArtifactRevision.from_json(json)
# print the JSON string representation of the object
print(ArtifactRevision.to_json())

# convert the object into a dict
artifact_revision_dict = artifact_revision_instance.to_dict()
# create an instance of ArtifactRevision from a dict
artifact_revision_form_dict = artifact_revision.from_dict(artifact_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


