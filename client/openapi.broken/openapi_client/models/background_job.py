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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.abstract_background_job_status_info import AbstractBackgroundJobStatusInfo
from openapi_client.models.background_job_step import BackgroundJobStep
from openapi_client.models.user_reference import UserReference
from typing import Optional, Set
from typing_extensions import Self

class BackgroundJob(BaseModel):
    """
    Information about a background job
    """ # noqa: E501
    background_job_status: Optional[StrictStr] = Field(default=None, description="Status of a background job", alias="backgroundJobStatus")
    background_job_type: Optional[StrictStr] = Field(default=None, description="Type of a background job", alias="backgroundJobType")
    created_at: Optional[datetime] = Field(default=None, description="Creation time of job", alias="createdAt")
    description: Optional[StrictStr] = Field(default=None, description="Description of job")
    finished_at: Optional[datetime] = Field(default=None, description="Completion time of job", alias="finishedAt")
    id: Optional[StrictInt] = Field(default=None, description="ID of job")
    status_info: Optional[AbstractBackgroundJobStatusInfo] = Field(default=None, alias="statusInfo")
    steps: Optional[List[BackgroundJobStep]] = Field(default=None, description="Sub-steps of a job")
    submitted_by: Optional[UserReference] = Field(default=None, alias="submittedBy")
    __properties: ClassVar[List[str]] = ["backgroundJobStatus", "backgroundJobType", "createdAt", "description", "finishedAt", "id", "statusInfo", "steps", "submittedBy"]

    @field_validator('background_job_status')
    def background_job_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DRAFT', 'NEW', 'IN_PROGRESS', 'FINISHED']):
            raise ValueError("must be one of enum values ('DRAFT', 'NEW', 'IN_PROGRESS', 'FINISHED')")
        return value

    @field_validator('background_job_type')
    def background_job_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RUN_IN_EXCEL', 'MASS_TEST_SET_RUN_CREATION', 'DEPENDENCY_FINDER', 'ITEM_EXCEL_IMPORT', 'DEPLOYMENT_EXPORT', 'WORKING_SET_UPDATE', 'WORKING_SET_CONFIG_UPDATE', 'ITEM_MOVE', 'DEPLOYMENT_IMPORT', 'PDF_MERGE', 'EXPORT_TO_WORD', 'DOCUMENT_MERGE']):
            raise ValueError("must be one of enum values ('RUN_IN_EXCEL', 'MASS_TEST_SET_RUN_CREATION', 'DEPENDENCY_FINDER', 'ITEM_EXCEL_IMPORT', 'DEPLOYMENT_EXPORT', 'WORKING_SET_UPDATE', 'WORKING_SET_CONFIG_UPDATE', 'ITEM_MOVE', 'DEPLOYMENT_IMPORT', 'PDF_MERGE', 'EXPORT_TO_WORD', 'DOCUMENT_MERGE')")
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
        """Create an instance of BackgroundJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status_info
        if self.status_info:
            _dict['statusInfo'] = self.status_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of submitted_by
        if self.submitted_by:
            _dict['submittedBy'] = self.submitted_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackgroundJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backgroundJobStatus": obj.get("backgroundJobStatus"),
            "backgroundJobType": obj.get("backgroundJobType"),
            "createdAt": obj.get("createdAt"),
            "description": obj.get("description"),
            "finishedAt": obj.get("finishedAt"),
            "id": obj.get("id"),
            "statusInfo": AbstractBackgroundJobStatusInfo.from_dict(obj["statusInfo"]) if obj.get("statusInfo") is not None else None,
            "steps": [BackgroundJobStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "submittedBy": UserReference.from_dict(obj["submittedBy"]) if obj.get("submittedBy") is not None else None
        })
        return _obj

