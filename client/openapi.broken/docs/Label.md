# Label

Label that is used for entities like tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**hidden** | **bool** | Whether the label is hidden or not | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**private_label** | **bool** | Whether the label is private or not | [optional] 

## Example

```python
from openapi_client.models.label import Label

# TODO update the JSON string below
json = "{}"
# create an instance of Label from a JSON string
label_instance = Label.from_json(json)
# print the JSON string representation of the object
print(Label.to_json())

# convert the object into a dict
label_dict = label_instance.to_dict()
# create an instance of Label from a dict
label_form_dict = label.from_dict(label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


