# ReportPermission

Access permissions for the report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access level | 
**project** | [**ProjectReference**](ProjectReference.md) |  | 
**role** | [**RoleReference**](RoleReference.md) |  | 

## Example

```python
from openapi_client.models.report_permission import ReportPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPermission from a JSON string
report_permission_instance = ReportPermission.from_json(json)
# print the JSON string representation of the object
print(ReportPermission.to_json())

# convert the object into a dict
report_permission_dict = report_permission_instance.to_dict()
# create an instance of ReportPermission from a dict
report_permission_form_dict = report_permission.from_dict(report_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


