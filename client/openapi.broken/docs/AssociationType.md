# AssociationType

Basic properties of a codebeamer association type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 

## Example

```python
from openapi_client.models.association_type import AssociationType

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationType from a JSON string
association_type_instance = AssociationType.from_json(json)
# print the JSON string representation of the object
print(AssociationType.to_json())

# convert the object into a dict
association_type_dict = association_type_instance.to_dict()
# create an instance of AssociationType from a dict
association_type_form_dict = association_type.from_dict(association_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


