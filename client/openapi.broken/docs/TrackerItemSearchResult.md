# TrackerItemSearchResult

One page of tracker items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TrackerItem]**](TrackerItem.md) | Found tracker items | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.tracker_item_search_result import TrackerItemSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemSearchResult from a JSON string
tracker_item_search_result_instance = TrackerItemSearchResult.from_json(json)
# print the JSON string representation of the object
print(TrackerItemSearchResult.to_json())

# convert the object into a dict
tracker_item_search_result_dict = tracker_item_search_result_instance.to_dict()
# create an instance of TrackerItemSearchResult from a dict
tracker_item_search_result_form_dict = tracker_item_search_result.from_dict(tracker_item_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


