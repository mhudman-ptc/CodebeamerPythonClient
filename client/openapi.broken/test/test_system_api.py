# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.system_api import SystemApi


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_status(self) -> None:
        """Test case for get_system_status

        Get system maintenance status
        """
        pass

    def test_set_system_status(self) -> None:
        """Test case for set_system_status

        Set system maintenance status
        """
        pass


if __name__ == '__main__':
    unittest.main()
