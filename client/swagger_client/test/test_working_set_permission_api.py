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
from swagger_client.api.working_set_permission_api import WorkingSetPermissionApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkingSetPermissionApi(unittest.TestCase):
    """WorkingSetPermissionApi unit test stubs"""

    def setUp(self):
        self.api = WorkingSetPermissionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_update_working_set_permission(self):
        """Test case for update_working_set_permission

        Set the trackers permissions for specific roles in the given workingset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
