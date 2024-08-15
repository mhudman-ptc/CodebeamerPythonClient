# UpdateTrackerItemFieldWithItemId

Update fields of a tracker item and provide the itemId as well

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_values** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Fields of a tracker item | [optional] 
**item_id** | **int** | Id of a tracker item | [optional] 
**table_values** | [**List[TableFieldValue]**](TableFieldValue.md) | Fields of a tracker item | [optional] 

## Example

```python
from openapi_client.models.update_tracker_item_field_with_item_id import UpdateTrackerItemFieldWithItemId

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrackerItemFieldWithItemId from a JSON string
update_tracker_item_field_with_item_id_instance = UpdateTrackerItemFieldWithItemId.from_json(json)
# print the JSON string representation of the object
print(UpdateTrackerItemFieldWithItemId.to_json())

# convert the object into a dict
update_tracker_item_field_with_item_id_dict = update_tracker_item_field_with_item_id_instance.to_dict()
# create an instance of UpdateTrackerItemFieldWithItemId from a dict
update_tracker_item_field_with_item_id_form_dict = update_tracker_item_field_with_item_id.from_dict(update_tracker_item_field_with_item_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


