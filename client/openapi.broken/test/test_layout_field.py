# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.layout_field import LayoutField

class TestLayoutField(unittest.TestCase):
    """LayoutField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LayoutField:
        """Test LayoutField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LayoutField`
        """
        model = LayoutField()
        if include_optional:
            return LayoutField(
                field = '',
                field_id = 56,
                width = ''
            )
        else:
            return LayoutField(
        )
        """

    def testLayoutField(self):
        """Test LayoutField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()