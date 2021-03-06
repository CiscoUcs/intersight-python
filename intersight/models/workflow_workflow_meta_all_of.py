# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class WorkflowWorkflowMetaAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'str',
        'input_parameters': 'list[str]',
        'name': 'str',
        'output_parameters': 'object',
        'schema_version': 'int',
        'src': 'str',
        'tasks': 'object',
        'type': 'str',
        'version': 'int',
        'wait_on_duplicate': 'bool',
        'organization': 'OrganizationOrganization'
    }

    attribute_map = {
        'description': 'Description',
        'input_parameters': 'InputParameters',
        'name': 'Name',
        'output_parameters': 'OutputParameters',
        'schema_version': 'SchemaVersion',
        'src': 'Src',
        'tasks': 'Tasks',
        'type': 'Type',
        'version': 'Version',
        'wait_on_duplicate': 'WaitOnDuplicate',
        'organization': 'Organization'
    }

    def __init__(self,
                 description=None,
                 input_parameters=None,
                 name=None,
                 output_parameters=None,
                 schema_version=None,
                 src=None,
                 tasks=None,
                 type='SystemDefined',
                 version=None,
                 wait_on_duplicate=None,
                 organization=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowWorkflowMetaAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._input_parameters = None
        self._name = None
        self._output_parameters = None
        self._schema_version = None
        self._src = None
        self._tasks = None
        self._type = None
        self._version = None
        self._wait_on_duplicate = None
        self._organization = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if input_parameters is not None:
            self.input_parameters = input_parameters
        if name is not None:
            self.name = name
        if output_parameters is not None:
            self.output_parameters = output_parameters
        if schema_version is not None:
            self.schema_version = schema_version
        if src is not None:
            self.src = src
        if tasks is not None:
            self.tasks = tasks
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if wait_on_duplicate is not None:
            self.wait_on_duplicate = wait_on_duplicate
        if organization is not None:
            self.organization = organization

    @property
    def description(self):
        """Gets the description of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The description for the workflow.    # noqa: E501

        :return: The description of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowWorkflowMetaAllOf.

        The description for the workflow.    # noqa: E501

        :param description: The description of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def input_parameters(self):
        """Gets the input_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501


        :return: The input_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_parameters

    @input_parameters.setter
    def input_parameters(self, input_parameters):
        """Sets the input_parameters of this WorkflowWorkflowMetaAllOf.


        :param input_parameters: The input_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: list[str]
        """

        self._input_parameters = input_parameters

    @property
    def name(self):
        """Gets the name of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The name given to the workflow.    # noqa: E501

        :return: The name of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowWorkflowMetaAllOf.

        The name given to the workflow.    # noqa: E501

        :param name: The name of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output_parameters(self):
        """Gets the output_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The workflow output parameters.    # noqa: E501

        :return: The output_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: object
        """
        return self._output_parameters

    @output_parameters.setter
    def output_parameters(self, output_parameters):
        """Sets the output_parameters of this WorkflowWorkflowMetaAllOf.

        The workflow output parameters.    # noqa: E501

        :param output_parameters: The output_parameters of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: object
        """

        self._output_parameters = output_parameters

    @property
    def schema_version(self):
        """Gets the schema_version of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The Conductor schema version that decides what attribute can be supported.    # noqa: E501

        :return: The schema_version of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: int
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this WorkflowWorkflowMetaAllOf.

        The Conductor schema version that decides what attribute can be supported.    # noqa: E501

        :param schema_version: The schema_version of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: int
        """

        self._schema_version = schema_version

    @property
    def src(self):
        """Gets the src of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The src is workflow owner service.    # noqa: E501

        :return: The src of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this WorkflowWorkflowMetaAllOf.

        The src is workflow owner service.    # noqa: E501

        :param src: The src of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: str
        """

        self._src = src

    @property
    def tasks(self):
        """Gets the tasks of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The tasks contained inside of the workflow.    # noqa: E501

        :return: The tasks of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: object
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this WorkflowWorkflowMetaAllOf.

        The tasks contained inside of the workflow.    # noqa: E501

        :param tasks: The tasks of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: object
        """

        self._tasks = tasks

    @property
    def type(self):
        """Gets the type of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The type of workflow definition.    # noqa: E501

        :return: The type of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WorkflowWorkflowMetaAllOf.

        The type of workflow definition.    # noqa: E501

        :param type: The type of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["SystemDefined", "UserDefined",
                          "Dynamic"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

    @property
    def version(self):
        """Gets the version of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        The version for the workflow so we can support multiple versions for the same workflow name.    # noqa: E501

        :return: The version of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkflowWorkflowMetaAllOf.

        The version for the workflow so we can support multiple versions for the same workflow name.    # noqa: E501

        :param version: The version of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def wait_on_duplicate(self):
        """Gets the wait_on_duplicate of this WorkflowWorkflowMetaAllOf.  # noqa: E501

        Parameter decides if workflows will wait for a duplicate to finish before starting a new one.     # noqa: E501

        :return: The wait_on_duplicate of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._wait_on_duplicate

    @wait_on_duplicate.setter
    def wait_on_duplicate(self, wait_on_duplicate):
        """Sets the wait_on_duplicate of this WorkflowWorkflowMetaAllOf.

        Parameter decides if workflows will wait for a duplicate to finish before starting a new one.     # noqa: E501

        :param wait_on_duplicate: The wait_on_duplicate of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: bool
        """

        self._wait_on_duplicate = wait_on_duplicate

    @property
    def organization(self):
        """Gets the organization of this WorkflowWorkflowMetaAllOf.  # noqa: E501


        :return: The organization of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this WorkflowWorkflowMetaAllOf.


        :param organization: The organization of this WorkflowWorkflowMetaAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowWorkflowMetaAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowWorkflowMetaAllOf):
            return True

        return self.to_dict() != other.to_dict()
