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


class WorkflowTaskInfo(object):
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
        'end_time': 'datetime',
        'failure_reason': 'str',
        'input': 'object',
        'inst_id': 'str',
        'internal': 'bool',
        'label': 'str',
        'message': 'list[WorkflowMessage]',
        'name': 'str',
        'output': 'object',
        'ref_name': 'str',
        'retry_count': 'int',
        'start_time': 'datetime',
        'status': 'str',
        'task_inst_id_list': 'list[WorkflowTaskRetryInfo]',
        'sub_workflow_info': 'WorkflowWorkflowInfo',
        'task_definition': 'WorkflowTaskDefinition',
        'workflow_info': 'WorkflowWorkflowInfo'
    }

    attribute_map = {
        'description': 'Description',
        'end_time': 'EndTime',
        'failure_reason': 'FailureReason',
        'input': 'Input',
        'inst_id': 'InstId',
        'internal': 'Internal',
        'label': 'Label',
        'message': 'Message',
        'name': 'Name',
        'output': 'Output',
        'ref_name': 'RefName',
        'retry_count': 'RetryCount',
        'start_time': 'StartTime',
        'status': 'Status',
        'task_inst_id_list': 'TaskInstIdList',
        'sub_workflow_info': 'SubWorkflowInfo',
        'task_definition': 'TaskDefinition',
        'workflow_info': 'WorkflowInfo'
    }

    def __init__(self,
                 description=None,
                 end_time=None,
                 failure_reason=None,
                 input=None,
                 inst_id=None,
                 internal=None,
                 label=None,
                 message=None,
                 name=None,
                 output=None,
                 ref_name=None,
                 retry_count=None,
                 start_time=None,
                 status=None,
                 task_inst_id_list=None,
                 sub_workflow_info=None,
                 task_definition=None,
                 workflow_info=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowTaskInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._end_time = None
        self._failure_reason = None
        self._input = None
        self._inst_id = None
        self._internal = None
        self._label = None
        self._message = None
        self._name = None
        self._output = None
        self._ref_name = None
        self._retry_count = None
        self._start_time = None
        self._status = None
        self._task_inst_id_list = None
        self._sub_workflow_info = None
        self._task_definition = None
        self._workflow_info = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if end_time is not None:
            self.end_time = end_time
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if input is not None:
            self.input = input
        if inst_id is not None:
            self.inst_id = inst_id
        if internal is not None:
            self.internal = internal
        if label is not None:
            self.label = label
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if output is not None:
            self.output = output
        if ref_name is not None:
            self.ref_name = ref_name
        if retry_count is not None:
            self.retry_count = retry_count
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if task_inst_id_list is not None:
            self.task_inst_id_list = task_inst_id_list
        if sub_workflow_info is not None:
            self.sub_workflow_info = sub_workflow_info
        if task_definition is not None:
            self.task_definition = task_definition
        if workflow_info is not None:
            self.workflow_info = workflow_info

    @property
    def description(self):
        """Gets the description of this WorkflowTaskInfo.  # noqa: E501

        The task description and this is the description that was added when the task was included into the workflow.    # noqa: E501

        :return: The description of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowTaskInfo.

        The task description and this is the description that was added when the task was included into the workflow.    # noqa: E501

        :param description: The description of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this WorkflowTaskInfo.  # noqa: E501

        The time stamp when the task reached a final state.    # noqa: E501

        :return: The end_time of this WorkflowTaskInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WorkflowTaskInfo.

        The time stamp when the task reached a final state.    # noqa: E501

        :param end_time: The end_time of this WorkflowTaskInfo.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def failure_reason(self):
        """Gets the failure_reason of this WorkflowTaskInfo.  # noqa: E501

        Description of the reason why the task failed.    # noqa: E501

        :return: The failure_reason of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this WorkflowTaskInfo.

        Description of the reason why the task failed.    # noqa: E501

        :param failure_reason: The failure_reason of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def input(self):
        """Gets the input of this WorkflowTaskInfo.  # noqa: E501

        The input data that was sent to the task at the start of execution.    # noqa: E501

        :return: The input of this WorkflowTaskInfo.  # noqa: E501
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this WorkflowTaskInfo.

        The input data that was sent to the task at the start of execution.    # noqa: E501

        :param input: The input of this WorkflowTaskInfo.  # noqa: E501
        :type: object
        """

        self._input = input

    @property
    def inst_id(self):
        """Gets the inst_id of this WorkflowTaskInfo.  # noqa: E501

        The current running task instance Id.    # noqa: E501

        :return: The inst_id of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        """Sets the inst_id of this WorkflowTaskInfo.

        The current running task instance Id.    # noqa: E501

        :param inst_id: The inst_id of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._inst_id = inst_id

    @property
    def internal(self):
        """Gets the internal of this WorkflowTaskInfo.  # noqa: E501

        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.    # noqa: E501

        :return: The internal of this WorkflowTaskInfo.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this WorkflowTaskInfo.

        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.    # noqa: E501

        :param internal: The internal of this WorkflowTaskInfo.  # noqa: E501
        :type: bool
        """

        self._internal = internal

    @property
    def label(self):
        """Gets the label of this WorkflowTaskInfo.  # noqa: E501

        User friendly short label to describe this task instance in the workflow.    # noqa: E501

        :return: The label of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this WorkflowTaskInfo.

        User friendly short label to describe this task instance in the workflow.    # noqa: E501

        :param label: The label of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def message(self):
        """Gets the message of this WorkflowTaskInfo.  # noqa: E501


        :return: The message of this WorkflowTaskInfo.  # noqa: E501
        :rtype: list[WorkflowMessage]
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WorkflowTaskInfo.


        :param message: The message of this WorkflowTaskInfo.  # noqa: E501
        :type: list[WorkflowMessage]
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this WorkflowTaskInfo.  # noqa: E501

        Task definition name which specifies the task type.    # noqa: E501

        :return: The name of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowTaskInfo.

        Task definition name which specifies the task type.    # noqa: E501

        :param name: The name of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output(self):
        """Gets the output of this WorkflowTaskInfo.  # noqa: E501

        The output data that was generated by this task.    # noqa: E501

        :return: The output of this WorkflowTaskInfo.  # noqa: E501
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this WorkflowTaskInfo.

        The output data that was generated by this task.    # noqa: E501

        :param output: The output of this WorkflowTaskInfo.  # noqa: E501
        :type: object
        """

        self._output = output

    @property
    def ref_name(self):
        """Gets the ref_name of this WorkflowTaskInfo.  # noqa: E501

        The task reference name to ensure its unique inside a workflow.    # noqa: E501

        :return: The ref_name of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this WorkflowTaskInfo.

        The task reference name to ensure its unique inside a workflow.    # noqa: E501

        :param ref_name: The ref_name of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._ref_name = ref_name

    @property
    def retry_count(self):
        """Gets the retry_count of this WorkflowTaskInfo.  # noqa: E501

        A counter for number of retries.    # noqa: E501

        :return: The retry_count of this WorkflowTaskInfo.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this WorkflowTaskInfo.

        A counter for number of retries.    # noqa: E501

        :param retry_count: The retry_count of this WorkflowTaskInfo.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def start_time(self):
        """Gets the start_time of this WorkflowTaskInfo.  # noqa: E501

        The time stamp when the task started execution.    # noqa: E501

        :return: The start_time of this WorkflowTaskInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WorkflowTaskInfo.

        The time stamp when the task started execution.    # noqa: E501

        :param start_time: The start_time of this WorkflowTaskInfo.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this WorkflowTaskInfo.  # noqa: E501

        The status of the task and this will specify if the task is running or has reached a final state.    # noqa: E501

        :return: The status of this WorkflowTaskInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowTaskInfo.

        The status of the task and this will specify if the task is running or has reached a final state.    # noqa: E501

        :param status: The status of this WorkflowTaskInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def task_inst_id_list(self):
        """Gets the task_inst_id_list of this WorkflowTaskInfo.  # noqa: E501


        :return: The task_inst_id_list of this WorkflowTaskInfo.  # noqa: E501
        :rtype: list[WorkflowTaskRetryInfo]
        """
        return self._task_inst_id_list

    @task_inst_id_list.setter
    def task_inst_id_list(self, task_inst_id_list):
        """Sets the task_inst_id_list of this WorkflowTaskInfo.


        :param task_inst_id_list: The task_inst_id_list of this WorkflowTaskInfo.  # noqa: E501
        :type: list[WorkflowTaskRetryInfo]
        """

        self._task_inst_id_list = task_inst_id_list

    @property
    def sub_workflow_info(self):
        """Gets the sub_workflow_info of this WorkflowTaskInfo.  # noqa: E501


        :return: The sub_workflow_info of this WorkflowTaskInfo.  # noqa: E501
        :rtype: WorkflowWorkflowInfo
        """
        return self._sub_workflow_info

    @sub_workflow_info.setter
    def sub_workflow_info(self, sub_workflow_info):
        """Sets the sub_workflow_info of this WorkflowTaskInfo.


        :param sub_workflow_info: The sub_workflow_info of this WorkflowTaskInfo.  # noqa: E501
        :type: WorkflowWorkflowInfo
        """

        self._sub_workflow_info = sub_workflow_info

    @property
    def task_definition(self):
        """Gets the task_definition of this WorkflowTaskInfo.  # noqa: E501


        :return: The task_definition of this WorkflowTaskInfo.  # noqa: E501
        :rtype: WorkflowTaskDefinition
        """
        return self._task_definition

    @task_definition.setter
    def task_definition(self, task_definition):
        """Sets the task_definition of this WorkflowTaskInfo.


        :param task_definition: The task_definition of this WorkflowTaskInfo.  # noqa: E501
        :type: WorkflowTaskDefinition
        """

        self._task_definition = task_definition

    @property
    def workflow_info(self):
        """Gets the workflow_info of this WorkflowTaskInfo.  # noqa: E501


        :return: The workflow_info of this WorkflowTaskInfo.  # noqa: E501
        :rtype: WorkflowWorkflowInfo
        """
        return self._workflow_info

    @workflow_info.setter
    def workflow_info(self, workflow_info):
        """Sets the workflow_info of this WorkflowTaskInfo.


        :param workflow_info: The workflow_info of this WorkflowTaskInfo.  # noqa: E501
        :type: WorkflowWorkflowInfo
        """

        self._workflow_info = workflow_info

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
        if not isinstance(other, WorkflowTaskInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowTaskInfo):
            return True

        return self.to_dict() != other.to_dict()
