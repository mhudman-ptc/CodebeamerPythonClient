# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.tracker_field_dependency import TrackerFieldDependency

class TestTrackerFieldDependency(unittest.TestCase):
    """TrackerFieldDependency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerFieldDependency:
        """Test TrackerFieldDependency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerFieldDependency`
        """
        model = TrackerFieldDependency()
        if include_optional:
            return TrackerFieldDependency(
                dependent_field_id = 56,
                value_combinations = {
                    'key' : ''
                    }
            )
        else:
            return TrackerFieldDependency(
        )
        """

    def testTrackerFieldDependency(self):
        """Test TrackerFieldDependency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
