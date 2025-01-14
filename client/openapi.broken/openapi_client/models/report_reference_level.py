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
from openapi_client.models.report_column import ReportColumn
from typing import Optional, Set
from typing_extensions import Self

class ReportReferenceLevel(BaseModel):
    """
    Reference results for an item.
    """ # noqa: E501
    columns: Optional[List[ReportColumn]] = Field(default=None, description="Columns to show on this reference level.")
    downstream_reference_rows: Optional[List[ReportReferencedRow]] = Field(default=None, description="Downstream reference results.", alias="downstreamReferenceRows")
    reference_level: Optional[StrictInt] = Field(default=None, description="Reference level.", alias="referenceLevel")
    upstream_reference_rows: Optional[List[ReportReferencedRow]] = Field(default=None, description="Upstream reference results.", alias="upstreamReferenceRows")
    __properties: ClassVar[List[str]] = ["columns", "downstreamReferenceRows", "referenceLevel", "upstreamReferenceRows"]

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
        """Create an instance of ReportReferenceLevel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in downstream_reference_rows (list)
        _items = []
        if self.downstream_reference_rows:
            for _item in self.downstream_reference_rows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['downstreamReferenceRows'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in upstream_reference_rows (list)
        _items = []
        if self.upstream_reference_rows:
            for _item in self.upstream_reference_rows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['upstreamReferenceRows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportReferenceLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "columns": [ReportColumn.from_dict(_item) for _item in obj["columns"]] if obj.get("columns") is not None else None,
            "downstreamReferenceRows": [ReportReferencedRow.from_dict(_item) for _item in obj["downstreamReferenceRows"]] if obj.get("downstreamReferenceRows") is not None else None,
            "referenceLevel": obj.get("referenceLevel"),
            "upstreamReferenceRows": [ReportReferencedRow.from_dict(_item) for _item in obj["upstreamReferenceRows"]] if obj.get("upstreamReferenceRows") is not None else None
        })
        return _obj

from openapi_client.models.report_referenced_row import ReportReferencedRow
# TODO: Rewrite to not use raise_errors
ReportReferenceLevel.model_rebuild(raise_errors=False)

