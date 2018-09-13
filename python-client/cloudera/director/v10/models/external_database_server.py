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


class ExternalDatabaseServer(object):
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
        'hostname': 'str',
        'name': 'str',
        'password': 'str',
        'port': 'int',
        'properties': 'dict(str, str)',
        'type': 'str',
        'username': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'name': 'name',
        'password': 'password',
        'port': 'port',
        'properties': 'properties',
        'type': 'type',
        'username': 'username'
    }

    def __init__(self, hostname=None, name=None, password=None, port=None, properties=None, type=None, username=None):  # noqa: E501
        """ExternalDatabaseServer - a model defined in Swagger"""  # noqa: E501

        self._hostname = None
        self._name = None
        self._password = None
        self._port = None
        self._properties = None
        self._type = None
        self._username = None
        self.discriminator = None

        self.hostname = hostname
        self.name = name
        self.password = password
        self.port = port
        if properties is not None:
            self.properties = properties
        self.type = type
        self.username = username

    @property
    def hostname(self):
        """Gets the hostname of this ExternalDatabaseServer.  # noqa: E501

        External database server hostname  # noqa: E501

        :return: The hostname of this ExternalDatabaseServer.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ExternalDatabaseServer.

        External database server hostname  # noqa: E501

        :param hostname: The hostname of this ExternalDatabaseServer.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def name(self):
        """Gets the name of this ExternalDatabaseServer.  # noqa: E501

        External database server name  # noqa: E501

        :return: The name of this ExternalDatabaseServer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalDatabaseServer.

        External database server name  # noqa: E501

        :param name: The name of this ExternalDatabaseServer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this ExternalDatabaseServer.  # noqa: E501

        Password for administrative access to external database server [redacted on read]  # noqa: E501

        :return: The password of this ExternalDatabaseServer.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ExternalDatabaseServer.

        Password for administrative access to external database server [redacted on read]  # noqa: E501

        :param password: The password of this ExternalDatabaseServer.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def port(self):
        """Gets the port of this ExternalDatabaseServer.  # noqa: E501

        External database server port  # noqa: E501

        :return: The port of this ExternalDatabaseServer.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ExternalDatabaseServer.

        External database server port  # noqa: E501

        :param port: The port of this ExternalDatabaseServer.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def properties(self):
        """Gets the properties of this ExternalDatabaseServer.  # noqa: E501

        External database server display properties  # noqa: E501

        :return: The properties of this ExternalDatabaseServer.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ExternalDatabaseServer.

        External database server display properties  # noqa: E501

        :param properties: The properties of this ExternalDatabaseServer.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this ExternalDatabaseServer.  # noqa: E501

        External database server type  # noqa: E501

        :return: The type of this ExternalDatabaseServer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalDatabaseServer.

        External database server type  # noqa: E501

        :param type: The type of this ExternalDatabaseServer.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["POSTGRESQL", "MYSQL", "ORACLE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def username(self):
        """Gets the username of this ExternalDatabaseServer.  # noqa: E501

        User name for administrative access to external database server  # noqa: E501

        :return: The username of this ExternalDatabaseServer.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ExternalDatabaseServer.

        User name for administrative access to external database server  # noqa: E501

        :param username: The username of this ExternalDatabaseServer.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, ExternalDatabaseServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
