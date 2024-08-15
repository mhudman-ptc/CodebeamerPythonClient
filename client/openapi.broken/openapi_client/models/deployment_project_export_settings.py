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
from openapi_client.models.deployment_tracker_export_settings import DeploymentTrackerExportSettings
from typing import Optional, Set
from typing_extensions import Self

class DeploymentProjectExportSettings(BaseModel):
    """
    Project export settings for deployment
    """ # noqa: E501
    include_queries: Optional[StrictBool] = Field(default=None, description="Flag if queries are included.", alias="includeQueries")
    include_tracker_items: Optional[StrictBool] = Field(default=None, description="Flag if tracker items are included.", alias="includeTrackerItems")
    include_trackers: Optional[StrictBool] = Field(default=None, description="Flag if trackers are included.", alias="includeTrackers")
    project_id: StrictInt = Field(description="Project id", alias="projectId")
    trackers: Optional[List[DeploymentTrackerExportSettings]] = Field(default=None, description="Tracker export settings")
    __properties: ClassVar[List[str]] = ["includeQueries", "includeTrackerItems", "includeTrackers", "projectId", "trackers"]

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
        """Create an instance of DeploymentProjectExportSettings from a JSON string"""
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
        """Create an instance of DeploymentProjectExportSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeQueries": obj.get("includeQueries"),
            "includeTrackerItems": obj.get("includeTrackerItems"),
            "includeTrackers": obj.get("includeTrackers"),
            "projectId": obj.get("projectId"),
            "trackers": [DeploymentTrackerExportSettings.from_dict(_item) for _item in obj["trackers"]] if obj.get("trackers") is not None else None
        })
        return _obj


