# ReportGroupWithGroups

ReportGroup having subgroups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[ReportGroup]**](ReportGroup.md) | Subgroups in the group. | [optional] 

## Example

```python
from openapi_client.models.report_group_with_groups import ReportGroupWithGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ReportGroupWithGroups from a JSON string
report_group_with_groups_instance = ReportGroupWithGroups.from_json(json)
# print the JSON string representation of the object
print(ReportGroupWithGroups.to_json())

# convert the object into a dict
report_group_with_groups_dict = report_group_with_groups_instance.to_dict()
# create an instance of ReportGroupWithGroups from a dict
report_group_with_groups_form_dict = report_group_with_groups.from_dict(report_group_with_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


