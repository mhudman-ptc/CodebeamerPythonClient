# OutlineItemSearchResult

Paginated search result of outline items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline_items** | [**List[OutlineItem]**](OutlineItem.md) | Found outline items | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.outline_item_search_result import OutlineItemSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of OutlineItemSearchResult from a JSON string
outline_item_search_result_instance = OutlineItemSearchResult.from_json(json)
# print the JSON string representation of the object
print(OutlineItemSearchResult.to_json())

# convert the object into a dict
outline_item_search_result_dict = outline_item_search_result_instance.to_dict()
# create an instance of OutlineItemSearchResult from a dict
outline_item_search_result_form_dict = outline_item_search_result.from_dict(outline_item_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


