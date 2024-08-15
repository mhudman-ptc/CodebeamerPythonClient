# LayoutField

fieldModel of a groupsModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | field of a fieldModel | [optional] 
**field_id** | **int** | fieldId of a fieldModel | [optional] 
**width** | **str** | width of a fieldModel | [optional] 

## Example

```python
from openapi_client.models.layout_field import LayoutField

# TODO update the JSON string below
json = "{}"
# create an instance of LayoutField from a JSON string
layout_field_instance = LayoutField.from_json(json)
# print the JSON string representation of the object
print(LayoutField.to_json())

# convert the object into a dict
layout_field_dict = layout_field_instance.to_dict()
# create an instance of LayoutField from a dict
layout_field_form_dict = layout_field.from_dict(layout_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


