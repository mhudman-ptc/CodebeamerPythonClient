# FieldReference

Reference to a field of a specific tracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_field_names** | **List[str]** | The names of a shared fields assigned to the field. | [optional] [readonly] 
**tracker_id** | **int** | Id of the tracker | [optional] 

## Example

```python
from openapi_client.models.field_reference import FieldReference

# TODO update the JSON string below
json = "{}"
# create an instance of FieldReference from a JSON string
field_reference_instance = FieldReference.from_json(json)
# print the JSON string representation of the object
print(FieldReference.to_json())

# convert the object into a dict
field_reference_dict = field_reference_instance.to_dict()
# create an instance of FieldReference from a dict
field_reference_form_dict = field_reference.from_dict(field_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


