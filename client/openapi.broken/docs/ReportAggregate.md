# ReportAggregate

Aggregated values for a column of a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **float** | Average of the column values | [optional] 
**column_ref** | **str** | Column reference | [optional] 
**maximum** | **float** | Average of the column values | [optional] 
**minimum** | **float** | Minimum of the column values | [optional] 
**sum** | **float** | Sum of the column values | [optional] 

## Example

```python
from openapi_client.models.report_aggregate import ReportAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAggregate from a JSON string
report_aggregate_instance = ReportAggregate.from_json(json)
# print the JSON string representation of the object
print(ReportAggregate.to_json())

# convert the object into a dict
report_aggregate_dict = report_aggregate_instance.to_dict()
# create an instance of ReportAggregate from a dict
report_aggregate_form_dict = report_aggregate.from_dict(report_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


