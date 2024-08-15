# RestException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.rest_exception import RestException

# TODO update the JSON string below
json = "{}"
# create an instance of RestException from a JSON string
rest_exception_instance = RestException.from_json(json)
# print the JSON string representation of the object
print(RestException.to_json())

# convert the object into a dict
rest_exception_dict = rest_exception_instance.to_dict()
# create an instance of RestException from a dict
rest_exception_form_dict = rest_exception.from_dict(rest_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


