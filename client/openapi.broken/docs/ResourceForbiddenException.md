# ResourceForbiddenException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_forbidden_exception import ResourceForbiddenException

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceForbiddenException from a JSON string
resource_forbidden_exception_instance = ResourceForbiddenException.from_json(json)
# print the JSON string representation of the object
print(ResourceForbiddenException.to_json())

# convert the object into a dict
resource_forbidden_exception_dict = resource_forbidden_exception_instance.to_dict()
# create an instance of ResourceForbiddenException from a dict
resource_forbidden_exception_form_dict = resource_forbidden_exception.from_dict(resource_forbidden_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


