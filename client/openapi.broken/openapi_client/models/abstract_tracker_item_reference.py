# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.tracker_item_revision import TrackerItemRevision
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.downstream_tracker_item_reference import DownstreamTrackerItemReference
    from openapi_client.models.incoming_tracker_item_association import IncomingTrackerItemAssociation
    from openapi_client.models.outgoing_tracker_item_association import OutgoingTrackerItemAssociation
    from openapi_client.models.upstream_tracker_item_reference import UpstreamTrackerItemReference

class AbstractTrackerItemReference(BaseModel):
    """
    Reference to an item
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Id of the reference/association")
    item_revision: Optional[TrackerItemRevision] = Field(default=None, alias="itemRevision")
    type: Optional[StrictStr] = Field(default=None, description="Type of the relation")
    __properties: ClassVar[List[str]] = ["id", "itemRevision", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'DownstreamTrackerItemReference': 'DownstreamTrackerItemReference','IncomingTrackerItemAssociation': 'IncomingTrackerItemAssociation','OutgoingTrackerItemAssociation': 'OutgoingTrackerItemAssociation','UpstreamTrackerItemReference': 'UpstreamTrackerItemReference'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[DownstreamTrackerItemReference, IncomingTrackerItemAssociation, OutgoingTrackerItemAssociation, UpstreamTrackerItemReference]]:
        """Create an instance of AbstractTrackerItemReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of item_revision
        if self.item_revision:
            _dict['itemRevision'] = self.item_revision.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[DownstreamTrackerItemReference, IncomingTrackerItemAssociation, OutgoingTrackerItemAssociation, UpstreamTrackerItemReference]]:
        """Create an instance of AbstractTrackerItemReference from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'DownstreamTrackerItemReference':
            return import_module("openapi_client.models.downstream_tracker_item_reference").DownstreamTrackerItemReference.from_dict(obj)
        if object_type ==  'IncomingTrackerItemAssociation':
            return import_module("openapi_client.models.incoming_tracker_item_association").IncomingTrackerItemAssociation.from_dict(obj)
        if object_type ==  'OutgoingTrackerItemAssociation':
            return import_module("openapi_client.models.outgoing_tracker_item_association").OutgoingTrackerItemAssociation.from_dict(obj)
        if object_type ==  'UpstreamTrackerItemReference':
            return import_module("openapi_client.models.upstream_tracker_item_reference").UpstreamTrackerItemReference.from_dict(obj)

        raise ValueError("AbstractTrackerItemReference failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

