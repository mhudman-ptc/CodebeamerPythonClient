# TrackerItem

Basic properties of a codebeamer tracker item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued_millis** | **int** | Accrued work time of a tracker item in milliseconds | [optional] [readonly] 
**areas** | [**List[AbstractReference]**](AbstractReference.md) | Areas of a tracker item | [optional] 
**assigned_at** | **datetime** | Assignee date of a tracker item | [optional] [readonly] 
**assigned_to** | [**List[AbstractReference]**](AbstractReference.md) | Assignees of a tracker item | [optional] 
**categories** | [**List[AbstractReference]**](AbstractReference.md) | Categories of a tracker item | [optional] 
**children** | [**List[TrackerItemReference]**](TrackerItemReference.md) | Children of a tracker item | [optional] [readonly] 
**closed_at** | **datetime** | Close date of a tracker item | [optional] 
**comments** | [**List[CommentReference]**](CommentReference.md) | Comment in the tracker item | [optional] [readonly] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**custom_fields** | [**List[AbstractFieldValue]**](AbstractFieldValue.md) | Custom field of a tracker item | [optional] 
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**end_date** | **datetime** | End date of a tracker item | [optional] 
**estimated_millis** | **int** | Estimated work time of a tracker item in milliseconds | [optional] 
**formality** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**id** | **int** | Id of the entity | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**name** | **str** | Name of the entity | [optional] 
**ordinal** | **int** | Ordinal of a tracker item | [optional] 
**owners** | [**List[AbstractReference]**](AbstractReference.md) | Owners of a tracker item | [optional] 
**parent** | [**TrackerItemReference**](TrackerItemReference.md) |  | [optional] 
**platforms** | [**List[AbstractReference]**](AbstractReference.md) | Platforms of a tracker item | [optional] 
**priority** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**release_method** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**resolutions** | [**List[AbstractReference]**](AbstractReference.md) | Resolutions of a tracker item | [optional] 
**severities** | [**List[AbstractReference]**](AbstractReference.md) | Severities of a tracker item | [optional] 
**spent_millis** | **int** | Spent work time of a tracker item in milliseconds | [optional] 
**start_date** | **datetime** | Start date of a tracker item | [optional] 
**status** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**story_points** | **int** | Story points of a tracker item | [optional] 
**subjects** | [**List[AbstractReference]**](AbstractReference.md) | Subjects of a tracker item | [optional] 
**tags** | [**List[Label]**](Label.md) | Tags of the tracker item | [optional] [readonly] 
**teams** | [**List[AbstractReference]**](AbstractReference.md) | Teams of a tracker item | [optional] 
**tracker** | [**TrackerReference**](TrackerReference.md) |  | [optional] 
**type_name** | **str** | Type name of a tracker item | [optional] 
**version** | **int** | Version of a tracker item | [optional] [readonly] 
**versions** | [**List[AbstractReference]**](AbstractReference.md) | Versions of a tracker item | [optional] 

## Example

```python
from openapi_client.models.tracker_item import TrackerItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerItem from a JSON string
tracker_item_instance = TrackerItem.from_json(json)
# print the JSON string representation of the object
print(TrackerItem.to_json())

# convert the object into a dict
tracker_item_dict = tracker_item_instance.to_dict()
# create an instance of TrackerItem from a dict
tracker_item_form_dict = tracker_item.from_dict(tracker_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


