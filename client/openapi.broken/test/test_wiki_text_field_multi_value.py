# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wiki_text_field_multi_value import WikiTextFieldMultiValue

class TestWikiTextFieldMultiValue(unittest.TestCase):
    """WikiTextFieldMultiValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WikiTextFieldMultiValue:
        """Test WikiTextFieldMultiValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WikiTextFieldMultiValue`
        """
        model = WikiTextFieldMultiValue()
        if include_optional:
            return WikiTextFieldMultiValue(
                plain_text_value = '',
                value = ''
            )
        else:
            return WikiTextFieldMultiValue(
        )
        """

    def testWikiTextFieldMultiValue(self):
        """Test WikiTextFieldMultiValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
