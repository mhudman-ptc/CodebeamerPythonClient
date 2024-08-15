# AbstractOutline

Abstract outline entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline_indexes** | [**List[OutlineIndex]**](OutlineIndex.md) | Indexes of the entity in the outline. | [optional] 
**type** | **str** | Type of the outline model | [optional] 

## Example

```python
from openapi_client.models.abstract_outline import AbstractOutline

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractOutline from a JSON string
abstract_outline_instance = AbstractOutline.from_json(json)
# print the JSON string representation of the object
print(AbstractOutline.to_json())

# convert the object into a dict
abstract_outline_dict = abstract_outline_instance.to_dict()
# create an instance of AbstractOutline from a dict
abstract_outline_form_dict = abstract_outline.from_dict(abstract_outline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


