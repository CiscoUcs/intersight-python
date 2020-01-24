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


class UcsdBackupInfoAllOf(object):
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
        'backup_file_name': 'str',
        'backup_location': 'str',
        'backup_server_ip': 'str',
        'backup_size': 'int',
        'connectors': 'list[UcsdConnectorPack]',
        'duration': 'int',
        'encryption_key': 'str',
        'failure_reason': 'str',
        'is_purged': 'bool',
        'last_modified': 'datetime',
        'percentage_completion': 'int',
        'product_version': 'str',
        'protocol': 'str',
        'stage_completion': 'str',
        'start_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'backup_file_name': 'BackupFileName',
        'backup_location': 'BackupLocation',
        'backup_server_ip': 'BackupServerIp',
        'backup_size': 'BackupSize',
        'connectors': 'Connectors',
        'duration': 'Duration',
        'encryption_key': 'EncryptionKey',
        'failure_reason': 'FailureReason',
        'is_purged': 'IsPurged',
        'last_modified': 'LastModified',
        'percentage_completion': 'PercentageCompletion',
        'product_version': 'ProductVersion',
        'protocol': 'Protocol',
        'stage_completion': 'StageCompletion',
        'start_time': 'StartTime',
        'status': 'Status'
    }

    def __init__(self,
                 backup_file_name=None,
                 backup_location=None,
                 backup_server_ip=None,
                 backup_size=None,
                 connectors=None,
                 duration=None,
                 encryption_key=None,
                 failure_reason=None,
                 is_purged=None,
                 last_modified=None,
                 percentage_completion=None,
                 product_version=None,
                 protocol=None,
                 stage_completion=None,
                 start_time=None,
                 status=None,
                 local_vars_configuration=None):  # noqa: E501
        """UcsdBackupInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._backup_file_name = None
        self._backup_location = None
        self._backup_server_ip = None
        self._backup_size = None
        self._connectors = None
        self._duration = None
        self._encryption_key = None
        self._failure_reason = None
        self._is_purged = None
        self._last_modified = None
        self._percentage_completion = None
        self._product_version = None
        self._protocol = None
        self._stage_completion = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        if backup_file_name is not None:
            self.backup_file_name = backup_file_name
        if backup_location is not None:
            self.backup_location = backup_location
        if backup_server_ip is not None:
            self.backup_server_ip = backup_server_ip
        if backup_size is not None:
            self.backup_size = backup_size
        if connectors is not None:
            self.connectors = connectors
        if duration is not None:
            self.duration = duration
        if encryption_key is not None:
            self.encryption_key = encryption_key
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if is_purged is not None:
            self.is_purged = is_purged
        if last_modified is not None:
            self.last_modified = last_modified
        if percentage_completion is not None:
            self.percentage_completion = percentage_completion
        if product_version is not None:
            self.product_version = product_version
        if protocol is not None:
            self.protocol = protocol
        if stage_completion is not None:
            self.stage_completion = stage_completion
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status

    @property
    def backup_file_name(self):
        """Gets the backup_file_name of this UcsdBackupInfoAllOf.  # noqa: E501

        Auto generated backup File Name with combination of file prefix given an user input and the timestamp.    # noqa: E501

        :return: The backup_file_name of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """Sets the backup_file_name of this UcsdBackupInfoAllOf.

        Auto generated backup File Name with combination of file prefix given an user input and the timestamp.    # noqa: E501

        :param backup_file_name: The backup_file_name of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._backup_file_name = backup_file_name

    @property
    def backup_location(self):
        """Gets the backup_location of this UcsdBackupInfoAllOf.  # noqa: E501

        Backup location that contains the backup images for end device which can be used for restore operation.    # noqa: E501

        :return: The backup_location of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """Sets the backup_location of this UcsdBackupInfoAllOf.

        Backup location that contains the backup images for end device which can be used for restore operation.    # noqa: E501

        :param backup_location: The backup_location of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._backup_location = backup_location

    @property
    def backup_server_ip(self):
        """Gets the backup_server_ip of this UcsdBackupInfoAllOf.  # noqa: E501

        Backup server where backup images are maintained.    # noqa: E501

        :return: The backup_server_ip of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._backup_server_ip

    @backup_server_ip.setter
    def backup_server_ip(self, backup_server_ip):
        """Sets the backup_server_ip of this UcsdBackupInfoAllOf.

        Backup server where backup images are maintained.    # noqa: E501

        :param backup_server_ip: The backup_server_ip of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._backup_server_ip = backup_server_ip

    @property
    def backup_size(self):
        """Gets the backup_size of this UcsdBackupInfoAllOf.  # noqa: E501

        Size of the backup image in bytes.    # noqa: E501

        :return: The backup_size of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """Sets the backup_size of this UcsdBackupInfoAllOf.

        Size of the backup image in bytes.    # noqa: E501

        :param backup_size: The backup_size of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: int
        """

        self._backup_size = backup_size

    @property
    def connectors(self):
        """Gets the connectors of this UcsdBackupInfoAllOf.  # noqa: E501


        :return: The connectors of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: list[UcsdConnectorPack]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """Sets the connectors of this UcsdBackupInfoAllOf.


        :param connectors: The connectors of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: list[UcsdConnectorPack]
        """

        self._connectors = connectors

    @property
    def duration(self):
        """Gets the duration of this UcsdBackupInfoAllOf.  # noqa: E501

        Time taken for the backup to be completed.    # noqa: E501

        :return: The duration of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UcsdBackupInfoAllOf.

        Time taken for the backup to be completed.    # noqa: E501

        :param duration: The duration of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def encryption_key(self):
        """Gets the encryption_key of this UcsdBackupInfoAllOf.  # noqa: E501

        The key used for encrypting the backup file.    # noqa: E501

        :return: The encryption_key of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """Sets the encryption_key of this UcsdBackupInfoAllOf.

        The key used for encrypting the backup file.    # noqa: E501

        :param encryption_key: The encryption_key of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._encryption_key = encryption_key

    @property
    def failure_reason(self):
        """Gets the failure_reason of this UcsdBackupInfoAllOf.  # noqa: E501

        Reason for backup failure.    # noqa: E501

        :return: The failure_reason of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this UcsdBackupInfoAllOf.

        Reason for backup failure.    # noqa: E501

        :param failure_reason: The failure_reason of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def is_purged(self):
        """Gets the is_purged of this UcsdBackupInfoAllOf.  # noqa: E501

        Backup image got purged or not. The backup images get purged based on the retention count set by the user in the backup config policy.    # noqa: E501

        :return: The is_purged of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_purged

    @is_purged.setter
    def is_purged(self, is_purged):
        """Sets the is_purged of this UcsdBackupInfoAllOf.

        Backup image got purged or not. The backup images get purged based on the retention count set by the user in the backup config policy.    # noqa: E501

        :param is_purged: The is_purged of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: bool
        """

        self._is_purged = is_purged

    @property
    def last_modified(self):
        """Gets the last_modified of this UcsdBackupInfoAllOf.  # noqa: E501

        Last modified time when this backup record got updated.    # noqa: E501

        :return: The last_modified of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UcsdBackupInfoAllOf.

        Last modified time when this backup record got updated.    # noqa: E501

        :param last_modified: The last_modified of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def percentage_completion(self):
        """Gets the percentage_completion of this UcsdBackupInfoAllOf.  # noqa: E501

        Backup current precentage completion status information.    # noqa: E501

        :return: The percentage_completion of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: int
        """
        return self._percentage_completion

    @percentage_completion.setter
    def percentage_completion(self, percentage_completion):
        """Sets the percentage_completion of this UcsdBackupInfoAllOf.

        Backup current precentage completion status information.    # noqa: E501

        :param percentage_completion: The percentage_completion of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: int
        """

        self._percentage_completion = percentage_completion

    @property
    def product_version(self):
        """Gets the product_version of this UcsdBackupInfoAllOf.  # noqa: E501

        The end device product version when the backup image was taken.    # noqa: E501

        :return: The product_version of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this UcsdBackupInfoAllOf.

        The end device product version when the backup image was taken.    # noqa: E501

        :param product_version: The product_version of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._product_version = product_version

    @property
    def protocol(self):
        """Gets the protocol of this UcsdBackupInfoAllOf.  # noqa: E501

        Protocol used for the remote backup. possible values are FTP, SCP and SFTP. Not applicable for the localhost (127.0.0.1).    # noqa: E501

        :return: The protocol of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UcsdBackupInfoAllOf.

        Protocol used for the remote backup. possible values are FTP, SCP and SFTP. Not applicable for the localhost (127.0.0.1).    # noqa: E501

        :param protocol: The protocol of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def stage_completion(self):
        """Gets the stage_completion of this UcsdBackupInfoAllOf.  # noqa: E501

        Backup current status stage information.    # noqa: E501

        :return: The stage_completion of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._stage_completion

    @stage_completion.setter
    def stage_completion(self, stage_completion):
        """Sets the stage_completion of this UcsdBackupInfoAllOf.

        Backup current status stage information.    # noqa: E501

        :param stage_completion: The stage_completion of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._stage_completion = stage_completion

    @property
    def start_time(self):
        """Gets the start_time of this UcsdBackupInfoAllOf.  # noqa: E501

        Start time of backup when it got initiated.    # noqa: E501

        :return: The start_time of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UcsdBackupInfoAllOf.

        Start time of backup when it got initiated.    # noqa: E501

        :param start_time: The start_time of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this UcsdBackupInfoAllOf.  # noqa: E501

        Current status of Backup current.     # noqa: E501

        :return: The status of this UcsdBackupInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UcsdBackupInfoAllOf.

        Current status of Backup current.     # noqa: E501

        :param status: The status of this UcsdBackupInfoAllOf.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, UcsdBackupInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UcsdBackupInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
