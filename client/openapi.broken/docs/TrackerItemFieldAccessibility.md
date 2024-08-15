# TrackerItemFieldAccessibility

Accessibilities of fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editable** | **bool** | Field is editable | [optional] 
**field** | [**FieldReference**](FieldReference.md) |  | [optional] 
**mandatory** | **bool** | Field is mandatory | [optional] 
**visible** | **bool** | Field is visible | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_accessibility import TrackerItemFieldAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldAccessibility from a JSON string
tracker_item_field_accessibility_instance = TrackerItemFieldAccessibility.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldAccessibility.to_json())

# convert the object into a dict
tracker_item_field_accessibility_dict = tracker_item_field_accessibility_instance.to_dict()
# create an instance of TrackerItemFieldAccessibility from a dict
tracker_item_field_accessibility_form_dict = tracker_item_field_accessibility.from_dict(tracker_item_field_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


