# WikiRenderRequest

Request model to render a wiki page in a specific context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_id** | **int** | Id of the entity used as rendering context | [optional] 
**context_version** | **int** | Version of the entity used as rendering context | [optional] 
**markup** | **str** | Wiki markup to render as HTML | 
**rendering_context_type** | **str** | Type of the entity used as rendering context | [optional] 

## Example

```python
from openapi_client.models.wiki_render_request import WikiRenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WikiRenderRequest from a JSON string
wiki_render_request_instance = WikiRenderRequest.from_json(json)
# print the JSON string representation of the object
print(WikiRenderRequest.to_json())

# convert the object into a dict
wiki_render_request_dict = wiki_render_request_instance.to_dict()
# create an instance of WikiRenderRequest from a dict
wiki_render_request_form_dict = wiki_render_request.from_dict(wiki_render_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


