# TrackerConfiguration

This model represents the whole Tracker configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_information** | [**TrackerBasicInformation**](TrackerBasicInformation.md) |  | [optional] 
**fields** | [**List[TrackerField]**](TrackerField.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracker_configuration import TrackerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerConfiguration from a JSON string
tracker_configuration_instance = TrackerConfiguration.from_json(json)
# print the JSON string representation of the object
print(TrackerConfiguration.to_json())

# convert the object into a dict
tracker_configuration_dict = tracker_configuration_instance.to_dict()
# create an instance of TrackerConfiguration from a dict
tracker_configuration_form_dict = tracker_configuration.from_dict(tracker_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


