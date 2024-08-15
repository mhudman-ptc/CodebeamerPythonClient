# UpdateTestRunRequest

Model to contain Test Case run update request models

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_result_propagation** | **bool** | The propagation of the result is enabled for parent Test Run or not | [optional] [default to True]
**update_request_models** | [**List[UpdateTestCaseRunRequest]**](UpdateTestCaseRunRequest.md) | List of update Test Case run request models | 

## Example

```python
from openapi_client.models.update_test_run_request import UpdateTestRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTestRunRequest from a JSON string
update_test_run_request_instance = UpdateTestRunRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTestRunRequest.to_json())

# convert the object into a dict
update_test_run_request_dict = update_test_run_request_instance.to_dict()
# create an instance of UpdateTestRunRequest from a dict
update_test_run_request_form_dict = update_test_run_request.from_dict(update_test_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


