# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.report_reference_level_settings import ReportReferenceLevelSettings

class TestReportReferenceLevelSettings(unittest.TestCase):
    """ReportReferenceLevelSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportReferenceLevelSettings:
        """Test ReportReferenceLevelSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportReferenceLevelSettings`
        """
        model = ReportReferenceLevelSettings()
        if include_optional:
            return ReportReferenceLevelSettings(
                columns = [
                    openapi_client.models.report_column_settings.ReportColumnSettings(
                        column_index = 0, 
                        field = openapi_client.models.field_reference.FieldReference(), )
                    ],
                downstream_reference = False,
                level = 1,
                reference_tracker_types = [
                    openapi_client.models.tracker_type_reference.TrackerTypeReference()
                    ],
                reference_trackers = [
                    openapi_client.models.tracker_reference.TrackerReference()
                    ],
                upstream_reference = True
            )
        else:
            return ReportReferenceLevelSettings(
                columns = [
                    openapi_client.models.report_column_settings.ReportColumnSettings(
                        column_index = 0, 
                        field = openapi_client.models.field_reference.FieldReference(), )
                    ],
                downstream_reference = False,
                level = 1,
                upstream_reference = True,
        )
        """

    def testReportReferenceLevelSettings(self):
        """Test ReportReferenceLevelSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
