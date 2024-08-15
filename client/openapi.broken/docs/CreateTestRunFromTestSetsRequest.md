# CreateTestRunFromTestSetsRequest

Request model to create a test run from multiple test sets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_only_accepted_test_cases** | **bool** | Generate Test Runs only from accepted Test Cases. | [optional] [default to False]
**test_run_model** | [**TrackerItem**](TrackerItem.md) |  | [optional] 
**test_set_refs** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Test set ids to include into the test run. Only the first test set will be considered. | [optional] 

## Example

```python
from openapi_client.models.create_test_run_from_test_sets_request import CreateTestRunFromTestSetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTestRunFromTestSetsRequest from a JSON string
create_test_run_from_test_sets_request_instance = CreateTestRunFromTestSetsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTestRunFromTestSetsRequest.to_json())

# convert the object into a dict
create_test_run_from_test_sets_request_dict = create_test_run_from_test_sets_request_instance.to_dict()
# create an instance of CreateTestRunFromTestSetsRequest from a dict
create_test_run_from_test_sets_request_form_dict = create_test_run_from_test_sets_request.from_dict(create_test_run_from_test_sets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


