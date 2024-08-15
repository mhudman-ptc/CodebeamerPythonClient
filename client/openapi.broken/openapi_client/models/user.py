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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    Properties of a codebeamer user
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="Address of a user")
    city: Optional[StrictStr] = Field(default=None, description="City of a user")
    company: Optional[StrictStr] = Field(default=None, description="Company of a user")
    country: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="Country of a user in ISO 3166-1 alpha-2 format")
    date_format: Optional[StrictStr] = Field(default=None, description="Date format of a user", alias="dateFormat")
    email: Optional[StrictStr] = Field(default=None, description="Email of a user")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of a user", alias="firstName")
    id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Id of the entity")
    language: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, description="Language of a user in ISO 639-1 format")
    last_login_date: Optional[datetime] = Field(default=None, description="Last login date of a user", alias="lastLoginDate")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of a user", alias="lastName")
    mobile: Optional[StrictStr] = Field(default=None, description="Mobile number of a user")
    name: Optional[StrictStr] = Field(default=None, description="Name of the entity")
    phone: Optional[StrictStr] = Field(default=None, description="Phone number of a user")
    registry_date: Optional[datetime] = Field(default=None, description="Registration date of a user", alias="registryDate")
    skills: Optional[StrictStr] = Field(default=None, description="Skills of a user")
    state: Optional[StrictStr] = Field(default=None, description="State / providence of a user")
    status: Optional[StrictStr] = Field(default=None, description="Status of a user")
    time_zone: Optional[StrictStr] = Field(default=None, description="Time zone of a user", alias="timeZone")
    title: Optional[StrictStr] = Field(default=None, description="Title of a user")
    zip: Optional[StrictStr] = Field(default=None, description="Zip of a user")
    __properties: ClassVar[List[str]] = ["address", "city", "company", "country", "dateFormat", "email", "firstName", "id", "language", "lastLoginDate", "lastName", "mobile", "name", "phone", "registryDate", "skills", "state", "status", "timeZone", "title", "zip"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVATED', 'DISABLED', 'INACTIVATION']):
            raise ValueError("must be one of enum values ('ACTIVATED', 'DISABLED', 'INACTIVATION')")
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
        """Create an instance of User from a JSON string"""
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
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "city": obj.get("city"),
            "company": obj.get("company"),
            "country": obj.get("country"),
            "dateFormat": obj.get("dateFormat"),
            "email": obj.get("email"),
            "firstName": obj.get("firstName"),
            "id": obj.get("id"),
            "language": obj.get("language"),
            "lastLoginDate": obj.get("lastLoginDate"),
            "lastName": obj.get("lastName"),
            "mobile": obj.get("mobile"),
            "name": obj.get("name"),
            "phone": obj.get("phone"),
            "registryDate": obj.get("registryDate"),
            "skills": obj.get("skills"),
            "state": obj.get("state"),
            "status": obj.get("status"),
            "timeZone": obj.get("timeZone"),
            "title": obj.get("title"),
            "zip": obj.get("zip")
        })
        return _obj


