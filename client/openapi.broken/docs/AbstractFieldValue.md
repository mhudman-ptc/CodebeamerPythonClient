# AbstractFieldValue

Value container of a field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **int** | Id of the field | [optional] 
**name** | **str** | Name of the field | [optional] 
**shared_field_name** | **str** | The name of a shared field assigned to the field. This can be specified as an alternative to fieldId. | [optional] 
**shared_field_names** | **List[str]** | The names of a shared fields assigned to the field. | [optional] 
**type** | **str** | Type of the field | 

## Example

```python
from openapi_client.models.abstract_field_value import AbstractFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractFieldValue from a JSON string
abstract_field_value_instance = AbstractFieldValue.from_json(json)
# print the JSON string representation of the object
print(AbstractFieldValue.to_json())

# convert the object into a dict
abstract_field_value_dict = abstract_field_value_instance.to_dict()
# create an instance of AbstractFieldValue from a dict
abstract_field_value_form_dict = abstract_field_value.from_dict(abstract_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


