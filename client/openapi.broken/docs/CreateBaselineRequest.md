# CreateBaselineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of baseline | [optional] 
**name** | **str** | Name of baseline | 
**project** | [**ProjectReference**](ProjectReference.md) |  | 
**tracker** | [**TrackerReference**](TrackerReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_baseline_request import CreateBaselineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBaselineRequest from a JSON string
create_baseline_request_instance = CreateBaselineRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBaselineRequest.to_json())

# convert the object into a dict
create_baseline_request_dict = create_baseline_request_instance.to_dict()
# create an instance of CreateBaselineRequest from a dict
create_baseline_request_form_dict = create_baseline_request.from_dict(create_baseline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


