# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.not_supported_field_value import NotSupportedFieldValue

class TestNotSupportedFieldValue(unittest.TestCase):
    """NotSupportedFieldValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotSupportedFieldValue:
        """Test NotSupportedFieldValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotSupportedFieldValue`
        """
        model = NotSupportedFieldValue()
        if include_optional:
            return NotSupportedFieldValue(
            )
        else:
            return NotSupportedFieldValue(
        )
        """

    def testNotSupportedFieldValue(self):
        """Test NotSupportedFieldValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
