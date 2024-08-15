# TrackerItemReviewVoteExport

A reviewer and its vote for a particular Tracker Item Review instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | What the reviewer voted for | [optional] 
**first_name** | **str** | First name of the reviewer | [optional] 
**last_name** | **str** | Last name of the reviewer | [optional] 
**reviewed_at** | **datetime** | Time at when the review was performed | [optional] 
**role_name** | **str** | Name of the role which the reviewer chose to use to vote | [optional] 
**user_name** | **str** | Username of the user who voted | [optional] 

## Example

```python
from openapi_client.models.tracker_item_review_vote_export import TrackerItemReviewVoteExport

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReviewVoteExport from a JSON string
tracker_item_review_vote_export_instance = TrackerItemReviewVoteExport.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReviewVoteExport.to_json())

# convert the object into a dict
tracker_item_review_vote_export_dict = tracker_item_review_vote_export_instance.to_dict()
# create an instance of TrackerItemReviewVoteExport from a dict
tracker_item_review_vote_export_form_dict = tracker_item_review_vote_export.from_dict(tracker_item_review_vote_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


