# AbstractTrackerItemChange

Update of an item's field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | [**FieldReference**](FieldReference.md) |  | [optional] 
**name** | **str** | Name of the field | [optional] 
**new_value** | [**AbstractFieldValue**](AbstractFieldValue.md) |  | [optional] 
**old_value** | [**AbstractFieldValue**](AbstractFieldValue.md) |  | [optional] 
**type** | **str** | Change model type | [optional] 

## Example

```python
from openapi_client.models.abstract_tracker_item_change import AbstractTrackerItemChange

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractTrackerItemChange from a JSON string
abstract_tracker_item_change_instance = AbstractTrackerItemChange.from_json(json)
# print the JSON string representation of the object
print(AbstractTrackerItemChange.to_json())

# convert the object into a dict
abstract_tracker_item_change_dict = abstract_tracker_item_change_instance.to_dict()
# create an instance of AbstractTrackerItemChange from a dict
abstract_tracker_item_change_form_dict = abstract_tracker_item_change.from_dict(abstract_tracker_item_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


