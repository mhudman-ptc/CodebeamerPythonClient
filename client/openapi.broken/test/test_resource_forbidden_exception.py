# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_forbidden_exception import ResourceForbiddenException

class TestResourceForbiddenException(unittest.TestCase):
    """ResourceForbiddenException unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceForbiddenException:
        """Test ResourceForbiddenException
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceForbiddenException`
        """
        model = ResourceForbiddenException()
        if include_optional:
            return ResourceForbiddenException(
                message = '',
                resource_uri = ''
            )
        else:
            return ResourceForbiddenException(
        )
        """

    def testResourceForbiddenException(self):
        """Test ResourceForbiddenException"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
