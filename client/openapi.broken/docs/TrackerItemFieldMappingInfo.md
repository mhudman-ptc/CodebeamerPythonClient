# TrackerItemFieldMappingInfo

Tracker field mapping information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lost_mapping** | [**List[TrackerItemFieldMapping]**](TrackerItemFieldMapping.md) | No mappable field exists, these fields will be lost | [optional] 
**mapping** | [**List[TrackerItemFieldMappingPair]**](TrackerItemFieldMappingPair.md) | Direct mappable fields | [optional] 
**possible_mapping** | [**List[TrackerItemFieldMappingPossiblePair]**](TrackerItemFieldMappingPossiblePair.md) | Not direct mappable fields, but possible mapping exist | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_mapping_info import TrackerItemFieldMappingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldMappingInfo from a JSON string
tracker_item_field_mapping_info_instance = TrackerItemFieldMappingInfo.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldMappingInfo.to_json())

# convert the object into a dict
tracker_item_field_mapping_info_dict = tracker_item_field_mapping_info_instance.to_dict()
# create an instance of TrackerItemFieldMappingInfo from a dict
tracker_item_field_mapping_info_form_dict = tracker_item_field_mapping_info.from_dict(tracker_item_field_mapping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


