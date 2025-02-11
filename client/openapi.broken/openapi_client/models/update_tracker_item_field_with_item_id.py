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
from openapi_client.models.abstract_field_value import AbstractFieldValue
from openapi_client.models.table_field_value import TableFieldValue
from typing import Optional, Set
from typing_extensions import Self

class UpdateTrackerItemFieldWithItemId(BaseModel):
    """
    Update fields of a tracker item and provide the itemId as well
    """ # noqa: E501
    field_values: Optional[List[AbstractFieldValue]] = Field(default=None, description="Fields of a tracker item", alias="fieldValues")
    item_id: Optional[StrictInt] = Field(default=None, description="Id of a tracker item", alias="itemId")
    table_values: Optional[List[TableFieldValue]] = Field(default=None, description="Fields of a tracker item", alias="tableValues")
    __properties: ClassVar[List[str]] = ["fieldValues", "itemId", "tableValues"]

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
        """Create an instance of UpdateTrackerItemFieldWithItemId from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in field_values (list)
        _items = []
        if self.field_values:
            for _item in self.field_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fieldValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in table_values (list)
        _items = []
        if self.table_values:
            for _item in self.table_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tableValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateTrackerItemFieldWithItemId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fieldValues": [AbstractFieldValue.from_dict(_item) for _item in obj["fieldValues"]] if obj.get("fieldValues") is not None else None,
            "itemId": obj.get("itemId"),
            "tableValues": [TableFieldValue.from_dict(_item) for _item in obj["tableValues"]] if obj.get("tableValues") is not None else None
        })
        return _obj


