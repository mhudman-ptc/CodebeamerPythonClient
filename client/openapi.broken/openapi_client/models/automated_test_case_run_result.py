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
from typing import Optional, Set
from typing_extensions import Self

class AutomatedTestCaseRunResult(BaseModel):
    """
    Request model to create a test run from test case
    """ # noqa: E501
    conclusion: Optional[StrictStr] = Field(default=None, description="Optional Test Case Run conclusion")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Test Case")
    group_name: Optional[StrictStr] = Field(default=None, description="Group name of the Test Case", alias="groupName")
    name: StrictStr = Field(description="Name of the Test Case")
    result: StrictStr = Field(description="Result of the test case")
    run_time: Optional[StrictInt] = Field(default=None, description="Optional runtime in seconds", alias="runTime")
    __properties: ClassVar[List[str]] = ["conclusion", "description", "groupName", "name", "result", "runTime"]

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
        """Create an instance of AutomatedTestCaseRunResult from a JSON string"""
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
        """Create an instance of AutomatedTestCaseRunResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conclusion": obj.get("conclusion"),
            "description": obj.get("description"),
            "groupName": obj.get("groupName"),
            "name": obj.get("name"),
            "result": obj.get("result"),
            "runTime": obj.get("runTime")
        })
        return _obj

