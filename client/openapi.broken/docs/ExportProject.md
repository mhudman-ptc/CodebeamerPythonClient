# ExportProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | A password that is used during the project encryption. | [optional] 
**selected_tracker_ids** | **List[int]** | If this list is not empty then only the Trackers listed here are exported. | [optional] 
**skip_associations** | **bool** | If true, then the Associations are not exported | [optional] [default to False]
**skip_reports** | **bool** | If true, then the Reports are not exported | [optional] [default to False]
**skip_tracker_items** | **bool** | If true, then the Tracker Items are not exported | [optional] [default to False]
**skip_wiki_pages** | **bool** | If true, then the Wiki PAges are not exported | [optional] [default to True]

## Example

```python
from openapi_client.models.export_project import ExportProject

# TODO update the JSON string below
json = "{}"
# create an instance of ExportProject from a JSON string
export_project_instance = ExportProject.from_json(json)
# print the JSON string representation of the object
print(ExportProject.to_json())

# convert the object into a dict
export_project_dict = export_project_instance.to_dict()
# create an instance of ExportProject from a dict
export_project_form_dict = export_project.from_dict(export_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


