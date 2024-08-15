# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.wiki_api import WikiApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWikiApi(unittest.TestCase):
    """WikiApi unit test stubs"""

    def setUp(self):
        self.api = WikiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_wiki_page_lock(self):
        """Test case for check_wiki_page_lock

        Check whether a wiki page is locked, and if it is, retrieve the details of the lock  # noqa: E501
        """
        pass

    def test_create_wiki_page(self):
        """Test case for create_wiki_page

        Create a new wiki page  # noqa: E501
        """
        pass

    def test_delete_wiki_page(self):
        """Test case for delete_wiki_page

        Delete a wiki page by its ID  # noqa: E501
        """
        pass

    def test_get_wiki_page(self):
        """Test case for get_wiki_page

        Get wiki page  # noqa: E501
        """
        pass

    def test_get_wiki_page_history(self):
        """Test case for get_wiki_page_history

        Returns the change history of the specified wiki page  # noqa: E501
        """
        pass

    def test_get_wiki_permissions(self):
        """Test case for get_wiki_permissions

        Get permissions of a wiki page  # noqa: E501
        """
        pass

    def test_lock_wiki_page(self):
        """Test case for lock_wiki_page

        Lock a wiki page  # noqa: E501
        """
        pass

    def test_render_wiki_markup(self):
        """Test case for render_wiki_markup

        Render a wiki page as HTML in a specific context  # noqa: E501
        """
        pass

    def test_render_wiki_page(self):
        """Test case for render_wiki_page

        Render a wiki page as HTML  # noqa: E501
        """
        pass

    def test_restore_wiki_page_content(self):
        """Test case for restore_wiki_page_content

        Restores the content from a previous version of a wiki page  # noqa: E501
        """
        pass

    def test_set_wiki_permissions(self):
        """Test case for set_wiki_permissions

        Set permissions of a wiki page  # noqa: E501
        """
        pass

    def test_unlock_wiki_page(self):
        """Test case for unlock_wiki_page

        Unlock a wiki page  # noqa: E501
        """
        pass

    def test_update_wiki_page(self):
        """Test case for update_wiki_page

        Update and/or move a wiki page  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
