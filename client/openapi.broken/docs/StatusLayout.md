# StatusLayout

statusLayout of a tracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** | layout of a statusLayout | [optional] 
**status** | **str** | status of a statusLayout | [optional] 

## Example

```python
from openapi_client.models.status_layout import StatusLayout

# TODO update the JSON string below
json = "{}"
# create an instance of StatusLayout from a JSON string
status_layout_instance = StatusLayout.from_json(json)
# print the JSON string representation of the object
print(StatusLayout.to_json())

# convert the object into a dict
status_layout_dict = status_layout_instance.to_dict()
# create an instance of StatusLayout from a dict
status_layout_form_dict = status_layout.from_dict(status_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


