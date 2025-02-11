# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.export_for_deployment_request import ExportForDeploymentRequest

class TestExportForDeploymentRequest(unittest.TestCase):
    """ExportForDeploymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportForDeploymentRequest:
        """Test ExportForDeploymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportForDeploymentRequest`
        """
        model = ExportForDeploymentRequest()
        if include_optional:
            return ExportForDeploymentRequest(
                export_file_name = '',
                password = '',
                project_settings = [
                    openapi_client.models.deployment_project_export_settings.DeploymentProjectExportSettings(
                        include_queries = True, 
                        include_tracker_items = True, 
                        include_trackers = True, 
                        project_id = 56, 
                        trackers = [
                            openapi_client.models.deployment_tracker_export_settings.DeploymentTrackerExportSettings(
                                items_included = True, 
                                tracker_id = 56, )
                            ], )
                    ],
                schema_name = '',
                schema_version = ''
            )
        else:
            return ExportForDeploymentRequest(
        )
        """

    def testExportForDeploymentRequest(self):
        """Test ExportForDeploymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
