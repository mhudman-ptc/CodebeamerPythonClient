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
from swagger_client.api.association_api import AssociationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAssociationApi(unittest.TestCase):
    """AssociationApi unit test stubs"""

    def setUp(self):
        self.api = AssociationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_association(self):
        """Test case for create_association

        Create a new association  # noqa: E501
        """
        pass

    def test_delete_association(self):
        """Test case for delete_association

        Delete association  # noqa: E501
        """
        pass

    def test_get_association(self):
        """Test case for get_association

        Get an association by id  # noqa: E501
        """
        pass

    def test_get_association_history(self):
        """Test case for get_association_history

        Returns the change history of the specified association  # noqa: E501
        """
        pass

    def test_get_association_type(self):
        """Test case for get_association_type

        Get association type by id  # noqa: E501
        """
        pass

    def test_get_available_association_types(self):
        """Test case for get_available_association_types

        Get available association types  # noqa: E501
        """
        pass

    def test_update_association(self):
        """Test case for update_association

        Update association settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
