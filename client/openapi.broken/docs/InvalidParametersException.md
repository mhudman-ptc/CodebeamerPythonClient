# InvalidParametersException


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invalid_parameters_exception import InvalidParametersException

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParametersException from a JSON string
invalid_parameters_exception_instance = InvalidParametersException.from_json(json)
# print the JSON string representation of the object
print(InvalidParametersException.to_json())

# convert the object into a dict
invalid_parameters_exception_dict = invalid_parameters_exception_instance.to_dict()
# create an instance of InvalidParametersException from a dict
invalid_parameters_exception_form_dict = invalid_parameters_exception.from_dict(invalid_parameters_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


