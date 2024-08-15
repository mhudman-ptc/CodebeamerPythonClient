# coding: utf-8

"""
    Codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TrackerItemsCommentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def comment_on_tracker_item(self, item_id, **kwargs):  # noqa: E501
        """Comment on a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comment_on_tracker_item(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.comment_on_tracker_item_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.comment_on_tracker_item_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def comment_on_tracker_item_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Comment on a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comment_on_tracker_item_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'attachments', 'comment', 'comment_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method comment_on_tracker_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `comment_on_tracker_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Comment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tracker_item_comment(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Delete comment of tracker item by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tracker_item_comment(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tracker_item_comment_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tracker_item_comment_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def delete_tracker_item_comment_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Delete comment of tracker item by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tracker_item_comment_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tracker_item_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `delete_tracker_item_comment`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `delete_tracker_item_comment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentId'] = params['comment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments/{commentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Comment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tracker_item_comments(self, item_id, **kwargs):  # noqa: E501
        """Delete comments of tracker item by item id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tracker_item_comments(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tracker_item_comments_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tracker_item_comments_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def delete_tracker_item_comments_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Delete comments of tracker item by item id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tracker_item_comments_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tracker_item_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `delete_tracker_item_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_comment_on_tracker_item(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Edit comment on a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_comment_on_tracker_item(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_comment_on_tracker_item_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_comment_on_tracker_item_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def edit_comment_on_tracker_item_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Edit comment on a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_comment_on_tracker_item_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id', 'attachments', 'comment', 'comment_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_comment_on_tracker_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `edit_comment_on_tracker_item`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `edit_comment_on_tracker_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentId'] = params['comment_id']  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments/{commentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Comment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tracker_item_comment(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Get comment of tracker item by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tracker_item_comment(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tracker_item_comment_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tracker_item_comment_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def get_tracker_item_comment_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Get comment of tracker item by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tracker_item_comment_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tracker_item_comment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `get_tracker_item_comment`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `get_tracker_item_comment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentId'] = params['comment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments/{commentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Comment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tracker_item_comments(self, item_id, **kwargs):  # noqa: E501
        """Get comments of tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tracker_item_comments(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: Id of a tracker item (required)
        :return: list[Comment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tracker_item_comments_with_http_info(item_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tracker_item_comments_with_http_info(item_id, **kwargs)  # noqa: E501
            return data

    def get_tracker_item_comments_with_http_info(self, item_id, **kwargs):  # noqa: E501
        """Get comments of tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tracker_item_comments_with_http_info(item_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: Id of a tracker item (required)
        :return: list[Comment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tracker_item_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `get_tracker_item_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Comment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reply_on_comment_of_tracker_item(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Reply on a comment of a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_on_comment_of_tracker_item(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reply_on_comment_of_tracker_item_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reply_on_comment_of_tracker_item_with_http_info(item_id, comment_id, **kwargs)  # noqa: E501
            return data

    def reply_on_comment_of_tracker_item_with_http_info(self, item_id, comment_id, **kwargs):  # noqa: E501
        """Reply on a comment of a tracker item  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reply_on_comment_of_tracker_item_with_http_info(item_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int item_id: (required)
        :param int comment_id: (required)
        :param str attachments:
        :param str comment:
        :param str comment_format:
        :return: Comment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'comment_id', 'attachments', 'comment', 'comment_format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reply_on_comment_of_tracker_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `reply_on_comment_of_tracker_item`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `reply_on_comment_of_tracker_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentId'] = params['comment_id']  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v3/items/{itemId}/comments/{commentId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Comment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
