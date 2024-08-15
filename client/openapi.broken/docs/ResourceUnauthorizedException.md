# ResourceUnauthorizedException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_unauthorized_exception import ResourceUnauthorizedException

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUnauthorizedException from a JSON string
resource_unauthorized_exception_instance = ResourceUnauthorizedException.from_json(json)
# print the JSON string representation of the object
print(ResourceUnauthorizedException.to_json())

# convert the object into a dict
resource_unauthorized_exception_dict = resource_unauthorized_exception_instance.to_dict()
# create an instance of ResourceUnauthorizedException from a dict
resource_unauthorized_exception_form_dict = resource_unauthorized_exception.from_dict(resource_unauthorized_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


