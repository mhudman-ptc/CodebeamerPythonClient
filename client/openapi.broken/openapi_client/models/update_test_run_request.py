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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.update_test_case_run_request import UpdateTestCaseRunRequest
from typing import Optional, Set
from typing_extensions import Self

class UpdateTestRunRequest(BaseModel):
    """
    Model to contain Test Case run update request models
    """ # noqa: E501
    parent_result_propagation: Optional[StrictBool] = Field(default=True, description="The propagation of the result is enabled for parent Test Run or not", alias="parentResultPropagation")
    update_request_models: List[UpdateTestCaseRunRequest] = Field(description="List of update Test Case run request models", alias="updateRequestModels")
    __properties: ClassVar[List[str]] = ["parentResultPropagation", "updateRequestModels"]

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
        """Create an instance of UpdateTestRunRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in update_request_models (list)
        _items = []
        if self.update_request_models:
            for _item in self.update_request_models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['updateRequestModels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTestRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parentResultPropagation": obj.get("parentResultPropagation") if obj.get("parentResultPropagation") is not None else True,
            "updateRequestModels": [UpdateTestCaseRunRequest.from_dict(_item) for _item in obj["updateRequestModels"]] if obj.get("updateRequestModels") is not None else None
        })
        return _obj


