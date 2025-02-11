# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_filtering_request import UserFilteringRequest

class TestUserFilteringRequest(unittest.TestCase):
    """UserFilteringRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserFilteringRequest:
        """Test UserFilteringRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserFilteringRequest`
        """
        model = UserFilteringRequest()
        if include_optional:
            return UserFilteringRequest(
                email = 'john.doe@codebeamer.com',
                first_name = 'John',
                last_name = 'Doe',
                name = 'John Doe',
                project_id = 56,
                user_status = 'ACTIVATED'
            )
        else:
            return UserFilteringRequest(
        )
        """

    def testUserFilteringRequest(self):
        """Test UserFilteringRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
