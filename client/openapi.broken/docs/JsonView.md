# JsonView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**var_json** | **str** |  | [optional] 
**json_object** | [**JsonView**](JsonView.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_view import JsonView

# TODO update the JSON string below
json = "{}"
# create an instance of JsonView from a JSON string
json_view_instance = JsonView.from_json(json)
# print the JSON string representation of the object
print(JsonView.to_json())

# convert the object into a dict
json_view_dict = json_view_instance.to_dict()
# create an instance of JsonView from a dict
json_view_form_dict = json_view.from_dict(json_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


