# AbstractBaselineReferenceModel

Baseline used when creating the working set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**type** | **str** | Type of a referenced object | [optional] 

## Example

```python
from openapi_client.models.abstract_baseline_reference_model import AbstractBaselineReferenceModel

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractBaselineReferenceModel from a JSON string
abstract_baseline_reference_model_instance = AbstractBaselineReferenceModel.from_json(json)
# print the JSON string representation of the object
print(AbstractBaselineReferenceModel.to_json())

# convert the object into a dict
abstract_baseline_reference_model_dict = abstract_baseline_reference_model_instance.to_dict()
# create an instance of AbstractBaselineReferenceModel from a dict
abstract_baseline_reference_model_form_dict = abstract_baseline_reference_model.from_dict(abstract_baseline_reference_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


