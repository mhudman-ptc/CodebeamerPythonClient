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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.base_tracker_field_choice_option import BaseTrackerFieldChoiceOption
from openapi_client.models.base_tracker_field_permission import BaseTrackerFieldPermission
from openapi_client.models.tracker_field_computed_field_reference import TrackerFieldComputedFieldReference
from openapi_client.models.tracker_field_date_field_settings import TrackerFieldDateFieldSettings
from openapi_client.models.tracker_field_dependency import TrackerFieldDependency
from openapi_client.models.tracker_field_service_desk_field import TrackerFieldServiceDeskField
from typing import Optional, Set
from typing_extensions import Self

class TrackerField(BaseModel):
    """
    This model represents a whole Tracker Field configuration.
    """ # noqa: E501
    aggregation_rule: Optional[StrictStr] = Field(default=None, description="The Aggregation Rule for a specific Field.", alias="aggregationRule")
    choice_option_setting: Optional[BaseTrackerFieldChoiceOption] = Field(default=None, alias="choiceOptionSetting")
    computed_as: Optional[StrictStr] = Field(default=None, alias="computedAs")
    computed_field_references: Optional[List[TrackerFieldComputedFieldReference]] = Field(default=None, alias="computedFieldReferences")
    date_field_settings: Optional[TrackerFieldDateFieldSettings] = Field(default=None, alias="dateFieldSettings")
    default_values_in_statuses: Optional[Dict[str, StrictStr]] = Field(default=None, alias="defaultValuesInStatuses")
    dependency: Optional[TrackerFieldDependency] = None
    description: Optional[StrictStr] = None
    digits: Optional[StrictInt] = None
    distribution_rule: Optional[StrictStr] = Field(default=None, description="The Distribution Rule of a specific Field.", alias="distributionRule")
    global_type_ids: Optional[List[StrictInt]] = Field(default=None, alias="globalTypeIds")
    height: Optional[StrictInt] = None
    hidden: Optional[StrictBool] = None
    hide_if_formula: Optional[StrictStr] = Field(default=None, alias="hideIfFormula")
    hide_if_formula_same_as_field_id: Optional[StrictInt] = Field(default=None, alias="hideIfFormulaSameAsFieldId")
    label: Optional[StrictStr] = None
    listable: Optional[StrictBool] = None
    mandatory: Optional[StrictBool] = None
    mandatory_if_formula: Optional[StrictStr] = Field(default=None, alias="mandatoryIfFormula")
    mandatory_if_formula_same_as_field_id: Optional[StrictInt] = Field(default=None, alias="mandatoryIfFormulaSameAsFieldId")
    max_value: Optional[StrictStr] = Field(default=None, alias="maxValue")
    min_value: Optional[StrictStr] = Field(default=None, alias="minValue")
    multiple_selection: Optional[StrictBool] = Field(default=None, alias="multipleSelection")
    new_line: Optional[StrictBool] = Field(default=None, alias="newLine")
    omit_merge: Optional[StrictBool] = Field(default=None, alias="omitMerge")
    omit_suspected_when_change: Optional[StrictBool] = Field(default=None, alias="omitSuspectedWhenChange")
    permission: Optional[BaseTrackerFieldPermission] = None
    position: Optional[StrictInt] = None
    propagate_dependencies: Optional[StrictBool] = Field(default=None, alias="propagateDependencies")
    propagate_suspect: Optional[StrictBool] = Field(default=None, alias="propagateSuspect")
    reference_id: Optional[StrictInt] = Field(default=None, alias="referenceId")
    reversed_suspect: Optional[StrictBool] = Field(default=None, alias="reversedSuspect")
    service_desk_field: Optional[TrackerFieldServiceDeskField] = Field(default=None, alias="serviceDeskField")
    span: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    type_id: Optional[StrictInt] = Field(default=None, alias="typeId")
    union: Optional[StrictBool] = None
    width: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["aggregationRule", "choiceOptionSetting", "computedAs", "computedFieldReferences", "dateFieldSettings", "defaultValuesInStatuses", "dependency", "description", "digits", "distributionRule", "globalTypeIds", "height", "hidden", "hideIfFormula", "hideIfFormulaSameAsFieldId", "label", "listable", "mandatory", "mandatoryIfFormula", "mandatoryIfFormulaSameAsFieldId", "maxValue", "minValue", "multipleSelection", "newLine", "omitMerge", "omitSuspectedWhenChange", "permission", "position", "propagateDependencies", "propagateSuspect", "referenceId", "reversedSuspect", "serviceDeskField", "span", "title", "typeId", "union", "width"]

    @field_validator('aggregation_rule')
    def aggregation_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MINIMUM', 'MAXIMUM', 'UNION', 'INTERSECTION', 'SUM_TOTAL', 'AVERAGE']):
            raise ValueError("must be one of enum values ('MINIMUM', 'MAXIMUM', 'UNION', 'INTERSECTION', 'SUM_TOTAL', 'AVERAGE')")
        return value

    @field_validator('distribution_rule')
    def distribution_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SET', 'DEFAULT', 'LEAST', 'GREATEST', 'SUBSET', 'SUPERSET', 'CLOSE_RECURSIVELY', 'CLOSE_RESTRICTED']):
            raise ValueError("must be one of enum values ('SET', 'DEFAULT', 'LEAST', 'GREATEST', 'SUBSET', 'SUPERSET', 'CLOSE_RECURSIVELY', 'CLOSE_RESTRICTED')")
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
        """Create an instance of TrackerField from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of choice_option_setting
        if self.choice_option_setting:
            _dict['choiceOptionSetting'] = self.choice_option_setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in computed_field_references (list)
        _items = []
        if self.computed_field_references:
            for _item in self.computed_field_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['computedFieldReferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of date_field_settings
        if self.date_field_settings:
            _dict['dateFieldSettings'] = self.date_field_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dependency
        if self.dependency:
            _dict['dependency'] = self.dependency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permission
        if self.permission:
            _dict['permission'] = self.permission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_desk_field
        if self.service_desk_field:
            _dict['serviceDeskField'] = self.service_desk_field.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackerField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationRule": obj.get("aggregationRule"),
            "choiceOptionSetting": BaseTrackerFieldChoiceOption.from_dict(obj["choiceOptionSetting"]) if obj.get("choiceOptionSetting") is not None else None,
            "computedAs": obj.get("computedAs"),
            "computedFieldReferences": [TrackerFieldComputedFieldReference.from_dict(_item) for _item in obj["computedFieldReferences"]] if obj.get("computedFieldReferences") is not None else None,
            "dateFieldSettings": TrackerFieldDateFieldSettings.from_dict(obj["dateFieldSettings"]) if obj.get("dateFieldSettings") is not None else None,
            "defaultValuesInStatuses": obj.get("defaultValuesInStatuses"),
            "dependency": TrackerFieldDependency.from_dict(obj["dependency"]) if obj.get("dependency") is not None else None,
            "description": obj.get("description"),
            "digits": obj.get("digits"),
            "distributionRule": obj.get("distributionRule"),
            "globalTypeIds": obj.get("globalTypeIds"),
            "height": obj.get("height"),
            "hidden": obj.get("hidden"),
            "hideIfFormula": obj.get("hideIfFormula"),
            "hideIfFormulaSameAsFieldId": obj.get("hideIfFormulaSameAsFieldId"),
            "label": obj.get("label"),
            "listable": obj.get("listable"),
            "mandatory": obj.get("mandatory"),
            "mandatoryIfFormula": obj.get("mandatoryIfFormula"),
            "mandatoryIfFormulaSameAsFieldId": obj.get("mandatoryIfFormulaSameAsFieldId"),
            "maxValue": obj.get("maxValue"),
            "minValue": obj.get("minValue"),
            "multipleSelection": obj.get("multipleSelection"),
            "newLine": obj.get("newLine"),
            "omitMerge": obj.get("omitMerge"),
            "omitSuspectedWhenChange": obj.get("omitSuspectedWhenChange"),
            "permission": BaseTrackerFieldPermission.from_dict(obj["permission"]) if obj.get("permission") is not None else None,
            "position": obj.get("position"),
            "propagateDependencies": obj.get("propagateDependencies"),
            "propagateSuspect": obj.get("propagateSuspect"),
            "referenceId": obj.get("referenceId"),
            "reversedSuspect": obj.get("reversedSuspect"),
            "serviceDeskField": TrackerFieldServiceDeskField.from_dict(obj["serviceDeskField"]) if obj.get("serviceDeskField") is not None else None,
            "span": obj.get("span"),
            "title": obj.get("title"),
            "typeId": obj.get("typeId"),
            "union": obj.get("union"),
            "width": obj.get("width")
        })
        return _obj


