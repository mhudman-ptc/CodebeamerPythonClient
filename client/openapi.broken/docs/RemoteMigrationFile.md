# RemoteMigrationFile

A file to migrate from a remote directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name of the newly created attachment. | [optional] 
**file_path** | **str** | The path of the file relative to the configured migration home directory. | [optional] 
**md5sum** | **str** | Precomputed MD5 checksum of the file. | [optional] 
**sha512sum** | **str** | Precomputed SHA512 checksum of the file. | [optional] 

## Example

```python
from openapi_client.models.remote_migration_file import RemoteMigrationFile

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteMigrationFile from a JSON string
remote_migration_file_instance = RemoteMigrationFile.from_json(json)
# print the JSON string representation of the object
print(RemoteMigrationFile.to_json())

# convert the object into a dict
remote_migration_file_dict = remote_migration_file_instance.to_dict()
# create an instance of RemoteMigrationFile from a dict
remote_migration_file_form_dict = remote_migration_file.from_dict(remote_migration_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


