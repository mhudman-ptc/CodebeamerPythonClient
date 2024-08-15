# TrackerItemReviewExport

A tracker item review instance including its reviewers and their decisions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | [**List[TrackerItemReviewVoteExport]**](TrackerItemReviewVoteExport.md) | List of reviewers and their votes | [optional] 
**tracker_item_version** | **int** | Version of the Tracker Item at the time of the review | [optional] 

## Example

```python
from openapi_client.models.tracker_item_review_export import TrackerItemReviewExport

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReviewExport from a JSON string
tracker_item_review_export_instance = TrackerItemReviewExport.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReviewExport.to_json())

# convert the object into a dict
tracker_item_review_export_dict = tracker_item_review_export_instance.to_dict()
# create an instance of TrackerItemReviewExport from a dict
tracker_item_review_export_form_dict = tracker_item_review_export.from_dict(tracker_item_review_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


