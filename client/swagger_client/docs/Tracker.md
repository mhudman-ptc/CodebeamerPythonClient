# Tracker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_as_template** | **bool** | Indicator if the tracker can be used as a template | [optional] 
**color** | **str** | Color of the tracker | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**default_show_ancestor_items** | **bool** | Default Outline should show Ancestor Items or not | 
**default_show_descendant_items** | **bool** | Default Outline should show Descendant Items or not | 
**deleted** | **bool** | Indicator if the tracker is deleted | 
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**hidden** | **bool** | Indicator if the tracker is hidden | 
**id** | **int** | Id of the entity | [optional] 
**key_name** | **str** | Keyname of a tracker | [optional] 
**modified_at** | **datetime** | The date when the entity was modified | [optional] 
**modified_by** | [**UserReference**](UserReference.md) |  | [optional] 
**name** | **str** | Name of the entity | [optional] 
**only_workflow_can_create_new_referring_item** | **bool** | If true, then the only way to create new referring items is through workflow actions | 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**shared_in_working_set** | **bool** | If the tracker is shared in a WorkingSet | [optional] 
**template_tracker** | [**TrackerReference**](TrackerReference.md) |  | [optional] 
**tracker_field_layout_settings_model** | [**TrackerFieldLayoutSettings**](TrackerFieldLayoutSettings.md) |  | [optional] 
**type** | [**TrackerTypeReference**](TrackerTypeReference.md) |  | [optional] 
**using_quick_transitions** | **bool** | If true, then every transition will be executed immediately (if possible) without opening an editor for the item | 
**using_workflow** | **bool** | Should transitions and workflow actions be available in the tracker or not | 
**version** | **int** | Version of a tracker | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

