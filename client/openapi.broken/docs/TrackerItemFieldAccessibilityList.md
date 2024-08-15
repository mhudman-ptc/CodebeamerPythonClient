# TrackerItemFieldAccessibilityList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[TrackerItemFieldAccessibility]**](TrackerItemFieldAccessibility.md) | Accessibilities of fields | [optional] 

## Example

```python
from openapi_client.models.tracker_item_field_accessibility_list import TrackerItemFieldAccessibilityList

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItemFieldAccessibilityList from a JSON string
tracker_item_field_accessibility_list_instance = TrackerItemFieldAccessibilityList.from_json(json)
# print the JSON string representation of the object
print(TrackerItemFieldAccessibilityList.to_json())

# convert the object into a dict
tracker_item_field_accessibility_list_dict = tracker_item_field_accessibility_list_instance.to_dict()
# create an instance of TrackerItemFieldAccessibilityList from a dict
tracker_item_field_accessibility_list_form_dict = tracker_item_field_accessibility_list.from_dict(tracker_item_field_accessibility_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


