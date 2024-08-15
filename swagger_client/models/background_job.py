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

class BackgroundJob(object):
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
        'background_job_status': 'str',
        'background_job_type': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'finished_at': 'datetime',
        'id': 'int',
        'status_info': 'AbstractBackgroundJobStatusInfo',
        'steps': 'list[BackgroundJobStep]',
        'submitted_by': 'UserReference'
    }

    attribute_map = {
        'background_job_status': 'backgroundJobStatus',
        'background_job_type': 'backgroundJobType',
        'created_at': 'createdAt',
        'description': 'description',
        'finished_at': 'finishedAt',
        'id': 'id',
        'status_info': 'statusInfo',
        'steps': 'steps',
        'submitted_by': 'submittedBy'
    }

    def __init__(self, background_job_status=None, background_job_type=None, created_at=None, description=None, finished_at=None, id=None, status_info=None, steps=None, submitted_by=None):  # noqa: E501
        """BackgroundJob - a model defined in Swagger"""  # noqa: E501
        self._background_job_status = None
        self._background_job_type = None
        self._created_at = None
        self._description = None
        self._finished_at = None
        self._id = None
        self._status_info = None
        self._steps = None
        self._submitted_by = None
        self.discriminator = None
        if background_job_status is not None:
            self.background_job_status = background_job_status
        if background_job_type is not None:
            self.background_job_type = background_job_type
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if finished_at is not None:
            self.finished_at = finished_at
        if id is not None:
            self.id = id
        if status_info is not None:
            self.status_info = status_info
        if steps is not None:
            self.steps = steps
        if submitted_by is not None:
            self.submitted_by = submitted_by

    @property
    def background_job_status(self):
        """Gets the background_job_status of this BackgroundJob.  # noqa: E501

        Status of a background job  # noqa: E501

        :return: The background_job_status of this BackgroundJob.  # noqa: E501
        :rtype: str
        """
        return self._background_job_status

    @background_job_status.setter
    def background_job_status(self, background_job_status):
        """Sets the background_job_status of this BackgroundJob.

        Status of a background job  # noqa: E501

        :param background_job_status: The background_job_status of this BackgroundJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "NEW", "IN_PROGRESS", "FINISHED"]  # noqa: E501
        if background_job_status not in allowed_values:
            raise ValueError(
                "Invalid value for `background_job_status` ({0}), must be one of {1}"  # noqa: E501
                .format(background_job_status, allowed_values)
            )

        self._background_job_status = background_job_status

    @property
    def background_job_type(self):
        """Gets the background_job_type of this BackgroundJob.  # noqa: E501

        Type of job  # noqa: E501

        :return: The background_job_type of this BackgroundJob.  # noqa: E501
        :rtype: str
        """
        return self._background_job_type

    @background_job_type.setter
    def background_job_type(self, background_job_type):
        """Sets the background_job_type of this BackgroundJob.

        Type of job  # noqa: E501

        :param background_job_type: The background_job_type of this BackgroundJob.  # noqa: E501
        :type: str
        """

        self._background_job_type = background_job_type

    @property
    def created_at(self):
        """Gets the created_at of this BackgroundJob.  # noqa: E501

        Creation time of job  # noqa: E501

        :return: The created_at of this BackgroundJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BackgroundJob.

        Creation time of job  # noqa: E501

        :param created_at: The created_at of this BackgroundJob.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this BackgroundJob.  # noqa: E501

        Description of job  # noqa: E501

        :return: The description of this BackgroundJob.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackgroundJob.

        Description of job  # noqa: E501

        :param description: The description of this BackgroundJob.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def finished_at(self):
        """Gets the finished_at of this BackgroundJob.  # noqa: E501

        Completion time of job  # noqa: E501

        :return: The finished_at of this BackgroundJob.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this BackgroundJob.

        Completion time of job  # noqa: E501

        :param finished_at: The finished_at of this BackgroundJob.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this BackgroundJob.  # noqa: E501

        ID of job  # noqa: E501

        :return: The id of this BackgroundJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackgroundJob.

        ID of job  # noqa: E501

        :param id: The id of this BackgroundJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status_info(self):
        """Gets the status_info of this BackgroundJob.  # noqa: E501


        :return: The status_info of this BackgroundJob.  # noqa: E501
        :rtype: AbstractBackgroundJobStatusInfo
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this BackgroundJob.


        :param status_info: The status_info of this BackgroundJob.  # noqa: E501
        :type: AbstractBackgroundJobStatusInfo
        """

        self._status_info = status_info

    @property
    def steps(self):
        """Gets the steps of this BackgroundJob.  # noqa: E501

        Sub-steps of a job  # noqa: E501

        :return: The steps of this BackgroundJob.  # noqa: E501
        :rtype: list[BackgroundJobStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this BackgroundJob.

        Sub-steps of a job  # noqa: E501

        :param steps: The steps of this BackgroundJob.  # noqa: E501
        :type: list[BackgroundJobStep]
        """

        self._steps = steps

    @property
    def submitted_by(self):
        """Gets the submitted_by of this BackgroundJob.  # noqa: E501


        :return: The submitted_by of this BackgroundJob.  # noqa: E501
        :rtype: UserReference
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        """Sets the submitted_by of this BackgroundJob.


        :param submitted_by: The submitted_by of this BackgroundJob.  # noqa: E501
        :type: UserReference
        """

        self._submitted_by = submitted_by

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
        if issubclass(BackgroundJob, dict):
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
        if not isinstance(other, BackgroundJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
