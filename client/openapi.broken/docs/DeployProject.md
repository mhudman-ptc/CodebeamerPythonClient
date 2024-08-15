# DeployProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_file_id** | **int** | Id of a codebeamer document | [optional] 
**password** | **str** | The password to decrypt the uploaded configuration file | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**project_file_id** | **int** | Id of a codebeamer document | [optional] 

## Example

```python
from openapi_client.models.deploy_project import DeployProject

# TODO update the JSON string below
json = "{}"
# create an instance of DeployProject from a JSON string
deploy_project_instance = DeployProject.from_json(json)
# print the JSON string representation of the object
print(DeployProject.to_json())

# convert the object into a dict
deploy_project_dict = deploy_project_instance.to_dict()
# create an instance of DeployProject from a dict
deploy_project_form_dict = deploy_project.from_dict(deploy_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


