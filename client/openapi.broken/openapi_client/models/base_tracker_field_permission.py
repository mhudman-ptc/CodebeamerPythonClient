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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.per_status_field_permission import PerStatusFieldPermission
    from openapi_client.models.same_as_field_permission import SameAsFieldPermission
    from openapi_client.models.single_field_permission import SingleFieldPermission
    from openapi_client.models.unrestricted_field_permission import UnrestrictedFieldPermission

class BaseTrackerFieldPermission(BaseModel):
    """
    Describes the permission of a Tracker Field.
    """ # noqa: E501
    type: StrictStr
    __properties: ClassVar[List[str]] = ["type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'PerStatusFieldPermission': 'PerStatusFieldPermission','SameAsFieldPermission': 'SameAsFieldPermission','SingleFieldPermission': 'SingleFieldPermission','UnrestrictedFieldPermission': 'UnrestrictedFieldPermission'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[PerStatusFieldPermission, SameAsFieldPermission, SingleFieldPermission, UnrestrictedFieldPermission]]:
        """Create an instance of BaseTrackerFieldPermission from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[PerStatusFieldPermission, SameAsFieldPermission, SingleFieldPermission, UnrestrictedFieldPermission]]:
        """Create an instance of BaseTrackerFieldPermission from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'PerStatusFieldPermission':
            return import_module("openapi_client.models.per_status_field_permission").PerStatusFieldPermission.from_dict(obj)
        if object_type ==  'SameAsFieldPermission':
            return import_module("openapi_client.models.same_as_field_permission").SameAsFieldPermission.from_dict(obj)
        if object_type ==  'SingleFieldPermission':
            return import_module("openapi_client.models.single_field_permission").SingleFieldPermission.from_dict(obj)
        if object_type ==  'UnrestrictedFieldPermission':
            return import_module("openapi_client.models.unrestricted_field_permission").UnrestrictedFieldPermission.from_dict(obj)

        raise ValueError("BaseTrackerFieldPermission failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


