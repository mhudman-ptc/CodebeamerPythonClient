# TrackerItemRelationsResult

References to a tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downstream_references** | [**List[DownstreamTrackerItemReference]**](DownstreamTrackerItemReference.md) | References and associations to the item | [optional] 
**incoming_associations** | [**List[IncomingTrackerItemAssociation]**](IncomingTrackerItemAssociation.md) | References and associations to the item | [optional] 
**is_last_page** | **bool** | Set to true if it is the last page | [optional] 
**item_count** | **int** | Number of items on page | [optional] 
**item_id** | [**TrackerItemRevision**](TrackerItemRevision.md) |  | [optional] 
**outgoing_associations** | [**List[OutgoingTrackerItemAssociation]**](OutgoingTrackerItemAssociation.md) | References and associations to the item | [optional] 
**page** | **int** | Page no. | [optional] 
**page_size** | **int** | Page size | [optional] 
**upstream_references** | [**List[UpstreamTrackerItemReference]**](UpstreamTrackerItemReference.md) | References and associations to the item | [optional] 

## Example

```python
from openapi_client.models.tracker_item_relations_result import TrackerItemRelationsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemRelationsResult from a JSON string
tracker_item_relations_result_instance = TrackerItemRelationsResult.from_json(json)
# print the JSON string representation of the object
print(TrackerItemRelationsResult.to_json())

# convert the object into a dict
tracker_item_relations_result_dict = tracker_item_relations_result_instance.to_dict()
# create an instance of TrackerItemRelationsResult from a dict
tracker_item_relations_result_form_dict = tracker_item_relations_result.from_dict(tracker_item_relations_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


