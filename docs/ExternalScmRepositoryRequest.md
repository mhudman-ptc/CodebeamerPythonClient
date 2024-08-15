# ExternalScmRepositoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_id** | **int** | Id of already created token for external SCM provider API. Required in case when old access token should be used | [optional] 
**access_token_name** | **str** | Name of new access token for external SCM provider API. Required in case when new access token item should be created | [optional] 
**access_token_value** | **str** | Value of new access token for external SCM provider API. Required in case when new access token item should be created | [optional] 
**enable_patch_synchronization** | **bool** | Enable or disable patch synchronization | 
**name** | **str** | Name of new CB external SCM repository | 
**owner_name** | **str** | Owner name or organization name of external SCM provider repository | 
**project_name** | **str** | Project name of external SCM provider repository | [optional] 
**remote_api_url** | **str** | Base API URL of external SCM provider | 
**repository_name** | **str** | Repository name on external SCM provider&#x27;s side | 
**scm_type** | **str** | External SCM provider | 
**secret_id** | **int** | Id of already created Secret for external SCM provider API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

