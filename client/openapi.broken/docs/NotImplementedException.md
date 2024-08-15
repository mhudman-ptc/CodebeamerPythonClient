# NotImplementedException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.not_implemented_exception import NotImplementedException

# TODO update the JSON string below
json = "{}"
# create an instance of NotImplementedException from a JSON string
not_implemented_exception_instance = NotImplementedException.from_json(json)
# print the JSON string representation of the object
print(NotImplementedException.to_json())

# convert the object into a dict
not_implemented_exception_dict = not_implemented_exception_instance.to_dict()
# create an instance of NotImplementedException from a dict
not_implemented_exception_form_dict = not_implemented_exception.from_dict(not_implemented_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


