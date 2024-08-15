# ReportGroup

A report group which can contain rows or other groups based on the type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregates** | [**List[ReportAggregate]**](ReportAggregate.md) | List of the aggregate values with column id. | [optional] 
**count** | **float** | Number of items in the group, if it has subgroups then the aggregated number of items. | [optional] 
**grouping_value** | **str** | The common value in the group, , if it&#39;s available | [optional] 
**grouping_value_id** | **int** | The id of the common value in the group, if it&#39;s available | [optional] 
**header** | **str** | Grouping header | [optional] 
**type** | **str** | Type of the group. | [optional] 

## Example

```python
from openapi_client.models.report_group import ReportGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGroup from a JSON string
report_group_instance = ReportGroup.from_json(json)
# print the JSON string representation of the object
print(ReportGroup.to_json())

# convert the object into a dict
report_group_dict = report_group_instance.to_dict()
# create an instance of ReportGroup from a dict
report_group_form_dict = report_group.from_dict(report_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


