# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.workflow_transition import WorkflowTransition

class TestWorkflowTransition(unittest.TestCase):
    """WorkflowTransition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowTransition:
        """Test WorkflowTransition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowTransition`
        """
        model = WorkflowTransition()
        if include_optional:
            return WorkflowTransition(
                description = '',
                description_format = 'PlainText',
                from_status = openapi_client.models.choice_option_reference.ChoiceOptionReference(),
                hidden = True,
                id = 0,
                name = '',
                permissions = [
                    openapi_client.models.access_permission.AccessPermission(
                        access_level = 'NONE', 
                        field = openapi_client.models.field_reference.FieldReference(), 
                        project = openapi_client.models.project_reference.ProjectReference(), 
                        role = openapi_client.models.role_reference.RoleReference(), )
                    ],
                to_status = openapi_client.models.choice_option_reference.ChoiceOptionReference()
            )
        else:
            return WorkflowTransition(
                to_status = openapi_client.models.choice_option_reference.ChoiceOptionReference(),
        )
        """

    def testWorkflowTransition(self):
        """Test WorkflowTransition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
