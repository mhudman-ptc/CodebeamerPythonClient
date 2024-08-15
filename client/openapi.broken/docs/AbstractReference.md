# AbstractReference

Reference to an item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**type** | **str** | Type of a referenced object | [optional] 

## Example

```python
from openapi_client.models.abstract_reference import AbstractReference

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractReference from a JSON string
abstract_reference_instance = AbstractReference.from_json(json)
# print the JSON string representation of the object
print(AbstractReference.to_json())

# convert the object into a dict
abstract_reference_dict = abstract_reference_instance.to_dict()
# create an instance of AbstractReference from a dict
abstract_reference_form_dict = abstract_reference.from_dict(abstract_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


