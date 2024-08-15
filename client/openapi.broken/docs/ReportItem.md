# ReportItem

An item of the report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_real_result** | **bool** | Indicator if the item is a real query result (e.g. not an ancestor item). | [optional] 
**item** | [**TrackerItem**](TrackerItem.md) |  | [optional] 
**outline_level** | **int** | Item&#39;s level in the tracker outline. | [optional] 

## Example

```python
from openapi_client.models.report_item import ReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportItem from a JSON string
report_item_instance = ReportItem.from_json(json)
# print the JSON string representation of the object
print(ReportItem.to_json())

# convert the object into a dict
report_item_dict = report_item_instance.to_dict()
# create an instance of ReportItem from a dict
report_item_form_dict = report_item.from_dict(report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


