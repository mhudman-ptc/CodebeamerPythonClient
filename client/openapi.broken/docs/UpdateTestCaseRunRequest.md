# UpdateTestCaseRunRequest

Request model to update Test Run's result for a Test Case

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **str** | Optional conclusion text | [optional] 
**custom_fields** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Optional field values to set on the Test Run | [optional] 
**reported_bug_references** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Optional reference list of Bugs attached to the Test result | [optional] 
**result** | **str** | Result of the test case | 
**run_time** | **int** | Optional runtime in seconds | [optional] 
**test_case_reference** | [**TrackerItemReference**](TrackerItemReference.md) |  | 

## Example

```python
from openapi_client.models.update_test_case_run_request import UpdateTestCaseRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTestCaseRunRequest from a JSON string
update_test_case_run_request_instance = UpdateTestCaseRunRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTestCaseRunRequest.to_json())

# convert the object into a dict
update_test_case_run_request_dict = update_test_case_run_request_instance.to_dict()
# create an instance of UpdateTestCaseRunRequest from a dict
update_test_case_run_request_form_dict = update_test_case_run_request.from_dict(update_test_case_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


