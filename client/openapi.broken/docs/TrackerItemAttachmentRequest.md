# TrackerItemAttachmentRequest

Request data to retrieve tracker item attachments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_id** | **int** | Baseline id to specify the versions of the tracker items. | [optional] 
**exclude_filter** | **bool** | Indicator if the attachments matching the filters need to be excluded or not | [optional] 
**extensions** | **List[str]** | File extension filters. | [optional] 
**mime_types** | **List[str]** | File mime type filters. | [optional] 

## Example

```python
from openapi_client.models.tracker_item_attachment_request import TrackerItemAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemAttachmentRequest from a JSON string
tracker_item_attachment_request_instance = TrackerItemAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerItemAttachmentRequest.to_json())

# convert the object into a dict
tracker_item_attachment_request_dict = tracker_item_attachment_request_instance.to_dict()
# create an instance of TrackerItemAttachmentRequest from a dict
tracker_item_attachment_request_form_dict = tracker_item_attachment_request.from_dict(tracker_item_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


