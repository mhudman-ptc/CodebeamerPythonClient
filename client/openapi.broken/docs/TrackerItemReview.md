# TrackerItemReview

A tracker item review instance including its reviewers and their decisions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**TrackerItemReviewConfig**](TrackerItemReviewConfig.md) |  | [optional] 
**result** | **str** | Whether the review is approved or rejected | [optional] 
**reviewers** | [**List[TrackerItemReviewVote]**](TrackerItemReviewVote.md) | List of reviewers, and their votes | [optional] 
**tracker_item** | [**TrackerItemRevision**](TrackerItemRevision.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_review import TrackerItemReview

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReview from a JSON string
tracker_item_review_instance = TrackerItemReview.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReview.to_json())

# convert the object into a dict
tracker_item_review_dict = tracker_item_review_instance.to_dict()
# create an instance of TrackerItemReview from a dict
tracker_item_review_form_dict = tracker_item_review.from_dict(tracker_item_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


