# TrackerItemReviewVote

A tracker item review instance including its reviewers and their decisions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_role** | [**RoleReference**](RoleReference.md) |  | [optional] 
**decision** | **str** | The result of this particular vote | [optional] 
**reviewed_at** | **datetime** | Date and time of the vote | [optional] 
**user** | [**UserReference**](UserReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_review_vote import TrackerItemReviewVote

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReviewVote from a JSON string
tracker_item_review_vote_instance = TrackerItemReviewVote.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReviewVote.to_json())

# convert the object into a dict
tracker_item_review_vote_dict = tracker_item_review_vote_instance.to_dict()
# create an instance of TrackerItemReviewVote from a dict
tracker_item_review_vote_form_dict = tracker_item_review_vote.from_dict(tracker_item_review_vote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


