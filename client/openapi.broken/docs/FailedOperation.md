# FailedOperation

Holds the details of a failed operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_message** | **str** | Exception message | [optional] 
**id** | **int** | Entity id | [optional] 

## Example

```python
from openapi_client.models.failed_operation import FailedOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FailedOperation from a JSON string
failed_operation_instance = FailedOperation.from_json(json)
# print the JSON string representation of the object
print(FailedOperation.to_json())

# convert the object into a dict
failed_operation_dict = failed_operation_instance.to_dict()
# create an instance of FailedOperation from a dict
failed_operation_form_dict = failed_operation.from_dict(failed_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


