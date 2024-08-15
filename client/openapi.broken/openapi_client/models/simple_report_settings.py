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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.report_permission import ReportPermission
from openapi_client.models.resizable_report_column_settings import ResizableReportColumnSettings
from typing import Optional, Set
from typing_extensions import Self

class SimpleReportSettings(BaseModel):
    """
    Settings for a simple report.
    """ # noqa: E501
    added_permissions: Optional[List[ReportPermission]] = Field(default=None, description="Access permissions for the report.", alias="addedPermissions")
    cb_ql: StrictStr = Field(description="CbQL query string of the report.", alias="cbQl")
    columns: List[ResizableReportColumnSettings] = Field(description="Column definitions.")
    description: StrictStr = Field(description="Description of the report.")
    name: StrictStr = Field(description="Name of the report.")
    report_id: Optional[StrictInt] = Field(default=None, description="Id of a report", alias="reportId")
    show_all_children: Optional[StrictBool] = Field(default=None, description="Indicator to ability to collapse/expand all child items.", alias="showAllChildren")
    show_ancestors: Optional[StrictBool] = Field(default=None, description="Indicator to show the ancestors of a result item.", alias="showAncestors")
    show_descendants: Optional[StrictBool] = Field(default=None, description="Indicator to show the descendants of a result item.", alias="showDescendants")
    __properties: ClassVar[List[str]] = ["addedPermissions", "cbQl", "columns", "description", "name", "reportId", "showAllChildren", "showAncestors", "showDescendants"]

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
        """Create an instance of SimpleReportSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in added_permissions (list)
        _items = []
        if self.added_permissions:
            for _item in self.added_permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addedPermissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimpleReportSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addedPermissions": [ReportPermission.from_dict(_item) for _item in obj["addedPermissions"]] if obj.get("addedPermissions") is not None else None,
            "cbQl": obj.get("cbQl"),
            "columns": [ResizableReportColumnSettings.from_dict(_item) for _item in obj["columns"]] if obj.get("columns") is not None else None,
            "description": obj.get("description"),
            "name": obj.get("name"),
            "reportId": obj.get("reportId"),
            "showAllChildren": obj.get("showAllChildren"),
            "showAncestors": obj.get("showAncestors"),
            "showDescendants": obj.get("showDescendants")
        })
        return _obj


