# TrackerFieldServiceDeskField

Describes the Service Desk related configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_service_desk_field import TrackerFieldServiceDeskField

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldServiceDeskField from a JSON string
tracker_field_service_desk_field_instance = TrackerFieldServiceDeskField.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldServiceDeskField.to_json())

# convert the object into a dict
tracker_field_service_desk_field_dict = tracker_field_service_desk_field_instance.to_dict()
# create an instance of TrackerFieldServiceDeskField from a dict
tracker_field_service_desk_field_form_dict = tracker_field_service_desk_field.from_dict(tracker_field_service_desk_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


