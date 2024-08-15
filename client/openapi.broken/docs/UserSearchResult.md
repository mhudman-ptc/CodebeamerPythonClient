# UserSearchResult

Paginated search result of users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 
**users** | [**List[User]**](User.md) | Found users | [optional] 

## Example

```python
from openapi_client.models.user_search_result import UserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchResult from a JSON string
user_search_result_instance = UserSearchResult.from_json(json)
# print the JSON string representation of the object
print(UserSearchResult.to_json())

# convert the object into a dict
user_search_result_dict = user_search_result_instance.to_dict()
# create an instance of UserSearchResult from a dict
user_search_result_form_dict = user_search_result.from_dict(user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


