# ChoiceDocuments

Describes a Documents Choice Option field configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_filters** | [**List[ReferenceFilterBasedChoiceReferenceFilter]**](ReferenceFilterBasedChoiceReferenceFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.choice_documents import ChoiceDocuments

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceDocuments from a JSON string
choice_documents_instance = ChoiceDocuments.from_json(json)
# print the JSON string representation of the object
print(ChoiceDocuments.to_json())

# convert the object into a dict
choice_documents_dict = choice_documents_instance.to_dict()
# create an instance of ChoiceDocuments from a dict
choice_documents_form_dict = choice_documents.from_dict(choice_documents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


