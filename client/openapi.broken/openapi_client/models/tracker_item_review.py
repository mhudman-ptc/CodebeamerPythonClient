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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.tracker_item_review_config import TrackerItemReviewConfig
from openapi_client.models.tracker_item_review_vote import TrackerItemReviewVote
from openapi_client.models.tracker_item_revision import TrackerItemRevision
from typing import Optional, Set
from typing_extensions import Self

class TrackerItemReview(BaseModel):
    """
    A tracker item review instance including its reviewers and their decisions
    """ # noqa: E501
    config: Optional[TrackerItemReviewConfig] = None
    result: Optional[StrictStr] = Field(default=None, description="Whether the review is approved or rejected")
    reviewers: Optional[List[TrackerItemReviewVote]] = Field(default=None, description="List of reviewers, and their votes")
    tracker_item: Optional[TrackerItemRevision] = Field(default=None, alias="trackerItem")
    __properties: ClassVar[List[str]] = ["config", "result", "reviewers", "trackerItem"]

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['APPROVED', 'REJECTED', 'UNDECIDED']):
            raise ValueError("must be one of enum values ('APPROVED', 'REJECTED', 'UNDECIDED')")
        return value

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
        """Create an instance of TrackerItemReview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item in self.reviewers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reviewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of tracker_item
        if self.tracker_item:
            _dict['trackerItem'] = self.tracker_item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackerItemReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": TrackerItemReviewConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "result": obj.get("result"),
            "reviewers": [TrackerItemReviewVote.from_dict(_item) for _item in obj["reviewers"]] if obj.get("reviewers") is not None else None,
            "trackerItem": TrackerItemRevision.from_dict(obj["trackerItem"]) if obj.get("trackerItem") is not None else None
        })
        return _obj

