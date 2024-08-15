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
from swagger_client.api.group_api import GroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_group(self):
        """Test case for get_group

        Get user group  # noqa: E501
        """
        pass

    def test_get_group_members(self):
        """Test case for get_group_members

        Get all members of a user group  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Get user groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
