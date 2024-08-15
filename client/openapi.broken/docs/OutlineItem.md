# OutlineItem

Represents an outline item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_children** | **bool** | Indicator if the item has child items. | [optional] 
**item_reference** | [**TrackerItemReference**](TrackerItemReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.outline_item import OutlineItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutlineItem from a JSON string
outline_item_instance = OutlineItem.from_json(json)
# print the JSON string representation of the object
print(OutlineItem.to_json())

# convert the object into a dict
outline_item_dict = outline_item_instance.to_dict()
# create an instance of OutlineItem from a dict
outline_item_form_dict = outline_item.from_dict(outline_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


