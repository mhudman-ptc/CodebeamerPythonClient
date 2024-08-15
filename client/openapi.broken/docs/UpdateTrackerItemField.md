# UpdateTrackerItemField

Update fields of a tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_values** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Fields of a tracker item | [optional] 
**table_values** | [**List[TableFieldValue]**](TableFieldValue.md) | Fields of a tracker item | [optional] 

## Example

```python
from openapi_client.models.update_tracker_item_field import UpdateTrackerItemField

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrackerItemField from a JSON string
update_tracker_item_field_instance = UpdateTrackerItemField.from_json(json)
# print the JSON string representation of the object
print(UpdateTrackerItemField.to_json())

# convert the object into a dict
update_tracker_item_field_dict = update_tracker_item_field_instance.to_dict()
# create an instance of UpdateTrackerItemField from a dict
update_tracker_item_field_form_dict = update_tracker_item_field.from_dict(update_tracker_item_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


