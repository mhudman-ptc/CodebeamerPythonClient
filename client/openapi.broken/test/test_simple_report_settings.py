# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.simple_report_settings import SimpleReportSettings

class TestSimpleReportSettings(unittest.TestCase):
    """SimpleReportSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleReportSettings:
        """Test SimpleReportSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleReportSettings`
        """
        model = SimpleReportSettings()
        if include_optional:
            return SimpleReportSettings(
                added_permissions = [
                    openapi_client.models.report_permission.ReportPermission(
                        access = 'READ', 
                        project = openapi_client.models.project_reference.ProjectReference(), 
                        role = openapi_client.models.role_reference.RoleReference(), )
                    ],
                cb_ql = 'priority='Normal'',
                columns = [
                    openapi_client.models.resizable_report_column_settings.ResizableReportColumnSettings(
                        column_index = 0, 
                        column_width_percentage = 43.2, 
                        field = openapi_client.models.field_reference.FieldReference(), )
                    ],
                description = 'Normal priority items.',
                name = 'My first query',
                report_id = 1,
                show_all_children = False,
                show_ancestors = True,
                show_descendants = False
            )
        else:
            return SimpleReportSettings(
                cb_ql = 'priority='Normal'',
                columns = [
                    openapi_client.models.resizable_report_column_settings.ResizableReportColumnSettings(
                        column_index = 0, 
                        column_width_percentage = 43.2, 
                        field = openapi_client.models.field_reference.FieldReference(), )
                    ],
                description = 'Normal priority items.',
                name = 'My first query',
        )
        """

    def testSimpleReportSettings(self):
        """Test SimpleReportSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
