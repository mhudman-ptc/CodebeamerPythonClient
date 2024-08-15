# TrackerFieldStatusPermissions

Field permissions by role for specific status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[AccessPermission]**](AccessPermission.md) | Access permissions by role | [optional] 
**status** | [**ChoiceOptionReference**](ChoiceOptionReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_status_permissions import TrackerFieldStatusPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldStatusPermissions from a JSON string
tracker_field_status_permissions_instance = TrackerFieldStatusPermissions.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldStatusPermissions.to_json())

# convert the object into a dict
tracker_field_status_permissions_dict = tracker_field_status_permissions_instance.to_dict()
# create an instance of TrackerFieldStatusPermissions from a dict
tracker_field_status_permissions_form_dict = tracker_field_status_permissions.from_dict(tracker_field_status_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


