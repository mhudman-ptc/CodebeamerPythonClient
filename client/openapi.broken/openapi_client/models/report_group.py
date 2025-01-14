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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.report_aggregate import ReportAggregate
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.report_group_with_groups import ReportGroupWithGroups
    from openapi_client.models.report_group_with_referenced_rows import ReportGroupWithReferencedRows
    from openapi_client.models.report_group_with_rows import ReportGroupWithRows

class ReportGroup(BaseModel):
    """
    A report group which can contain rows or other groups based on the type.
    """ # noqa: E501
    aggregates: Optional[List[ReportAggregate]] = Field(default=None, description="List of the aggregate values with column id.")
    count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of items in the group, if it has subgroups then the aggregated number of items.")
    grouping_value: Optional[StrictStr] = Field(default=None, description="The common value in the group, , if it's available", alias="groupingValue")
    grouping_value_id: Optional[StrictInt] = Field(default=None, description="The id of the common value in the group, if it's available", alias="groupingValueId")
    header: Optional[StrictStr] = Field(default=None, description="Grouping header")
    type: Optional[StrictStr] = Field(default=None, description="Type of the group.")
    __properties: ClassVar[List[str]] = ["aggregates", "count", "groupingValue", "groupingValueId", "header", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ReportGroupWithGroups': 'ReportGroupWithGroups','ReportGroupWithReferencedRows': 'ReportGroupWithReferencedRows','ReportGroupWithRows': 'ReportGroupWithRows'
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
    def from_json(cls, json_str: str) -> Optional[Union[ReportGroupWithGroups, ReportGroupWithReferencedRows, ReportGroupWithRows]]:
        """Create an instance of ReportGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aggregates (list)
        _items = []
        if self.aggregates:
            for _item in self.aggregates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['aggregates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ReportGroupWithGroups, ReportGroupWithReferencedRows, ReportGroupWithRows]]:
        """Create an instance of ReportGroup from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ReportGroupWithGroups':
            return import_module("openapi_client.models.report_group_with_groups").ReportGroupWithGroups.from_dict(obj)
        if object_type ==  'ReportGroupWithReferencedRows':
            return import_module("openapi_client.models.report_group_with_referenced_rows").ReportGroupWithReferencedRows.from_dict(obj)
        if object_type ==  'ReportGroupWithRows':
            return import_module("openapi_client.models.report_group_with_rows").ReportGroupWithRows.from_dict(obj)

        raise ValueError("ReportGroup failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


