# TrackerSearchResult

One page of trackers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 
**trackers** | [**List[Tracker]**](Tracker.md) | Found tracker items | [optional] 

## Example

```python
from openapi_client.models.tracker_search_result import TrackerSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerSearchResult from a JSON string
tracker_search_result_instance = TrackerSearchResult.from_json(json)
# print the JSON string representation of the object
print(TrackerSearchResult.to_json())

# convert the object into a dict
tracker_search_result_dict = tracker_search_result_instance.to_dict()
# create an instance of TrackerSearchResult from a dict
tracker_search_result_form_dict = tracker_search_result.from_dict(tracker_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


