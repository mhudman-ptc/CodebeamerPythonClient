# TrackerItemReviewConfig

The configuration from which the review was created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_approvals** | **int** | Number of approvals after which the review is considered approved | [optional] 
**required_rejections** | **int** | Number of rejections after which the review is considered rejected | [optional] 
**required_signature** | **str** | Whether the user has to provide its credentials to vote | [optional] 
**role_required** | **bool** | Whether the reviewers have to chose in which of their roles do they want to vote | [optional] 

## Example

```python
from openapi_client.models.tracker_item_review_config import TrackerItemReviewConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemReviewConfig from a JSON string
tracker_item_review_config_instance = TrackerItemReviewConfig.from_json(json)
# print the JSON string representation of the object
print(TrackerItemReviewConfig.to_json())

# convert the object into a dict
tracker_item_review_config_dict = tracker_item_review_config_instance.to_dict()
# create an instance of TrackerItemReviewConfig from a dict
tracker_item_review_config_form_dict = tracker_item_review_config.from_dict(tracker_item_review_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


