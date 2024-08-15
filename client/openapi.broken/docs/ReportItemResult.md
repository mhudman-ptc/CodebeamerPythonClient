# ReportItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReportItem]**](ReportItem.md) | Found tracker items | [optional] 
**page** | **int** | Index of the page | [optional] 
**page_size** | **int** | Size of the found page | [optional] 
**total** | **int** | Number of matched tracker items by the search criteria | [optional] 

## Example

```python
from openapi_client.models.report_item_result import ReportItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReportItemResult from a JSON string
report_item_result_instance = ReportItemResult.from_json(json)
# print the JSON string representation of the object
print(ReportItemResult.to_json())

# convert the object into a dict
report_item_result_dict = report_item_result_instance.to_dict()
# create an instance of ReportItemResult from a dict
report_item_result_form_dict = report_item_result.from_dict(report_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


