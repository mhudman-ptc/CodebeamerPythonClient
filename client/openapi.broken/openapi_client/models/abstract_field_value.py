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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from openapi_client.models.bool_field_value import BoolFieldValue
    from openapi_client.models.choice_field_multi_value import ChoiceFieldMultiValue
    from openapi_client.models.choice_field_value import ChoiceFieldValue
    from openapi_client.models.color_field_value import ColorFieldValue
    from openapi_client.models.country_field_multi_value import CountryFieldMultiValue
    from openapi_client.models.country_field_value import CountryFieldValue
    from openapi_client.models.date_field_value import DateFieldValue
    from openapi_client.models.decimal_field_value import DecimalFieldValue
    from openapi_client.models.duration_field_value import DurationFieldValue
    from openapi_client.models.integer_field_value import IntegerFieldValue
    from openapi_client.models.language_field_multi_value import LanguageFieldMultiValue
    from openapi_client.models.language_field_value import LanguageFieldValue
    from openapi_client.models.not_supported_field_value import NotSupportedFieldValue
    from openapi_client.models.referred_test_step_field_value import ReferredTestStepFieldValue
    from openapi_client.models.table_field_value import TableFieldValue
    from openapi_client.models.text_field_value import TextFieldValue
    from openapi_client.models.url_field_value import UrlFieldValue
    from openapi_client.models.wiki_text_field_multi_value import WikiTextFieldMultiValue
    from openapi_client.models.wiki_text_field_value import WikiTextFieldValue

class AbstractFieldValue(BaseModel):
    """
    Value container of a field
    """ # noqa: E501
    field_id: Optional[StrictInt] = Field(default=None, description="Id of the field", alias="fieldId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the field")
    shared_field_name: Optional[StrictStr] = Field(default=None, description="The name of a shared field assigned to the field. This can be specified as an alternative to fieldId.", alias="sharedFieldName")
    shared_field_names: Optional[List[StrictStr]] = Field(default=None, description="The names of a shared fields assigned to the field.", alias="sharedFieldNames")
    type: StrictStr = Field(description="Type of the field")
    __properties: ClassVar[List[str]] = ["fieldId", "name", "sharedFieldName", "sharedFieldNames", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'BoolFieldValue': 'BoolFieldValue','ChoiceFieldMultiValue': 'ChoiceFieldMultiValue','ChoiceFieldValue': 'ChoiceFieldValue','ColorFieldValue': 'ColorFieldValue','CountryFieldMultiValue': 'CountryFieldMultiValue','CountryFieldValue': 'CountryFieldValue','DateFieldValue': 'DateFieldValue','DecimalFieldValue': 'DecimalFieldValue','DurationFieldValue': 'DurationFieldValue','IntegerFieldValue': 'IntegerFieldValue','LanguageFieldMultiValue': 'LanguageFieldMultiValue','LanguageFieldValue': 'LanguageFieldValue','NotSupportedFieldValue': 'NotSupportedFieldValue','ReferredTestStepFieldValue': 'ReferredTestStepFieldValue','TableFieldValue': 'TableFieldValue','TextFieldValue': 'TextFieldValue','UrlFieldValue': 'UrlFieldValue','WikiTextFieldMultiValue': 'WikiTextFieldMultiValue','WikiTextFieldValue': 'WikiTextFieldValue'
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
    def from_json(cls, json_str: str) -> Optional[Union[BoolFieldValue, ChoiceFieldMultiValue, ChoiceFieldValue, ColorFieldValue, CountryFieldMultiValue, CountryFieldValue, DateFieldValue, DecimalFieldValue, DurationFieldValue, IntegerFieldValue, LanguageFieldMultiValue, LanguageFieldValue, NotSupportedFieldValue, ReferredTestStepFieldValue, TableFieldValue, TextFieldValue, UrlFieldValue, WikiTextFieldMultiValue, WikiTextFieldValue]]:
        """Create an instance of AbstractFieldValue from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[BoolFieldValue, ChoiceFieldMultiValue, ChoiceFieldValue, ColorFieldValue, CountryFieldMultiValue, CountryFieldValue, DateFieldValue, DecimalFieldValue, DurationFieldValue, IntegerFieldValue, LanguageFieldMultiValue, LanguageFieldValue, NotSupportedFieldValue, ReferredTestStepFieldValue, TableFieldValue, TextFieldValue, UrlFieldValue, WikiTextFieldMultiValue, WikiTextFieldValue]]:
        """Create an instance of AbstractFieldValue from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'BoolFieldValue':
            return import_module("openapi_client.models.bool_field_value").BoolFieldValue.from_dict(obj)
        if object_type ==  'ChoiceFieldMultiValue':
            return import_module("openapi_client.models.choice_field_multi_value").ChoiceFieldMultiValue.from_dict(obj)
        if object_type ==  'ChoiceFieldValue':
            return import_module("openapi_client.models.choice_field_value").ChoiceFieldValue.from_dict(obj)
        if object_type ==  'ColorFieldValue':
            return import_module("openapi_client.models.color_field_value").ColorFieldValue.from_dict(obj)
        if object_type ==  'CountryFieldMultiValue':
            return import_module("openapi_client.models.country_field_multi_value").CountryFieldMultiValue.from_dict(obj)
        if object_type ==  'CountryFieldValue':
            return import_module("openapi_client.models.country_field_value").CountryFieldValue.from_dict(obj)
        if object_type ==  'DateFieldValue':
            return import_module("openapi_client.models.date_field_value").DateFieldValue.from_dict(obj)
        if object_type ==  'DecimalFieldValue':
            return import_module("openapi_client.models.decimal_field_value").DecimalFieldValue.from_dict(obj)
        if object_type ==  'DurationFieldValue':
            return import_module("openapi_client.models.duration_field_value").DurationFieldValue.from_dict(obj)
        if object_type ==  'IntegerFieldValue':
            return import_module("openapi_client.models.integer_field_value").IntegerFieldValue.from_dict(obj)
        if object_type ==  'LanguageFieldMultiValue':
            return import_module("openapi_client.models.language_field_multi_value").LanguageFieldMultiValue.from_dict(obj)
        if object_type ==  'LanguageFieldValue':
            return import_module("openapi_client.models.language_field_value").LanguageFieldValue.from_dict(obj)
        if object_type ==  'NotSupportedFieldValue':
            return import_module("openapi_client.models.not_supported_field_value").NotSupportedFieldValue.from_dict(obj)
        if object_type ==  'ReferredTestStepFieldValue':
            return import_module("openapi_client.models.referred_test_step_field_value").ReferredTestStepFieldValue.from_dict(obj)
        if object_type ==  'TableFieldValue':
            return import_module("openapi_client.models.table_field_value").TableFieldValue.from_dict(obj)
        if object_type ==  'TextFieldValue':
            return import_module("openapi_client.models.text_field_value").TextFieldValue.from_dict(obj)
        if object_type ==  'UrlFieldValue':
            return import_module("openapi_client.models.url_field_value").UrlFieldValue.from_dict(obj)
        if object_type ==  'WikiTextFieldMultiValue':
            return import_module("openapi_client.models.wiki_text_field_multi_value").WikiTextFieldMultiValue.from_dict(obj)
        if object_type ==  'WikiTextFieldValue':
            return import_module("openapi_client.models.wiki_text_field_value").WikiTextFieldValue.from_dict(obj)

        raise ValueError("AbstractFieldValue failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

