# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WikisCommentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def comment_on_wiki(self, wiki_id, **kwargs):  # noqa: E501
        """Comment on a wiki page  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comment_on_wiki(wiki_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wiki_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: list[AttachmentReference]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.comment_on_wiki_with_http_info(wiki_id, **kwargs)  # noqa: E501
        else:
            (data) = self.comment_on_wiki_with_http_info(wiki_id, **kwargs)  # noqa: E501
            return data

    def comment_on_wiki_with_http_info(self, wiki_id, **kwargs):  # noqa: E501
        """Comment on a wiki page  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comment_on_wiki_with_http_info(wiki_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wiki_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: list[AttachmentReference]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wiki_id', 'attachments', 'comment', 'comment_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method comment_on_wiki" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wiki_id' is set
        if ('wiki_id' not in params or
                params['wiki_id'] is None):
            raise ValueError("Missing the required parameter `wiki_id` when calling `comment_on_wiki`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wiki_id' in params:
            path_params['wikiId'] = params['wiki_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'attachments' in params:
            local_var_files['attachments'] = params['attachments']  # noqa: E501
        if 'comment' in params:
            form_params.append(('comment', params['comment']))  # noqa: E501
        if 'comment_format' in params:
            form_params.append(('commentFormat', params['comment_format']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/wikipages/{wikiId}/comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AttachmentReference]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attachment_by_name(self, wiki_id, file_name, **kwargs):  # noqa: E501
        """Get attachment of wiki page by file name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_by_name(wiki_id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wiki_id: (required)
        :param str file_name: (required)
        :return: Attachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_attachment_by_name_with_http_info(wiki_id, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_attachment_by_name_with_http_info(wiki_id, file_name, **kwargs)  # noqa: E501
            return data

    def get_attachment_by_name_with_http_info(self, wiki_id, file_name, **kwargs):  # noqa: E501
        """Get attachment of wiki page by file name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_by_name_with_http_info(wiki_id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int wiki_id: (required)
        :param str file_name: (required)
        :return: Attachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wiki_id', 'file_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attachment_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'wiki_id' is set
        if ('wiki_id' not in params or
                params['wiki_id'] is None):
            raise ValueError("Missing the required parameter `wiki_id` when calling `get_attachment_by_name`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `get_attachment_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wiki_id' in params:
            path_params['wikiId'] = params['wiki_id']  # noqa: E501

        query_params = []
        if 'file_name' in params:
            query_params.append(('fileName', params['file_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/wikipages/{wikiId}/attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Attachment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
