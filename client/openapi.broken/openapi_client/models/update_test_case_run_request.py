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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.abstract_field_value import AbstractFieldValue
from openapi_client.models.tracker_item_reference import TrackerItemReference
from typing import Optional, Set
from typing_extensions import Self

class UpdateTestCaseRunRequest(BaseModel):
    """
    Request model to update Test Run's result for a Test Case
    """ # noqa: E501
    conclusion: Optional[StrictStr] = Field(default=None, description="Optional conclusion text")
    custom_fields: Optional[List[AbstractFieldValue]] = Field(default=None, description="Optional field values to set on the Test Run", alias="customFields")
    reported_bug_references: Optional[List[TrackerItemReference]] = Field(default=None, description="Optional reference list of Bugs attached to the Test result", alias="reportedBugReferences")
    result: StrictStr = Field(description="Result of the test case")
    run_time: Optional[StrictInt] = Field(default=None, description="Optional runtime in seconds", alias="runTime")
    test_case_reference: TrackerItemReference = Field(alias="testCaseReference")
    __properties: ClassVar[List[str]] = ["conclusion", "customFields", "reportedBugReferences", "result", "runTime", "testCaseReference"]

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PASSED', 'FAILED', 'BLOCKED', 'NOT_APPLICABLE']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'BLOCKED', 'NOT_APPLICABLE')")
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
        """Create an instance of UpdateTestCaseRunRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reported_bug_references (list)
        _items = []
        if self.reported_bug_references:
            for _item in self.reported_bug_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reportedBugReferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of test_case_reference
        if self.test_case_reference:
            _dict['testCaseReference'] = self.test_case_reference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTestCaseRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conclusion": obj.get("conclusion"),
            "customFields": [AbstractFieldValue.from_dict(_item) for _item in obj["customFields"]] if obj.get("customFields") is not None else None,
            "reportedBugReferences": [TrackerItemReference.from_dict(_item) for _item in obj["reportedBugReferences"]] if obj.get("reportedBugReferences") is not None else None,
            "result": obj.get("result"),
            "runTime": obj.get("runTime"),
            "testCaseReference": TrackerItemReference.from_dict(obj["testCaseReference"]) if obj.get("testCaseReference") is not None else None
        })
        return _obj


