# MemberReferenceSearchResult

Paginated search result of members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[AbstractReference]**](AbstractReference.md) | Found members | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.member_reference_search_result import MemberReferenceSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of MemberReferenceSearchResult from a JSON string
member_reference_search_result_instance = MemberReferenceSearchResult.from_json(json)
# print the JSON string representation of the object
print(MemberReferenceSearchResult.to_json())

# convert the object into a dict
member_reference_search_result_dict = member_reference_search_result_instance.to_dict()
# create an instance of MemberReferenceSearchResult from a dict
member_reference_search_result_form_dict = member_reference_search_result.from_dict(member_reference_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


