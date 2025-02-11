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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.downstream_tracker_item_reference import DownstreamTrackerItemReference
from openapi_client.models.incoming_tracker_item_association import IncomingTrackerItemAssociation
from openapi_client.models.outgoing_tracker_item_association import OutgoingTrackerItemAssociation
from openapi_client.models.tracker_item_revision import TrackerItemRevision
from openapi_client.models.upstream_tracker_item_reference import UpstreamTrackerItemReference
from typing import Optional, Set
from typing_extensions import Self

class TrackerItemRelationsResult(BaseModel):
    """
    References to a tracker item
    """ # noqa: E501
    downstream_references: Optional[List[DownstreamTrackerItemReference]] = Field(default=None, description="References and associations to the item", alias="downstreamReferences")
    incoming_associations: Optional[List[IncomingTrackerItemAssociation]] = Field(default=None, description="References and associations to the item", alias="incomingAssociations")
    is_last_page: Optional[StrictBool] = Field(default=None, description="Set to true if it is the last page", alias="isLastPage")
    item_count: Optional[StrictInt] = Field(default=None, description="Number of items on page", alias="itemCount")
    item_id: Optional[TrackerItemRevision] = Field(default=None, alias="itemId")
    outgoing_associations: Optional[List[OutgoingTrackerItemAssociation]] = Field(default=None, description="References and associations to the item", alias="outgoingAssociations")
    page: Optional[StrictInt] = Field(default=None, description="Page no.")
    page_size: Optional[StrictInt] = Field(default=None, description="Page size", alias="pageSize")
    upstream_references: Optional[List[UpstreamTrackerItemReference]] = Field(default=None, description="References and associations to the item", alias="upstreamReferences")
    __properties: ClassVar[List[str]] = ["downstreamReferences", "incomingAssociations", "isLastPage", "itemCount", "itemId", "outgoingAssociations", "page", "pageSize", "upstreamReferences"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TrackerItemRelationsResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in downstream_references (list)
        _items = []
        if self.downstream_references:
            for _item in self.downstream_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['downstreamReferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in incoming_associations (list)
        _items = []
        if self.incoming_associations:
            for _item in self.incoming_associations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['incomingAssociations'] = _items
        # override the default output from pydantic by calling `to_dict()` of item_id
        if self.item_id:
            _dict['itemId'] = self.item_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in outgoing_associations (list)
        _items = []
        if self.outgoing_associations:
            for _item in self.outgoing_associations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outgoingAssociations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in upstream_references (list)
        _items = []
        if self.upstream_references:
            for _item in self.upstream_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['upstreamReferences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackerItemRelationsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "downstreamReferences": [DownstreamTrackerItemReference.from_dict(_item) for _item in obj["downstreamReferences"]] if obj.get("downstreamReferences") is not None else None,
            "incomingAssociations": [IncomingTrackerItemAssociation.from_dict(_item) for _item in obj["incomingAssociations"]] if obj.get("incomingAssociations") is not None else None,
            "isLastPage": obj.get("isLastPage"),
            "itemCount": obj.get("itemCount"),
            "itemId": TrackerItemRevision.from_dict(obj["itemId"]) if obj.get("itemId") is not None else None,
            "outgoingAssociations": [OutgoingTrackerItemAssociation.from_dict(_item) for _item in obj["outgoingAssociations"]] if obj.get("outgoingAssociations") is not None else None,
            "page": obj.get("page"),
            "pageSize": obj.get("pageSize"),
            "upstreamReferences": [UpstreamTrackerItemReference.from_dict(_item) for _item in obj["upstreamReferences"]] if obj.get("upstreamReferences") is not None else None
        })
        return _obj


