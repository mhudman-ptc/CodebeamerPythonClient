# AbstractField

Abstract field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of a field | [optional] 
**formula** | **str** | Formula value of a field | [optional] 
**hidden** | **bool** | Visibility status of a field | [optional] 
**hide_if_dependency_formula** | **str** | Hide If dependency formula value of a field | [optional] 
**id** | **int** | Id of a field | [optional] 
**legacy_rest_name** | **str** | Identifier matching the legacy REST API naming | [optional] 
**mandatory_if_dependency_formula** | **str** | Mandatory If dependency formula value of a field | [optional] 
**mandatory_in_statuses** | [**List[ChoiceOptionReference]**](ChoiceOptionReference.md) | List of statuses where the field is mandatory. | [optional] 
**name** | **str** | Name of a field | [optional] 
**shared_fields** | [**List[SharedFieldReference]**](SharedFieldReference.md) | List of shared fields assigned to this field | [optional] 
**title** | **str** | Title of a field | [optional] 
**tracker_item_field** | **str** | Tracker item&#39;s field name for this field | [optional] 
**type** | **str** | Type of a field | [optional] 
**value_model** | **str** | Name of the updater/getter value model | [optional] 

## Example

```python
from openapi_client.models.abstract_field import AbstractField

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractField from a JSON string
abstract_field_instance = AbstractField.from_json(json)
# print the JSON string representation of the object
print(AbstractField.to_json())

# convert the object into a dict
abstract_field_dict = abstract_field_instance.to_dict()
# create an instance of AbstractField from a dict
abstract_field_form_dict = abstract_field.from_dict(abstract_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


