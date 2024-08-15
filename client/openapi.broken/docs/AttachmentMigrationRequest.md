# AttachmentMigrationRequest

Request for migrating attachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**files** | [**List[RemoteMigrationFile]**](RemoteMigrationFile.md) | List of files to migrate | [optional] 
**migration_action** | **str** | Type of action made on the source files. | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**target_item** | [**TrackerItemReference**](TrackerItemReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachment_migration_request import AttachmentMigrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentMigrationRequest from a JSON string
attachment_migration_request_instance = AttachmentMigrationRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentMigrationRequest.to_json())

# convert the object into a dict
attachment_migration_request_dict = attachment_migration_request_instance.to_dict()
# create an instance of AttachmentMigrationRequest from a dict
attachment_migration_request_form_dict = attachment_migration_request.from_dict(attachment_migration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


