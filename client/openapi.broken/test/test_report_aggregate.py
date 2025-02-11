# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_aggregate import ReportAggregate

class TestReportAggregate(unittest.TestCase):
    """ReportAggregate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportAggregate:
        """Test ReportAggregate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportAggregate`
        """
        model = ReportAggregate()
        if include_optional:
            return ReportAggregate(
                average = 11.32,
                column_ref = '11-1',
                maximum = 21.32,
                minimum = 1.32,
                sum = 22.64
            )
        else:
            return ReportAggregate(
        )
        """

    def testReportAggregate(self):
        """Test ReportAggregate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
