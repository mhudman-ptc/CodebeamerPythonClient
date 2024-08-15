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
from typing import Optional, Set
from typing_extensions import Self

class ExportToWordRequest(BaseModel):
    """
    Request model for exporting items to Word
    """ # noqa: E501
    current_item_and_its_children: Optional[StrictBool] = Field(default=None, description="The children of the current item should be included also or not", alias="currentItemAndItsChildren")
    current_item_id: StrictInt = Field(description="The id of the item", alias="currentItemId")
    export_target_tracker_folder_id: Optional[StrictInt] = Field(default=None, description="The Document tracker Folder where the exported file will be stored", alias="exportTargetTrackerFolderId")
    export_target_tracker_id: StrictInt = Field(description="The id of the Document type Tracker", alias="exportTargetTrackerId")
    new_version: Optional[StrictBool] = Field(default=None, description="If true, new version of the file will be created (timestamp added), otherwise previous file will be overwritten", alias="newVersion")
    report_id: Optional[StrictInt] = Field(default=None, description="If specified, the report result will be in the Word document instead of the current item (and its children, if this set)", alias="reportId")
    word_filename: StrictStr = Field(description="The name of the generated Word document", alias="wordFilename")
    word_template_name: Optional[StrictStr] = Field(default=None, description="Which Word template should be used for the Word document generation", alias="wordTemplateName")
    __properties: ClassVar[List[str]] = ["currentItemAndItsChildren", "currentItemId", "exportTargetTrackerFolderId", "exportTargetTrackerId", "newVersion", "reportId", "wordFilename", "wordTemplateName"]

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
        """Create an instance of ExportToWordRequest from a JSON string"""
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
        """Create an instance of ExportToWordRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currentItemAndItsChildren": obj.get("currentItemAndItsChildren"),
            "currentItemId": obj.get("currentItemId"),
            "exportTargetTrackerFolderId": obj.get("exportTargetTrackerFolderId"),
            "exportTargetTrackerId": obj.get("exportTargetTrackerId"),
            "newVersion": obj.get("newVersion"),
            "reportId": obj.get("reportId"),
            "wordFilename": obj.get("wordFilename"),
            "wordTemplateName": obj.get("wordTemplateName")
        })
        return _obj

