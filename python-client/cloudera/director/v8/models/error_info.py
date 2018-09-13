# coding: utf-8

"""
Licensed to Cloudera, Inc. under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import pprint
import re  # noqa: F401

import six


class ErrorInfo(object):
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
        'error_code': 'str',
        'error_type': 'str',
        'properties': 'dict(str, str)',
        'retryable': 'bool'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_type': 'errorType',
        'properties': 'properties',
        'retryable': 'retryable'
    }

    def __init__(self, error_code=None, error_type=None, properties=None, retryable=None):  # noqa: E501
        """ErrorInfo - a model defined in Swagger"""  # noqa: E501

        self._error_code = None
        self._error_type = None
        self._properties = None
        self._retryable = None
        self.discriminator = None

        self.error_code = error_code
        self.error_type = error_type
        self.properties = properties
        self.retryable = retryable

    @property
    def error_code(self):
        """Gets the error_code of this ErrorInfo.  # noqa: E501

        Error code  # noqa: E501

        :return: The error_code of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ErrorInfo.

        Error code  # noqa: E501

        :param error_code: The error_code of this ErrorInfo.  # noqa: E501
        :type: str
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501
        allowed_values = ["CLUSTER_DEPLOYMENT_IN_WRONG_STAGE", "CLUSTER_DEPLOYMENT_FAIL", "CLUSTER_GET_PARCEL_FAIL", "CLUSTER_MISSING_PRODUCT_PARCEL", "CLUSTER_PARCEL_VALIDATION_FAIL", "CLUSTER_UNSUPPORTED_UPDATE_STEP", "CLUSTER_RESTART_FAIL", "CM_AGENT_INSTALLATION_FAIL", "CM_BAD_REQUEST", "CM_CMD_FAIL", "CM_ILLEGAL_API_VERSION", "CM_ILLEGAL_ARGUMENT", "CM_REPO_EMPTY_URL", "CM_REPO_MULTIPLE_URL", "CM_UNAUTHORIZED_OPERATION", "CM_UNSUPPORTED_OPERATION", "CM_UNSUPPORTED_SERVICE_VERSIONS", "CM_REDEPLOY_CLIENT_CONFIGS_FAIL", "CM_IMPORT_KERBEROS_MISSING_PRINCIPAL", "CM_IMPORT_KERBEROS_INCORRECT_PASSWORD", "CM_SERVICE_HOST_NOT_FOUND", "CM_SERVICE_READ_ERROR", "CM_SERVICE_WRONG_STATE_FOR_DELETION", "CM_SERVICE_DB_AND_TEMPLATE_MISSING", "CM_FAIL_TRIGGER_FIRSTRUN", "CM_FIRSTRUN_AUTH_FAIL", "CM_FIRSTRUN_IO_ERROR", "CM_FIRSTRUN_BAD_RESPONSE", "DB_SERVER_CREATION_FAIL", "DB_SERVER_IN_FAILURE_STAGE", "DB_SERVER_MISSING", "DB_SERVER_NOT_READY", "DB_SERVER_PROVIDER_RETRIEVAL_FAIL", "DB_SERVER_TEMPLATE_EXIST", "INSTANCE_DNS_MISCONFIGURED", "INSTANCE_MISSING_CAPABILITIES", "INSTANCE_MISSING_FQDN", "INSTANCE_NOT_FOUND", "INSTANCE_SSH_CONNECTION_FAIL", "INSTANCE_ALLOCATION_TIME_OUT", "INSTANCE_ALLOCATION_ILLEGAL_ARGUMENT", "INSTANCE_ALLOCATION_ILLEGAL_STATE", "INSTANCE_ROOT_PARTITION_RESIZE_FAIL", "INSTANCE_TERMINATION_FAIL", "JOB_CANCELLATION_FAIL", "JOB_CANCELLATION_TIMEOUT", "JOB_EXECUTION_FAIL", "JOB_COMBINATION_INVALID_MAP_ENTRY", "JOB_COMBINATION_DUPLICATE_ENTRIES", "JOB_CREATION_FAIL", "RUN_SCRIPT_FAIL", "SSH_BACKGROUND_COMMAND_FAIL", "SSH_JOB_MISSING_BACKGROUND_PROCESS_STATE_FILE", "UNDEFINED"]  # noqa: E501
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def error_type(self):
        """Gets the error_type of this ErrorInfo.  # noqa: E501

        Error type  # noqa: E501

        :return: The error_type of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this ErrorInfo.

        Error type  # noqa: E501

        :param error_type: The error_type of this ErrorInfo.  # noqa: E501
        :type: str
        """
        if error_type is None:
            raise ValueError("Invalid value for `error_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CLIENT", "SERVICE", "UNKNOWN"]  # noqa: E501
        if error_type not in allowed_values:
            raise ValueError(
                "Invalid value for `error_type` ({0}), must be one of {1}"  # noqa: E501
                .format(error_type, allowed_values)
            )

        self._error_type = error_type

    @property
    def properties(self):
        """Gets the properties of this ErrorInfo.  # noqa: E501

        Properties associated with the error  # noqa: E501

        :return: The properties of this ErrorInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ErrorInfo.

        Properties associated with the error  # noqa: E501

        :param properties: The properties of this ErrorInfo.  # noqa: E501
        :type: dict(str, str)
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def retryable(self):
        """Gets the retryable of this ErrorInfo.  # noqa: E501

        Whether the operation that produced this error is retryable  # noqa: E501

        :return: The retryable of this ErrorInfo.  # noqa: E501
        :rtype: bool
        """
        return self._retryable

    @retryable.setter
    def retryable(self, retryable):
        """Sets the retryable of this ErrorInfo.

        Whether the operation that produced this error is retryable  # noqa: E501

        :param retryable: The retryable of this ErrorInfo.  # noqa: E501
        :type: bool
        """
        if retryable is None:
            raise ValueError("Invalid value for `retryable`, must not be `None`")  # noqa: E501

        self._retryable = retryable

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
