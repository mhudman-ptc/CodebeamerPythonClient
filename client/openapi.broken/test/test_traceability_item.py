# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.traceability_item import TraceabilityItem

class TestTraceabilityItem(unittest.TestCase):
    """TraceabilityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TraceabilityItem:
        """Test TraceabilityItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TraceabilityItem`
        """
        model = TraceabilityItem()
        if include_optional:
            return TraceabilityItem(
                children = [
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
                    ],
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
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ],
                incoming_references = [
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ],
                item_revision = openapi_client.models.tracker_item_revision.TrackerItemRevision(
                    id = 56, 
                    version = 56, ),
                outgoing_association = [
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ],
                outgoing_reference = [
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ],
                outgoing_associations = [
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ],
                outgoing_references = [
                    openapi_client.models.tracker_item_revision.TrackerItemRevision(
                        id = 56, 
                        version = 56, )
                    ]
            )
        else:
            return TraceabilityItem(
        )
        """

    def testTraceabilityItem(self):
        """Test TraceabilityItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()