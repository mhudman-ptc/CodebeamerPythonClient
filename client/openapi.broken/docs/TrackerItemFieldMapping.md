# TrackerItemFieldMapping

Information of Tracker field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**var_property** | **str** | Tracker field property name | [optional] 
**type_name** | **str** | Tracker field type | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_mapping import TrackerItemFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldMapping from a JSON string
tracker_item_field_mapping_instance = TrackerItemFieldMapping.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldMapping.to_json())

# convert the object into a dict
tracker_item_field_mapping_dict = tracker_item_field_mapping_instance.to_dict()
# create an instance of TrackerItemFieldMapping from a dict
tracker_item_field_mapping_form_dict = tracker_item_field_mapping.from_dict(tracker_item_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


