# ResourceNotFoundException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_not_found_exception import ResourceNotFoundException

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNotFoundException from a JSON string
resource_not_found_exception_instance = ResourceNotFoundException.from_json(json)
# print the JSON string representation of the object
print(ResourceNotFoundException.to_json())

# convert the object into a dict
resource_not_found_exception_dict = resource_not_found_exception_instance.to_dict()
# create an instance of ResourceNotFoundException from a dict
resource_not_found_exception_form_dict = resource_not_found_exception.from_dict(resource_not_found_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


