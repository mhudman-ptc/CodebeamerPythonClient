# TraceabilityResult

Traceability result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_warnings** | **str** | limit warnings | [optional] 
**traceability_items** | [**List[TraceabilityItem]**](TraceabilityItem.md) | traceability items | [optional] 

## Example

```python
from openapi_client.models.traceability_result import TraceabilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of TraceabilityResult from a JSON string
traceability_result_instance = TraceabilityResult.from_json(json)
# print the JSON string representation of the object
print(TraceabilityResult.to_json())

# convert the object into a dict
traceability_result_dict = traceability_result_instance.to_dict()
# create an instance of TraceabilityResult from a dict
traceability_result_form_dict = traceability_result.from_dict(traceability_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


