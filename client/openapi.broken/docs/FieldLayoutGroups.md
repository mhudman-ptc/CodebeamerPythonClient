# FieldLayoutGroups

groupsModels of a fieldLayoutSettingsModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collapsed** | **bool** | collapsed of a groupsModel | [optional] 
**color** | **str** | color of a groupsModel | [optional] 
**default** | **bool** | default of a groupsModel | [optional] 
**fields** | [**List[LayoutField]**](LayoutField.md) | fieldModel of a groupsModel | [optional] 
**name** | **str** | name of a groupsModel | [optional] 

## Example

```python
from openapi_client.models.field_layout_groups import FieldLayoutGroups

# TODO update the JSON string below
json = "{}"
# create an instance of FieldLayoutGroups from a JSON string
field_layout_groups_instance = FieldLayoutGroups.from_json(json)
# print the JSON string representation of the object
print(FieldLayoutGroups.to_json())

# convert the object into a dict
field_layout_groups_dict = field_layout_groups_instance.to_dict()
# create an instance of FieldLayoutGroups from a dict
field_layout_groups_form_dict = field_layout_groups.from_dict(field_layout_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


