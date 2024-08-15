# AutomatedTestCaseRunResult

Request model to create a test run from test case

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **str** | Optional Test Case Run conclusion | [optional] 
**description** | **str** | Description of the Test Case | [optional] 
**group_name** | **str** | Group name of the Test Case | [optional] 
**name** | **str** | Name of the Test Case | 
**result** | **str** | Result of the test case | 
**run_time** | **int** | Optional runtime in seconds | [optional] 

## Example

```python
from openapi_client.models.automated_test_case_run_result import AutomatedTestCaseRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedTestCaseRunResult from a JSON string
automated_test_case_run_result_instance = AutomatedTestCaseRunResult.from_json(json)
# print the JSON string representation of the object
print(AutomatedTestCaseRunResult.to_json())

# convert the object into a dict
automated_test_case_run_result_dict = automated_test_case_run_result_instance.to_dict()
# create an instance of AutomatedTestCaseRunResult from a dict
automated_test_case_run_result_form_dict = automated_test_case_run_result.from_dict(automated_test_case_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


