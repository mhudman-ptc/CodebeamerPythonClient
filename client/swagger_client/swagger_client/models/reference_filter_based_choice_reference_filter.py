# coding: utf-8

"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReferenceFilterBasedChoiceReferenceFilter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain_id': 'int',
        'domain_type': 'str',
        'filter_id': 'int',
        'filter_status_id': 'int',
        'id': 'int',
        'target_ids': 'list[int]',
        'target_permissions': 'list[str]'
    }

    attribute_map = {
        'domain_id': 'domainId',
        'domain_type': 'domainType',
        'filter_id': 'filterId',
        'filter_status_id': 'filterStatusId',
        'id': 'id',
        'target_ids': 'targetIds',
        'target_permissions': 'targetPermissions'
    }

    def __init__(self, domain_id=None, domain_type=None, filter_id=None, filter_status_id=None, id=None, target_ids=None, target_permissions=None):  # noqa: E501
        """ReferenceFilterBasedChoiceReferenceFilter - a model defined in Swagger"""  # noqa: E501
        self._domain_id = None
        self._domain_type = None
        self._filter_id = None
        self._filter_status_id = None
        self._id = None
        self._target_ids = None
        self._target_permissions = None
        self.discriminator = None
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_type is not None:
            self.domain_type = domain_type
        if filter_id is not None:
            self.filter_id = filter_id
        if filter_status_id is not None:
            self.filter_status_id = filter_status_id
        if id is not None:
            self.id = id
        if target_ids is not None:
            self.target_ids = target_ids
        if target_permissions is not None:
            self.target_permissions = target_permissions

    @property
    def domain_id(self):
        """Gets the domain_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The domain_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ReferenceFilterBasedChoiceReferenceFilter.


        :param domain_id: The domain_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: int
        """

        self._domain_id = domain_id

    @property
    def domain_type(self):
        """Gets the domain_type of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The domain_type of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this ReferenceFilterBasedChoiceReferenceFilter.


        :param domain_type: The domain_type of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRACKER", "PROJECT"]  # noqa: E501
        if domain_type not in allowed_values:
            raise ValueError(
                "Invalid value for `domain_type` ({0}), must be one of {1}"  # noqa: E501
                .format(domain_type, allowed_values)
            )

        self._domain_type = domain_type

    @property
    def filter_id(self):
        """Gets the filter_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The filter_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: int
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """Sets the filter_id of this ReferenceFilterBasedChoiceReferenceFilter.


        :param filter_id: The filter_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: int
        """

        self._filter_id = filter_id

    @property
    def filter_status_id(self):
        """Gets the filter_status_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The filter_status_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: int
        """
        return self._filter_status_id

    @filter_status_id.setter
    def filter_status_id(self, filter_status_id):
        """Sets the filter_status_id of this ReferenceFilterBasedChoiceReferenceFilter.


        :param filter_status_id: The filter_status_id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: int
        """

        self._filter_status_id = filter_status_id

    @property
    def id(self):
        """Gets the id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReferenceFilterBasedChoiceReferenceFilter.


        :param id: The id of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def target_ids(self):
        """Gets the target_ids of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The target_ids of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        """Sets the target_ids of this ReferenceFilterBasedChoiceReferenceFilter.


        :param target_ids: The target_ids of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: list[int]
        """

        self._target_ids = target_ids

    @property
    def target_permissions(self):
        """Gets the target_permissions of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501


        :return: The target_permissions of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_permissions

    @target_permissions.setter
    def target_permissions(self, target_permissions):
        """Sets the target_permissions of this ReferenceFilterBasedChoiceReferenceFilter.


        :param target_permissions: The target_permissions of this ReferenceFilterBasedChoiceReferenceFilter.  # noqa: E501
        :type: list[str]
        """

        self._target_permissions = target_permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReferenceFilterBasedChoiceReferenceFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReferenceFilterBasedChoiceReferenceFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
