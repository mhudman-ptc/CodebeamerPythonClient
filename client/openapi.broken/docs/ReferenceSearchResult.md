# ReferenceSearchResult

One page of references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**references** | [**List[AbstractReference]**](AbstractReference.md) | Found references | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.reference_search_result import ReferenceSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceSearchResult from a JSON string
reference_search_result_instance = ReferenceSearchResult.from_json(json)
# print the JSON string representation of the object
print(ReferenceSearchResult.to_json())

# convert the object into a dict
reference_search_result_dict = reference_search_result_instance.to_dict()
# create an instance of ReferenceSearchResult from a dict
reference_search_result_form_dict = reference_search_result.from_dict(reference_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


