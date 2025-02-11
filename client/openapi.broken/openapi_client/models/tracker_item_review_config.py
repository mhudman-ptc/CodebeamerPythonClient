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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TrackerItemReviewConfig(BaseModel):
    """
    The configuration from which the review was created
    """ # noqa: E501
    required_approvals: Optional[StrictInt] = Field(default=None, description="Number of approvals after which the review is considered approved", alias="requiredApprovals")
    required_rejections: Optional[StrictInt] = Field(default=None, description="Number of rejections after which the review is considered rejected", alias="requiredRejections")
    required_signature: Optional[StrictStr] = Field(default=None, description="Whether the user has to provide its credentials to vote", alias="requiredSignature")
    role_required: Optional[StrictBool] = Field(default=None, description="Whether the reviewers have to chose in which of their roles do they want to vote", alias="roleRequired")
    __properties: ClassVar[List[str]] = ["requiredApprovals", "requiredRejections", "requiredSignature", "roleRequired"]

    @field_validator('required_signature')
    def required_signature_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'PASSWORD', 'USERNAME_AND_PASSWORD']):
            raise ValueError("must be one of enum values ('NONE', 'PASSWORD', 'USERNAME_AND_PASSWORD')")
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
        """Create an instance of TrackerItemReviewConfig from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackerItemReviewConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requiredApprovals": obj.get("requiredApprovals"),
            "requiredRejections": obj.get("requiredRejections"),
            "requiredSignature": obj.get("requiredSignature"),
            "roleRequired": obj.get("roleRequired")
        })
        return _obj


