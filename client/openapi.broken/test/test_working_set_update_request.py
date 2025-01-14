# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.working_set_update_request import WorkingSetUpdateRequest

class TestWorkingSetUpdateRequest(unittest.TestCase):
    """WorkingSetUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkingSetUpdateRequest:
        """Test WorkingSetUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkingSetUpdateRequest`
        """
        model = WorkingSetUpdateRequest()
        if include_optional:
            return WorkingSetUpdateRequest(
                project_baseline_id = 56,
                source = openapi_client.models.working_set_reference.WorkingSetReference(),
                target = openapi_client.models.working_set_reference.WorkingSetReference(),
                trackers = [
                    openapi_client.models.working_set_tracker_update_request.WorkingSetTrackerUpdateRequest(
                        baseline_id = 56, 
                        cbql = '', 
                        tracker = openapi_client.models.tracker_reference.TrackerReference(), )
                    ]
            )
        else:
            return WorkingSetUpdateRequest(
                source = openapi_client.models.working_set_reference.WorkingSetReference(),
                target = openapi_client.models.working_set_reference.WorkingSetReference(),
        )
        """

    def testWorkingSetUpdateRequest(self):
        """Test WorkingSetUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
