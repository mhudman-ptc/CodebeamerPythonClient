# TrackerItemFieldMappingPair

Tracker field mapping pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_field** | [**TrackerItemFieldMapping**](TrackerItemFieldMapping.md) |  | 
**target_field** | [**TrackerItemFieldMapping**](TrackerItemFieldMapping.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_mapping_pair import TrackerItemFieldMappingPair

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldMappingPair from a JSON string
tracker_item_field_mapping_pair_instance = TrackerItemFieldMappingPair.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldMappingPair.to_json())

# convert the object into a dict
tracker_item_field_mapping_pair_dict = tracker_item_field_mapping_pair_instance.to_dict()
# create an instance of TrackerItemFieldMappingPair from a dict
tracker_item_field_mapping_pair_form_dict = tracker_item_field_mapping_pair.from_dict(tracker_item_field_mapping_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


