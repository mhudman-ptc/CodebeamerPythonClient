# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cross_project_dependency import CrossProjectDependency

class TestCrossProjectDependency(unittest.TestCase):
    """CrossProjectDependency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CrossProjectDependency:
        """Test CrossProjectDependency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossProjectDependency`
        """
        model = CrossProjectDependency()
        if include_optional:
            return CrossProjectDependency(
                referred_from = [
                    openapi_client.models.dependency_attribute.DependencyAttribute(
                        lookup_direction = 'Forward', 
                        path = [
                            openapi_client.models.dependency_entity_reference.DependencyEntityReference()
                            ], )
                    ],
                source_project = openapi_client.models.project_reference.ProjectReference(),
                target_project = openapi_client.models.project_reference.ProjectReference()
            )
        else:
            return CrossProjectDependency(
        )
        """

    def testCrossProjectDependency(self):
        """Test CrossProjectDependency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
