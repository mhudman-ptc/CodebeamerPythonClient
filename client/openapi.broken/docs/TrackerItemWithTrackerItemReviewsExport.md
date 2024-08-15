# TrackerItemWithTrackerItemReviewsExport

A Tracker Item with all of its corresponding Tracker Item Reviews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracker_item** | [**TrackerItem**](TrackerItem.md) |  | [optional] 
**tracker_item_reviews** | [**List[TrackerItemReviewExport]**](TrackerItemReviewExport.md) | List of Tracker Item Reviews | [optional] 

## Example

```python
from openapi_client.models.tracker_item_with_tracker_item_reviews_export import TrackerItemWithTrackerItemReviewsExport

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemWithTrackerItemReviewsExport from a JSON string
tracker_item_with_tracker_item_reviews_export_instance = TrackerItemWithTrackerItemReviewsExport.from_json(json)
# print the JSON string representation of the object
print(TrackerItemWithTrackerItemReviewsExport.to_json())

# convert the object into a dict
tracker_item_with_tracker_item_reviews_export_dict = tracker_item_with_tracker_item_reviews_export_instance.to_dict()
# create an instance of TrackerItemWithTrackerItemReviewsExport from a dict
tracker_item_with_tracker_item_reviews_export_form_dict = tracker_item_with_tracker_item_reviews_export.from_dict(tracker_item_with_tracker_item_reviews_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


