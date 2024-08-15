# OutlineWiki

A model created for wiki page outline models

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wiki_page_reference_model** | [**WikiPageReference**](WikiPageReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.outline_wiki import OutlineWiki

# TODO update the JSON string below
json = "{}"
# create an instance of OutlineWiki from a JSON string
outline_wiki_instance = OutlineWiki.from_json(json)
# print the JSON string representation of the object
print(OutlineWiki.to_json())

# convert the object into a dict
outline_wiki_dict = outline_wiki_instance.to_dict()
# create an instance of OutlineWiki from a dict
outline_wiki_form_dict = outline_wiki.from_dict(outline_wiki_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


