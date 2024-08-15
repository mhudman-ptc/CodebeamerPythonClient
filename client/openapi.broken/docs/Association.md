# Association

Basic properties of a codebeamer association

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_id** | **int** | Baseline ID | [optional] 
**bi_directional_propagation** | **bool** | Bi-directional reference | [optional] 
**created_at** | **datetime** | The date when the entity was created | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**description** | **str** | Description of the entity | [optional] 
**description_format** | **str** | Description format of the entity | [optional] 
**var_from** | [**AbstractReference**](AbstractReference.md) |  | 
**id** | **int** | Id of the entity | [optional] 
**name** | **str** | Name of the entity | [optional] 
**propagating_dependencies** | **bool** | Propagating dependencies | [optional] 
**propagating_suspects** | **bool** | Propagating suspects | [optional] 
**reverse_propagation** | **bool** | Reverse propagation | [optional] 
**to** | [**AbstractReference**](AbstractReference.md) |  | [optional] 
**type** | [**AssociationTypeReference**](AssociationTypeReference.md) |  | [optional] 
**url** | **str** | Association to url | [optional] 

## Example

```python
from openapi_client.models.association import Association

# TODO update the JSON string below
json = "{}"
# create an instance of Association from a JSON string
association_instance = Association.from_json(json)
# print the JSON string representation of the object
print(Association.to_json())

# convert the object into a dict
association_dict = association_instance.to_dict()
# create an instance of Association from a dict
association_form_dict = association.from_dict(association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


