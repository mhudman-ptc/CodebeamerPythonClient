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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.role_reference import RoleReference
from openapi_client.models.tracker_permission_reference import TrackerPermissionReference
from openapi_client.models.tracker_reference import TrackerReference
from typing import Optional, Set
from typing_extensions import Self

class WorkingSetPermissionRequest(BaseModel):
    """
    Request model trackers, roles and permissions.
    """ # noqa: E501
    permissions: Optional[List[TrackerPermissionReference]] = Field(default=None, description="Permission references.")
    roles: Optional[List[RoleReference]] = Field(default=None, description="Role references.")
    trackers: Optional[List[TrackerReference]] = Field(default=None, description="Tracker references.")
    __properties: ClassVar[List[str]] = ["permissions", "roles", "trackers"]

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
        """Create an instance of WorkingSetPermissionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trackers (list)
        _items = []
        if self.trackers:
            for _item in self.trackers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trackers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkingSetPermissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissions": [TrackerPermissionReference.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "roles": [RoleReference.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "trackers": [TrackerReference.from_dict(_item) for _item in obj["trackers"]] if obj.get("trackers") is not None else None
        })
        return _obj

