# CreateTestRunRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_only_accepted_test_cases** | **bool** | Generate Test Runs only from accepted Test Cases. | [optional] [default to False]
**test_case_ids** | [**list[TrackerItemReference]**](TrackerItemReference.md) |  | [optional] 
**test_case_refs** | [**list[TrackerItemReference]**](TrackerItemReference.md) | Test case ids to include into the test run | [optional] 
**test_run_model** | [**TrackerItem**](TrackerItem.md) |  | [optional] 
**test_set_ids** | [**list[TrackerItemReference]**](TrackerItemReference.md) |  | [optional] 
**test_set_refs** | [**list[TrackerItemReference]**](TrackerItemReference.md) | Test set ids to include into the test run. Only the first test set will be considered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

