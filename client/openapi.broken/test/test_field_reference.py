# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.field_reference import FieldReference

class TestFieldReference(unittest.TestCase):
    """FieldReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FieldReference:
        """Test FieldReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FieldReference`
        """
        model = FieldReference()
        if include_optional:
            return FieldReference(
                shared_field_names = [
                    ''
                    ],
                tracker_id = 1000
            )
        else:
            return FieldReference(
        )
        """

    def testFieldReference(self):
        """Test FieldReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
