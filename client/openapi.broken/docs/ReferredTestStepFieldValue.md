# ReferredTestStepFieldValue

Value container of a referred test step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_step_id** | **str** | Id of the referred test step | 
**referred_test_case_id** | **int** | Id of the test case where the referred test step comes | 
**value** | **str** | Id of the Test Step | [optional] 

## Example

```python
from openapi_client.models.referred_test_step_field_value import ReferredTestStepFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of ReferredTestStepFieldValue from a JSON string
referred_test_step_field_value_instance = ReferredTestStepFieldValue.from_json(json)
# print the JSON string representation of the object
print(ReferredTestStepFieldValue.to_json())

# convert the object into a dict
referred_test_step_field_value_dict = referred_test_step_field_value_instance.to_dict()
# create an instance of ReferredTestStepFieldValue from a dict
referred_test_step_field_value_form_dict = referred_test_step_field_value.from_dict(referred_test_step_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


