# ReportItemReference

Reference data of an underlying item of a row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | Identifier of the underlying item. | [optional] 
**tracker_id** | **int** | Identifier of the tracker of the underlying item. | [optional] 

## Example

```python
from openapi_client.models.report_item_reference import ReportItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReportItemReference from a JSON string
report_item_reference_instance = ReportItemReference.from_json(json)
# print the JSON string representation of the object
print(ReportItemReference.to_json())

# convert the object into a dict
report_item_reference_dict = report_item_reference_instance.to_dict()
# create an instance of ReportItemReference from a dict
report_item_reference_form_dict = report_item_reference.from_dict(report_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


