# TrackerFilteringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** | True to also show removed trackers. | [optional] 
**hidden** | **bool** | True to also show hidden trackers. | [optional] 
**key_name** | **str** | Filter by project key name | [optional] 
**types** | [**List[TrackerTypeReference]**](TrackerTypeReference.md) | List of tracker type references, to only show trackers of these types. | [optional] 

## Example

```python
from openapi_client.models.tracker_filtering_request import TrackerFilteringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerFilteringRequest from a JSON string
tracker_filtering_request_instance = TrackerFilteringRequest.from_json(json)
# print the JSON string representation of the object
print(TrackerFilteringRequest.to_json())

# convert the object into a dict
tracker_filtering_request_dict = tracker_filtering_request_instance.to_dict()
# create an instance of TrackerFilteringRequest from a dict
tracker_filtering_request_form_dict = tracker_filtering_request.from_dict(tracker_filtering_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


