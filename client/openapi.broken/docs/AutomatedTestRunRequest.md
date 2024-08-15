# AutomatedTestRunRequest

Request model to create a test run from test case runs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_non_existent_test_cases** | **bool** | Flag to create new test cases from testResults if necessary | [optional] 
**test_case_tracker_id** | **int** | ID of the Test Case tracker | 
**test_results** | [**List[AutomatedTestCaseRunResult]**](AutomatedTestCaseRunResult.md) | Test case results to include into the test run | 
**test_run_model** | [**TrackerItem**](TrackerItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.automated_test_run_request import AutomatedTestRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutomatedTestRunRequest from a JSON string
automated_test_run_request_instance = AutomatedTestRunRequest.from_json(json)
# print the JSON string representation of the object
print(AutomatedTestRunRequest.to_json())

# convert the object into a dict
automated_test_run_request_dict = automated_test_run_request_instance.to_dict()
# create an instance of AutomatedTestRunRequest from a dict
automated_test_run_request_form_dict = automated_test_run_request.from_dict(automated_test_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


