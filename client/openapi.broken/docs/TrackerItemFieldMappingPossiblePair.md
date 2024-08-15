# TrackerItemFieldMappingPossiblePair

Possible Tracker field mapping pair

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**possible_target_fields** | [**List[TrackerItemFieldMapping]**](TrackerItemFieldMapping.md) | Possible Target Tracker field information | [optional] 
**source_field** | [**TrackerItemFieldMapping**](TrackerItemFieldMapping.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_mapping_possible_pair import TrackerItemFieldMappingPossiblePair

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldMappingPossiblePair from a JSON string
tracker_item_field_mapping_possible_pair_instance = TrackerItemFieldMappingPossiblePair.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldMappingPossiblePair.to_json())

# convert the object into a dict
tracker_item_field_mapping_possible_pair_dict = tracker_item_field_mapping_possible_pair_instance.to_dict()
# create an instance of TrackerItemFieldMappingPossiblePair from a dict
tracker_item_field_mapping_possible_pair_form_dict = tracker_item_field_mapping_possible_pair.from_dict(tracker_item_field_mapping_possible_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


