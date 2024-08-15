# ReportPagingInformation

Paging information of the current result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Index of the page | [optional] 
**page_count** | **int** | Number of pages in the report | [optional] 
**page_size** | **int** | Size of the found page | [optional] 

## Example

```python
from openapi_client.models.report_paging_information import ReportPagingInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ReportPagingInformation from a JSON string
report_paging_information_instance = ReportPagingInformation.from_json(json)
# print the JSON string representation of the object
print(ReportPagingInformation.to_json())

# convert the object into a dict
report_paging_information_dict = report_paging_information_instance.to_dict()
# create an instance of ReportPagingInformation from a dict
report_paging_information_form_dict = report_paging_information.from_dict(report_paging_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


