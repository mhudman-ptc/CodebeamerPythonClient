# TrackerItemField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editable_fields** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Fields which can be modified | [optional] 
**editable_table_fields** | [**List[TableFieldValue]**](TableFieldValue.md) | Table fields which can be modified | [optional] 
**read_only_fields** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Fields which are not writable in the current state | [optional] 
**read_only_table_fields** | [**List[TableFieldValue]**](TableFieldValue.md) | Table fields which are not writable in the current state | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field import TrackerItemField

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemField from a JSON string
tracker_item_field_instance = TrackerItemField.from_json(json)
# print the JSON string representation of the object
print(TrackerItemField.to_json())

# convert the object into a dict
tracker_item_field_dict = tracker_item_field_instance.to_dict()
# create an instance of TrackerItemField from a dict
tracker_item_field_form_dict = tracker_item_field.from_dict(tracker_item_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


