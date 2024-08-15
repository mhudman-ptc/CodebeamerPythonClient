# TestRunResult

Multiple Test Runs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_runs** | [**List[TrackerItem]**](TrackerItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.test_run_result import TestRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunResult from a JSON string
test_run_result_instance = TestRunResult.from_json(json)
# print the JSON string representation of the object
print(TestRunResult.to_json())

# convert the object into a dict
test_run_result_dict = test_run_result_instance.to_dict()
# create an instance of TestRunResult from a dict
test_run_result_form_dict = test_run_result.from_dict(test_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


