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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.abstract_reference import AbstractReference
from openapi_client.models.association_type_reference import AssociationTypeReference
from openapi_client.models.user_reference import UserReference
from typing import Optional, Set
from typing_extensions import Self

class Association(BaseModel):
    """
    Basic properties of a codebeamer association
    """ # noqa: E501
    baseline_id: Optional[StrictInt] = Field(default=None, description="Baseline ID", alias="baselineId")
    bi_directional_propagation: Optional[StrictBool] = Field(default=None, description="Bi-directional reference", alias="biDirectionalPropagation")
    created_at: Optional[datetime] = Field(default=None, description="The date when the entity was created", alias="createdAt")
    created_by: Optional[UserReference] = Field(default=None, alias="createdBy")
    description: Optional[StrictStr] = Field(default=None, description="Description of the entity")
    description_format: Optional[StrictStr] = Field(default=None, description="Description format of the entity", alias="descriptionFormat")
    var_from: AbstractReference = Field(alias="from")
    id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Id of the entity")
    name: Optional[StrictStr] = Field(default=None, description="Name of the entity")
    propagating_dependencies: Optional[StrictBool] = Field(default=None, description="Propagating dependencies", alias="propagatingDependencies")
    propagating_suspects: Optional[StrictBool] = Field(default=None, description="Propagating suspects", alias="propagatingSuspects")
    reverse_propagation: Optional[StrictBool] = Field(default=None, description="Reverse propagation", alias="reversePropagation")
    to: Optional[AbstractReference] = None
    type: Optional[AssociationTypeReference] = None
    url: Optional[StrictStr] = Field(default=None, description="Association to url")
    __properties: ClassVar[List[str]] = ["baselineId", "biDirectionalPropagation", "createdAt", "createdBy", "description", "descriptionFormat", "from", "id", "name", "propagatingDependencies", "propagatingSuspects", "reversePropagation", "to", "type", "url"]

    @field_validator('description_format')
    def description_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PlainText', 'Html', 'Wiki']):
            raise ValueError("must be one of enum values ('PlainText', 'Html', 'Wiki')")
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
        """Create an instance of Association from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Association from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baselineId": obj.get("baselineId"),
            "biDirectionalPropagation": obj.get("biDirectionalPropagation"),
            "createdAt": obj.get("createdAt"),
            "createdBy": UserReference.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "description": obj.get("description"),
            "descriptionFormat": obj.get("descriptionFormat"),
            "from": AbstractReference.from_dict(obj["from"]) if obj.get("from") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "propagatingDependencies": obj.get("propagatingDependencies"),
            "propagatingSuspects": obj.get("propagatingSuspects"),
            "reversePropagation": obj.get("reversePropagation"),
            "to": AbstractReference.from_dict(obj["to"]) if obj.get("to") is not None else None,
            "type": AssociationTypeReference.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "url": obj.get("url")
        })
        return _obj


