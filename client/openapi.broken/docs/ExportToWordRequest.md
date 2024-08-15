# ExportToWordRequest

Request model for exporting items to Word

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_item_and_its_children** | **bool** | The children of the current item should be included also or not | [optional] 
**current_item_id** | **int** | The id of the item | 
**export_target_tracker_folder_id** | **int** | The Document tracker Folder where the exported file will be stored | [optional] 
**export_target_tracker_id** | **int** | The id of the Document type Tracker | 
**new_version** | **bool** | If true, new version of the file will be created (timestamp added), otherwise previous file will be overwritten | [optional] 
**report_id** | **int** | If specified, the report result will be in the Word document instead of the current item (and its children, if this set) | [optional] 
**word_filename** | **str** | The name of the generated Word document | 
**word_template_name** | **str** | Which Word template should be used for the Word document generation | [optional] 

## Example

```python
from openapi_client.models.export_to_word_request import ExportToWordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportToWordRequest from a JSON string
export_to_word_request_instance = ExportToWordRequest.from_json(json)
# print the JSON string representation of the object
print(ExportToWordRequest.to_json())

# convert the object into a dict
export_to_word_request_dict = export_to_word_request_instance.to_dict()
# create an instance of ExportToWordRequest from a dict
export_to_word_request_form_dict = export_to_word_request.from_dict(export_to_word_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


