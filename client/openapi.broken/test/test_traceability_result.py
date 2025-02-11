# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.traceability_result import TraceabilityResult

class TestTraceabilityResult(unittest.TestCase):
    """TraceabilityResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TraceabilityResult:
        """Test TraceabilityResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TraceabilityResult`
        """
        model = TraceabilityResult()
        if include_optional:
            return TraceabilityResult(
                limit_warnings = '',
                traceability_items = [
                    openapi_client.models.traceability_item.TraceabilityItem(
                        children = [
                            openapi_client.models.traceability_item.TraceabilityItem(
                                incoming_association = [
                                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                                        id = 56, 
                                        version = 56, )
                                    ], 
                                incoming_reference = [
                                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                                        id = 56, 
                                        version = 56, )
                                    ], 
                                incoming_associations = [
                                    
                                    ], 
                                incoming_references = [
                                    
                                    ], 
                                item_revision = , 
                                outgoing_association = [
                                    
                                    ], 
                                outgoing_reference = [
                                    
                                    ], 
                                outgoing_associations = [
                                    
                                    ], 
                                outgoing_references = [
                                    
                                    ], )
                            ], 
                        incoming_association = [
                            
                            ], 
                        incoming_reference = [
                            
                            ], 
                        incoming_associations = [
                            
                            ], 
                        incoming_references = [
                            
                            ], 
                        item_revision = , 
                        outgoing_association = [
                            
                            ], 
                        outgoing_reference = [
                            
                            ], 
                        outgoing_associations = [
                            
                            ], 
                        outgoing_references = [
                            
                            ], )
                    ]
            )
        else:
            return TraceabilityResult(
        )
        """

    def testTraceabilityResult(self):
        """Test TraceabilityResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
