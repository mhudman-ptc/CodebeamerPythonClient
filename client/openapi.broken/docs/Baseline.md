# Baseline

Properties of a baseline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**tracker** | [**TrackerReference**](TrackerReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.baseline import Baseline

# TODO update the JSON string below
json = "{}"
# create an instance of Baseline from a JSON string
baseline_instance = Baseline.from_json(json)
# print the JSON string representation of the object
print(Baseline.to_json())

# convert the object into a dict
baseline_dict = baseline_instance.to_dict()
# create an instance of Baseline from a dict
baseline_form_dict = baseline.from_dict(baseline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


