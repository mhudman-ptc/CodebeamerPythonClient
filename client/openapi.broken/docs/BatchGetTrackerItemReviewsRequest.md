# BatchGetTrackerItemReviewsRequest

Request model to fetch Tracker Item Reviews for multiple Tracker Items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_id** | **int** | Optional Baseline ID | [optional] 
**item_ids** | **List[int]** | List of Tracker Item IDs | [optional] 

## Example

```python
from openapi_client.models.batch_get_tracker_item_reviews_request import BatchGetTrackerItemReviewsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchGetTrackerItemReviewsRequest from a JSON string
batch_get_tracker_item_reviews_request_instance = BatchGetTrackerItemReviewsRequest.from_json(json)
# print the JSON string representation of the object
print(BatchGetTrackerItemReviewsRequest.to_json())

# convert the object into a dict
batch_get_tracker_item_reviews_request_dict = batch_get_tracker_item_reviews_request_instance.to_dict()
# create an instance of BatchGetTrackerItemReviewsRequest from a dict
batch_get_tracker_item_reviews_request_form_dict = batch_get_tracker_item_reviews_request.from_dict(batch_get_tracker_item_reviews_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


