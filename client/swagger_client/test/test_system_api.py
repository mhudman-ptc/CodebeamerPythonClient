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
from swagger_client.api.system_api import SystemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self):
        self.api = SystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_system_status(self):
        """Test case for get_system_status

        Get system maintenance status  # noqa: E501
        """
        pass

    def test_set_system_status(self):
        """Test case for set_system_status

        Set system maintenance status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()