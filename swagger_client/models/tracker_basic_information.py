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

class TrackerBasicInformation(object):
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
        'always_use_quick_transitions': 'bool',
        'color': 'str',
        'default_layout': 'str',
        'description': 'str',
        'hidden': 'bool',
        'inbox_id': 'int',
        'issue_type_id': 'int',
        'key': 'str',
        'locked': 'bool',
        'name': 'str',
        'only_workflow_actions_can_create_new_referring_items': 'bool',
        'project_id': 'int',
        'shared_in_working_sets': 'bool',
        'show_ancestor_items': 'bool',
        'show_descendant_items': 'bool',
        'template': 'bool',
        'template_id': 'int',
        'tracker_id': 'int',
        'workflow_is_active': 'bool'
    }

    attribute_map = {
        'always_use_quick_transitions': 'alwaysUseQuickTransitions',
        'color': 'color',
        'default_layout': 'defaultLayout',
        'description': 'description',
        'hidden': 'hidden',
        'inbox_id': 'inboxId',
        'issue_type_id': 'issueTypeId',
        'key': 'key',
        'locked': 'locked',
        'name': 'name',
        'only_workflow_actions_can_create_new_referring_items': 'onlyWorkflowActionsCanCreateNewReferringItems',
        'project_id': 'projectId',
        'shared_in_working_sets': 'sharedInWorkingSets',
        'show_ancestor_items': 'showAncestorItems',
        'show_descendant_items': 'showDescendantItems',
        'template': 'template',
        'template_id': 'templateId',
        'tracker_id': 'trackerId',
        'workflow_is_active': 'workflowIsActive'
    }

    def __init__(self, always_use_quick_transitions=None, color=None, default_layout=None, description=None, hidden=None, inbox_id=None, issue_type_id=None, key=None, locked=None, name=None, only_workflow_actions_can_create_new_referring_items=None, project_id=None, shared_in_working_sets=None, show_ancestor_items=None, show_descendant_items=None, template=None, template_id=None, tracker_id=None, workflow_is_active=None):  # noqa: E501
        """TrackerBasicInformation - a model defined in Swagger"""  # noqa: E501
        self._always_use_quick_transitions = None
        self._color = None
        self._default_layout = None
        self._description = None
        self._hidden = None
        self._inbox_id = None
        self._issue_type_id = None
        self._key = None
        self._locked = None
        self._name = None
        self._only_workflow_actions_can_create_new_referring_items = None
        self._project_id = None
        self._shared_in_working_sets = None
        self._show_ancestor_items = None
        self._show_descendant_items = None
        self._template = None
        self._template_id = None
        self._tracker_id = None
        self._workflow_is_active = None
        self.discriminator = None
        if always_use_quick_transitions is not None:
            self.always_use_quick_transitions = always_use_quick_transitions
        if color is not None:
            self.color = color
        if default_layout is not None:
            self.default_layout = default_layout
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if issue_type_id is not None:
            self.issue_type_id = issue_type_id
        if key is not None:
            self.key = key
        if locked is not None:
            self.locked = locked
        if name is not None:
            self.name = name
        if only_workflow_actions_can_create_new_referring_items is not None:
            self.only_workflow_actions_can_create_new_referring_items = only_workflow_actions_can_create_new_referring_items
        if project_id is not None:
            self.project_id = project_id
        if shared_in_working_sets is not None:
            self.shared_in_working_sets = shared_in_working_sets
        if show_ancestor_items is not None:
            self.show_ancestor_items = show_ancestor_items
        if show_descendant_items is not None:
            self.show_descendant_items = show_descendant_items
        if template is not None:
            self.template = template
        if template_id is not None:
            self.template_id = template_id
        if tracker_id is not None:
            self.tracker_id = tracker_id
        if workflow_is_active is not None:
            self.workflow_is_active = workflow_is_active

    @property
    def always_use_quick_transitions(self):
        """Gets the always_use_quick_transitions of this TrackerBasicInformation.  # noqa: E501


        :return: The always_use_quick_transitions of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._always_use_quick_transitions

    @always_use_quick_transitions.setter
    def always_use_quick_transitions(self, always_use_quick_transitions):
        """Sets the always_use_quick_transitions of this TrackerBasicInformation.


        :param always_use_quick_transitions: The always_use_quick_transitions of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._always_use_quick_transitions = always_use_quick_transitions

    @property
    def color(self):
        """Gets the color of this TrackerBasicInformation.  # noqa: E501


        :return: The color of this TrackerBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TrackerBasicInformation.


        :param color: The color of this TrackerBasicInformation.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def default_layout(self):
        """Gets the default_layout of this TrackerBasicInformation.  # noqa: E501


        :return: The default_layout of this TrackerBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._default_layout

    @default_layout.setter
    def default_layout(self, default_layout):
        """Sets the default_layout of this TrackerBasicInformation.


        :param default_layout: The default_layout of this TrackerBasicInformation.  # noqa: E501
        :type: str
        """
        allowed_values = ["TABLE", "DOCUMENT", "DOCUMENT_EDIT", "CARDBOARD", "DASHBOARD"]  # noqa: E501
        if default_layout not in allowed_values:
            raise ValueError(
                "Invalid value for `default_layout` ({0}), must be one of {1}"  # noqa: E501
                .format(default_layout, allowed_values)
            )

        self._default_layout = default_layout

    @property
    def description(self):
        """Gets the description of this TrackerBasicInformation.  # noqa: E501


        :return: The description of this TrackerBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrackerBasicInformation.


        :param description: The description of this TrackerBasicInformation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this TrackerBasicInformation.  # noqa: E501


        :return: The hidden of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this TrackerBasicInformation.


        :param hidden: The hidden of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def inbox_id(self):
        """Gets the inbox_id of this TrackerBasicInformation.  # noqa: E501


        :return: The inbox_id of this TrackerBasicInformation.  # noqa: E501
        :rtype: int
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this TrackerBasicInformation.


        :param inbox_id: The inbox_id of this TrackerBasicInformation.  # noqa: E501
        :type: int
        """

        self._inbox_id = inbox_id

    @property
    def issue_type_id(self):
        """Gets the issue_type_id of this TrackerBasicInformation.  # noqa: E501


        :return: The issue_type_id of this TrackerBasicInformation.  # noqa: E501
        :rtype: int
        """
        return self._issue_type_id

    @issue_type_id.setter
    def issue_type_id(self, issue_type_id):
        """Sets the issue_type_id of this TrackerBasicInformation.


        :param issue_type_id: The issue_type_id of this TrackerBasicInformation.  # noqa: E501
        :type: int
        """

        self._issue_type_id = issue_type_id

    @property
    def key(self):
        """Gets the key of this TrackerBasicInformation.  # noqa: E501


        :return: The key of this TrackerBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TrackerBasicInformation.


        :param key: The key of this TrackerBasicInformation.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def locked(self):
        """Gets the locked of this TrackerBasicInformation.  # noqa: E501


        :return: The locked of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this TrackerBasicInformation.


        :param locked: The locked of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """Gets the name of this TrackerBasicInformation.  # noqa: E501


        :return: The name of this TrackerBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackerBasicInformation.


        :param name: The name of this TrackerBasicInformation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def only_workflow_actions_can_create_new_referring_items(self):
        """Gets the only_workflow_actions_can_create_new_referring_items of this TrackerBasicInformation.  # noqa: E501


        :return: The only_workflow_actions_can_create_new_referring_items of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._only_workflow_actions_can_create_new_referring_items

    @only_workflow_actions_can_create_new_referring_items.setter
    def only_workflow_actions_can_create_new_referring_items(self, only_workflow_actions_can_create_new_referring_items):
        """Sets the only_workflow_actions_can_create_new_referring_items of this TrackerBasicInformation.


        :param only_workflow_actions_can_create_new_referring_items: The only_workflow_actions_can_create_new_referring_items of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._only_workflow_actions_can_create_new_referring_items = only_workflow_actions_can_create_new_referring_items

    @property
    def project_id(self):
        """Gets the project_id of this TrackerBasicInformation.  # noqa: E501


        :return: The project_id of this TrackerBasicInformation.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrackerBasicInformation.


        :param project_id: The project_id of this TrackerBasicInformation.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def shared_in_working_sets(self):
        """Gets the shared_in_working_sets of this TrackerBasicInformation.  # noqa: E501


        :return: The shared_in_working_sets of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._shared_in_working_sets

    @shared_in_working_sets.setter
    def shared_in_working_sets(self, shared_in_working_sets):
        """Sets the shared_in_working_sets of this TrackerBasicInformation.


        :param shared_in_working_sets: The shared_in_working_sets of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._shared_in_working_sets = shared_in_working_sets

    @property
    def show_ancestor_items(self):
        """Gets the show_ancestor_items of this TrackerBasicInformation.  # noqa: E501


        :return: The show_ancestor_items of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._show_ancestor_items

    @show_ancestor_items.setter
    def show_ancestor_items(self, show_ancestor_items):
        """Sets the show_ancestor_items of this TrackerBasicInformation.


        :param show_ancestor_items: The show_ancestor_items of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._show_ancestor_items = show_ancestor_items

    @property
    def show_descendant_items(self):
        """Gets the show_descendant_items of this TrackerBasicInformation.  # noqa: E501


        :return: The show_descendant_items of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._show_descendant_items

    @show_descendant_items.setter
    def show_descendant_items(self, show_descendant_items):
        """Sets the show_descendant_items of this TrackerBasicInformation.


        :param show_descendant_items: The show_descendant_items of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._show_descendant_items = show_descendant_items

    @property
    def template(self):
        """Gets the template of this TrackerBasicInformation.  # noqa: E501


        :return: The template of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TrackerBasicInformation.


        :param template: The template of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def template_id(self):
        """Gets the template_id of this TrackerBasicInformation.  # noqa: E501


        :return: The template_id of this TrackerBasicInformation.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TrackerBasicInformation.


        :param template_id: The template_id of this TrackerBasicInformation.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def tracker_id(self):
        """Gets the tracker_id of this TrackerBasicInformation.  # noqa: E501


        :return: The tracker_id of this TrackerBasicInformation.  # noqa: E501
        :rtype: int
        """
        return self._tracker_id

    @tracker_id.setter
    def tracker_id(self, tracker_id):
        """Sets the tracker_id of this TrackerBasicInformation.


        :param tracker_id: The tracker_id of this TrackerBasicInformation.  # noqa: E501
        :type: int
        """

        self._tracker_id = tracker_id

    @property
    def workflow_is_active(self):
        """Gets the workflow_is_active of this TrackerBasicInformation.  # noqa: E501


        :return: The workflow_is_active of this TrackerBasicInformation.  # noqa: E501
        :rtype: bool
        """
        return self._workflow_is_active

    @workflow_is_active.setter
    def workflow_is_active(self, workflow_is_active):
        """Sets the workflow_is_active of this TrackerBasicInformation.


        :param workflow_is_active: The workflow_is_active of this TrackerBasicInformation.  # noqa: E501
        :type: bool
        """

        self._workflow_is_active = workflow_is_active

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
        if issubclass(TrackerBasicInformation, dict):
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
        if not isinstance(other, TrackerBasicInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
