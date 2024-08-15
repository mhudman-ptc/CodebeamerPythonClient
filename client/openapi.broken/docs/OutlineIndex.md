# OutlineIndex

Represents the index of an item on a specific outline level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Outline index | [optional] 
**level** | **int** | Outline level | [optional] 

## Example

```python
from openapi_client.models.outline_index import OutlineIndex

# TODO update the JSON string below
json = "{}"
# create an instance of OutlineIndex from a JSON string
outline_index_instance = OutlineIndex.from_json(json)
# print the JSON string representation of the object
print(OutlineIndex.to_json())

# convert the object into a dict
outline_index_dict = outline_index_instance.to_dict()
# create an instance of OutlineIndex from a dict
outline_index_form_dict = outline_index.from_dict(outline_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


