# TrackerFieldComputedFieldReference

Describes the Computed Field Reference configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_field_id** | **int** |  | [optional] 
**referred_field_tracker_id** | **int** |  | [optional] 
**referred_tracker_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tracker_field_computed_field_reference import TrackerFieldComputedFieldReference

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFieldComputedFieldReference from a JSON string
tracker_field_computed_field_reference_instance = TrackerFieldComputedFieldReference.from_json(json)
# print the JSON string representation of the object
print(TrackerFieldComputedFieldReference.to_json())

# convert the object into a dict
tracker_field_computed_field_reference_dict = tracker_field_computed_field_reference_instance.to_dict()
# create an instance of TrackerFieldComputedFieldReference from a dict
tracker_field_computed_field_reference_form_dict = tracker_field_computed_field_reference.from_dict(tracker_field_computed_field_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


