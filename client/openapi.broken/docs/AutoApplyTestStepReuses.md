# AutoApplyTestStepReuses

Specifies which Test Cases are checked for duplicate Steps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_test_case_libraries** | **bool** | If it scans/finds the duplicate Steps in Test Case libraries of the user? Note: that only Reusable Steps will be reused from these libraries! | [optional] 
**test_cases** | [**List[TrackerItemReference]**](TrackerItemReference.md) | The Test Cases to find the duplicated steps inside: if these Test Cases has duplicated Steps these will be converted to Step-Reuses. | [optional] 

## Example

```python
from openapi_client.models.auto_apply_test_step_reuses import AutoApplyTestStepReuses

# TODO update the JSON string below
json = "{}"
# create an instance of AutoApplyTestStepReuses from a JSON string
auto_apply_test_step_reuses_instance = AutoApplyTestStepReuses.from_json(json)
# print the JSON string representation of the object
print(AutoApplyTestStepReuses.to_json())

# convert the object into a dict
auto_apply_test_step_reuses_dict = auto_apply_test_step_reuses_instance.to_dict()
# create an instance of AutoApplyTestStepReuses from a dict
auto_apply_test_step_reuses_form_dict = auto_apply_test_step_reuses.from_dict(auto_apply_test_step_reuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


