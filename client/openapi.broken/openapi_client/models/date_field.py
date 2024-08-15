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

from pydantic import ConfigDict
from typing import Any, ClassVar, Dict, List
from openapi_client.models.abstract_field import AbstractField
from openapi_client.models.choice_option_reference import ChoiceOptionReference
from openapi_client.models.shared_field_reference import SharedFieldReference
from typing import Optional, Set
from typing_extensions import Self

class DateField(AbstractField):
    """
    Date field
    """ # noqa: E501
    __properties: ClassVar[List[str]] = ["description", "formula", "hidden", "hideIfDependencyFormula", "id", "legacyRestName", "mandatoryIfDependencyFormula", "mandatoryInStatuses", "name", "sharedFields", "title", "trackerItemField", "type", "valueModel"]

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
        """Create an instance of DateField from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mandatory_in_statuses (list)
        _items = []
        if self.mandatory_in_statuses:
            for _item in self.mandatory_in_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mandatoryInStatuses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shared_fields (list)
        _items = []
        if self.shared_fields:
            for _item in self.shared_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sharedFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DateField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "formula": obj.get("formula"),
            "hidden": obj.get("hidden"),
            "hideIfDependencyFormula": obj.get("hideIfDependencyFormula"),
            "id": obj.get("id"),
            "legacyRestName": obj.get("legacyRestName"),
            "mandatoryIfDependencyFormula": obj.get("mandatoryIfDependencyFormula"),
            "mandatoryInStatuses": [ChoiceOptionReference.from_dict(_item) for _item in obj["mandatoryInStatuses"]] if obj.get("mandatoryInStatuses") is not None else None,
            "name": obj.get("name"),
            "sharedFields": [SharedFieldReference.from_dict(_item) for _item in obj["sharedFields"]] if obj.get("sharedFields") is not None else None,
            "title": obj.get("title"),
            "trackerItemField": obj.get("trackerItemField"),
            "type": obj.get("type"),
            "valueModel": obj.get("valueModel")
        })
        return _obj


