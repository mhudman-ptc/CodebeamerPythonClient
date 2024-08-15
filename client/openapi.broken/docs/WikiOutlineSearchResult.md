# WikiOutlineSearchResult

Paginated search result of outline wiki pages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline_wiki_pages** | [**List[OutlineWiki]**](OutlineWiki.md) | Found outline wiki pages | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.wiki_outline_search_result import WikiOutlineSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of WikiOutlineSearchResult from a JSON string
wiki_outline_search_result_instance = WikiOutlineSearchResult.from_json(json)
# print the JSON string representation of the object
print(WikiOutlineSearchResult.to_json())

# convert the object into a dict
wiki_outline_search_result_dict = wiki_outline_search_result_instance.to_dict()
# create an instance of WikiOutlineSearchResult from a dict
wiki_outline_search_result_form_dict = wiki_outline_search_result.from_dict(wiki_outline_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


