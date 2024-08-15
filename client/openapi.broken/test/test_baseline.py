# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.baseline import Baseline

class TestBaseline(unittest.TestCase):
    """Baseline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Baseline:
        """Test Baseline
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Baseline`
        """
        model = Baseline()
        if include_optional:
            return Baseline(
                description = '',
                description_format = 'PlainText',
                id = 0,
                name = '',
                project = openapi_client.models.project_reference.ProjectReference(),
                tracker = openapi_client.models.tracker_reference.TrackerReference()
            )
        else:
            return Baseline(
        )
        """

    def testBaseline(self):
        """Test Baseline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
