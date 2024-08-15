# TraceabilityItem

Traceability Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[TraceabilityItem]**](TraceabilityItem.md) | children | [optional] 
**incoming_association** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) |  | [optional] 
**incoming_reference** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) |  | [optional] 
**incoming_associations** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) | incoming associations | [optional] 
**incoming_references** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) | incoming references | [optional] 
**item_revision** | [**TrackerItemRevision**](TrackerItemRevision.md) |  | [optional] 
**outgoing_association** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) |  | [optional] 
**outgoing_reference** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) |  | [optional] 
**outgoing_associations** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) | outgoing association | [optional] 
**outgoing_references** | [**List[TrackerItemRevision]**](TrackerItemRevision.md) | outgoing reference | [optional] 

## Example

```python
from openapi_client.models.traceability_item import TraceabilityItem

# TODO update the JSON string below
json = "{}"
# create an instance of TraceabilityItem from a JSON string
traceability_item_instance = TraceabilityItem.from_json(json)
# print the JSON string representation of the object
print(TraceabilityItem.to_json())

# convert the object into a dict
traceability_item_dict = traceability_item_instance.to_dict()
# create an instance of TraceabilityItem from a dict
traceability_item_form_dict = traceability_item.from_dict(traceability_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


