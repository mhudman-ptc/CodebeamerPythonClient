# TrackerItemSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_id** | **int** | Baseline on which the query is applied. | [optional] 
**page** | **int** | Index of the page | [optional] [default to 1]
**page_size** | **int** | Size of the found page | [optional] [default to 25]
**query_string** | **str** | CbQL query for the requested items | 

## Example

```python
from openapi_client.models.tracker_item_search_request import TrackerItemSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemSearchRequest from a JSON string
tracker_item_search_request_instance = TrackerItemSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerItemSearchRequest.to_json())

# convert the object into a dict
tracker_item_search_request_dict = tracker_item_search_request_instance.to_dict()
# create an instance of TrackerItemSearchRequest from a dict
tracker_item_search_request_form_dict = tracker_item_search_request.from_dict(tracker_item_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


