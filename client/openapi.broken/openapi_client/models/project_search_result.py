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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class ProjectSearchResult(BaseModel):
    """
    One page of artifact revisions.
    """ # noqa: E501
    page: Optional[StrictInt] = Field(default=None, description="Index of the page")
    page_size: Optional[StrictInt] = Field(default=None, description="Size of the found page", alias="pageSize")
    projects: Optional[List[Project]] = Field(default=None, description="Found projects")
    total: Optional[StrictInt] = Field(default=None, description="Number of matched tracker items by the search criteria")
    __properties: ClassVar[List[str]] = ["page", "pageSize", "projects", "total"]

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
        """Create an instance of ProjectSearchResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in projects (list)
        _items = []
        if self.projects:
            for _item in self.projects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['projects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectSearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page": obj.get("page"),
            "pageSize": obj.get("pageSize"),
            "projects": [Project.from_dict(_item) for _item in obj["projects"]] if obj.get("projects") is not None else None,
            "total": obj.get("total")
        })
        return _obj


