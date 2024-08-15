# WorkflowTransition

A transition in the workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**from_status** | [**ChoiceOptionReference**](ChoiceOptionReference.md) |  | [optional] 
**hidden** | **bool** | Indicator if the transition is hidden | [optional] 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**permissions** | [**List[AccessPermission]**](AccessPermission.md) | Access permissions of the transition | [optional] 
**to_status** | [**ChoiceOptionReference**](ChoiceOptionReference.md) |  | 

## Example

```python
from openapi_client.models.workflow_transition import WorkflowTransition

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTransition from a JSON string
workflow_transition_instance = WorkflowTransition.from_json(json)
# print the JSON string representation of the object
print(WorkflowTransition.to_json())

# convert the object into a dict
workflow_transition_dict = workflow_transition_instance.to_dict()
# create an instance of WorkflowTransition from a dict
workflow_transition_form_dict = workflow_transition.from_dict(workflow_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


