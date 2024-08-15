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
    from openapi_client.models.choice_documents import ChoiceDocuments
    from openapi_client.models.choice_members import ChoiceMembers
    from openapi_client.models.choice_options import ChoiceOptions
    from openapi_client.models.choice_projects import ChoiceProjects
    from openapi_client.models.choice_repositories import ChoiceRepositories
    from openapi_client.models.choice_trackers import ChoiceTrackers
    from openapi_client.models.choice_users import ChoiceUsers
    from openapi_client.models.choice_work_config_items import ChoiceWorkConfigItems

class BaseTrackerFieldChoiceOption(BaseModel):
    """
    Describes a Choice Option field configuration.
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
        'ChoiceDocuments': 'ChoiceDocuments','ChoiceMembers': 'ChoiceMembers','ChoiceOptions': 'ChoiceOptions','ChoiceProjects': 'ChoiceProjects','ChoiceRepositories': 'ChoiceRepositories','ChoiceTrackers': 'ChoiceTrackers','ChoiceUsers': 'ChoiceUsers','ChoiceWorkConfigItems': 'ChoiceWorkConfigItems'
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
    def from_json(cls, json_str: str) -> Optional[Union[ChoiceDocuments, ChoiceMembers, ChoiceOptions, ChoiceProjects, ChoiceRepositories, ChoiceTrackers, ChoiceUsers, ChoiceWorkConfigItems]]:
        """Create an instance of BaseTrackerFieldChoiceOption from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ChoiceDocuments, ChoiceMembers, ChoiceOptions, ChoiceProjects, ChoiceRepositories, ChoiceTrackers, ChoiceUsers, ChoiceWorkConfigItems]]:
        """Create an instance of BaseTrackerFieldChoiceOption from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ChoiceDocuments':
            return import_module("openapi_client.models.choice_documents").ChoiceDocuments.from_dict(obj)
        if object_type ==  'ChoiceMembers':
            return import_module("openapi_client.models.choice_members").ChoiceMembers.from_dict(obj)
        if object_type ==  'ChoiceOptions':
            return import_module("openapi_client.models.choice_options").ChoiceOptions.from_dict(obj)
        if object_type ==  'ChoiceProjects':
            return import_module("openapi_client.models.choice_projects").ChoiceProjects.from_dict(obj)
        if object_type ==  'ChoiceRepositories':
            return import_module("openapi_client.models.choice_repositories").ChoiceRepositories.from_dict(obj)
        if object_type ==  'ChoiceTrackers':
            return import_module("openapi_client.models.choice_trackers").ChoiceTrackers.from_dict(obj)
        if object_type ==  'ChoiceUsers':
            return import_module("openapi_client.models.choice_users").ChoiceUsers.from_dict(obj)
        if object_type ==  'ChoiceWorkConfigItems':
            return import_module("openapi_client.models.choice_work_config_items").ChoiceWorkConfigItems.from_dict(obj)

        raise ValueError("BaseTrackerFieldChoiceOption failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

