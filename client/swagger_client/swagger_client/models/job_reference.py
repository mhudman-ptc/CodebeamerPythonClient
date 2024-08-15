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

class JobReference(object):
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
        'job_id': 'int',
        'job_type': 'str'
    }

    attribute_map = {
        'job_id': 'jobId',
        'job_type': 'jobType'
    }

    def __init__(self, job_id=None, job_type=None):  # noqa: E501
        """JobReference - a model defined in Swagger"""  # noqa: E501
        self._job_id = None
        self._job_type = None
        self.discriminator = None
        self.job_id = job_id
        self.job_type = job_type

    @property
    def job_id(self):
        """Gets the job_id of this JobReference.  # noqa: E501

        Id of the job  # noqa: E501

        :return: The job_id of this JobReference.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobReference.

        Id of the job  # noqa: E501

        :param job_id: The job_id of this JobReference.  # noqa: E501
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this JobReference.  # noqa: E501

        Type of a background job  # noqa: E501

        :return: The job_type of this JobReference.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobReference.

        Type of a background job  # noqa: E501

        :param job_type: The job_type of this JobReference.  # noqa: E501
        :type: str
        """
        if job_type is None:
            raise ValueError("Invalid value for `job_type`, must not be `None`")  # noqa: E501
        allowed_values = ["RUN_IN_EXCEL", "MASS_TEST_SET_RUN_CREATION", "DEPENDENCY_FINDER", "ITEM_EXCEL_IMPORT", "DEPLOYMENT_EXPORT", "WORKING_SET_UPDATE", "WORKING_SET_CONFIG_UPDATE", "ITEM_MOVE", "DEPLOYMENT_IMPORT", "PDF_MERGE", "EXPORT_TO_WORD", "DOCUMENT_MERGE"]  # noqa: E501
        if job_type not in allowed_values:
            raise ValueError(
                "Invalid value for `job_type` ({0}), must be one of {1}"  # noqa: E501
                .format(job_type, allowed_values)
            )

        self._job_type = job_type

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
        if issubclass(JobReference, dict):
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
        if not isinstance(other, JobReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
