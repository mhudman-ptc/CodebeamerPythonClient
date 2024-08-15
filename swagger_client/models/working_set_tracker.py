# coding: utf-8

"""
    Codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkingSetTracker(object):
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
        'baseline': 'AbstractBaselineReferenceModel',
        'created_at': 'datetime',
        'deleted': 'bool',
        'id': 'int',
        'name': 'str',
        'shared': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'baseline': 'baseline',
        'created_at': 'createdAt',
        'deleted': 'deleted',
        'id': 'id',
        'name': 'name',
        'shared': 'shared',
        'type': 'type'
    }

    def __init__(self, baseline=None, created_at=None, deleted=None, id=None, name=None, shared=None, type=None):  # noqa: E501
        """WorkingSetTracker - a model defined in Swagger"""  # noqa: E501
        self._baseline = None
        self._created_at = None
        self._deleted = None
        self._id = None
        self._name = None
        self._shared = None
        self._type = None
        self.discriminator = None
        if baseline is not None:
            self.baseline = baseline
        if created_at is not None:
            self.created_at = created_at
        if deleted is not None:
            self.deleted = deleted
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if shared is not None:
            self.shared = shared
        if type is not None:
            self.type = type

    @property
    def baseline(self):
        """Gets the baseline of this WorkingSetTracker.  # noqa: E501


        :return: The baseline of this WorkingSetTracker.  # noqa: E501
        :rtype: AbstractBaselineReferenceModel
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        """Sets the baseline of this WorkingSetTracker.


        :param baseline: The baseline of this WorkingSetTracker.  # noqa: E501
        :type: AbstractBaselineReferenceModel
        """

        self._baseline = baseline

    @property
    def created_at(self):
        """Gets the created_at of this WorkingSetTracker.  # noqa: E501

        Date of creation (Working-Set creation date for shared trackers, the date when the branch was created for included trackers)  # noqa: E501

        :return: The created_at of this WorkingSetTracker.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkingSetTracker.

        Date of creation (Working-Set creation date for shared trackers, the date when the branch was created for included trackers)  # noqa: E501

        :param created_at: The created_at of this WorkingSetTracker.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted(self):
        """Gets the deleted of this WorkingSetTracker.  # noqa: E501

        Is the Tracker deleted or not  # noqa: E501

        :return: The deleted of this WorkingSetTracker.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this WorkingSetTracker.

        Is the Tracker deleted or not  # noqa: E501

        :param deleted: The deleted of this WorkingSetTracker.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this WorkingSetTracker.  # noqa: E501

        Id of the entity  # noqa: E501

        :return: The id of this WorkingSetTracker.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkingSetTracker.

        Id of the entity  # noqa: E501

        :param id: The id of this WorkingSetTracker.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WorkingSetTracker.  # noqa: E501

        Name of the entity  # noqa: E501

        :return: The name of this WorkingSetTracker.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkingSetTracker.

        Name of the entity  # noqa: E501

        :param name: The name of this WorkingSetTracker.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shared(self):
        """Gets the shared of this WorkingSetTracker.  # noqa: E501

        Shared in Working-Set  # noqa: E501

        :return: The shared of this WorkingSetTracker.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this WorkingSetTracker.

        Shared in Working-Set  # noqa: E501

        :param shared: The shared of this WorkingSetTracker.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def type(self):
        """Gets the type of this WorkingSetTracker.  # noqa: E501

        Type of a referenced object  # noqa: E501

        :return: The type of this WorkingSetTracker.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkingSetTracker.

        Type of a referenced object  # noqa: E501

        :param type: The type of this WorkingSetTracker.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(WorkingSetTracker, dict):
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
        if not isinstance(other, WorkingSetTracker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
