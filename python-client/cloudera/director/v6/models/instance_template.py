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


class InstanceTemplate(object):
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
        'bootstrap_script': 'str',
        'config': 'dict(str, str)',
        'image': 'str',
        'name': 'str',
        'normalize_instance': 'bool',
        'ssh_username': 'str',
        'tags': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'bootstrap_script': 'bootstrapScript',
        'config': 'config',
        'image': 'image',
        'name': 'name',
        'normalize_instance': 'normalizeInstance',
        'ssh_username': 'sshUsername',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, bootstrap_script=None, config=None, image=None, name=None, normalize_instance=None, ssh_username=None, tags=None, type=None):  # noqa: E501
        """InstanceTemplate - a model defined in Swagger"""  # noqa: E501

        self._bootstrap_script = None
        self._config = None
        self._image = None
        self._name = None
        self._normalize_instance = None
        self._ssh_username = None
        self._tags = None
        self._type = None
        self.discriminator = None

        if bootstrap_script is not None:
            self.bootstrap_script = bootstrap_script
        if config is not None:
            self.config = config
        self.image = image
        self.name = name
        if normalize_instance is not None:
            self.normalize_instance = normalize_instance
        if ssh_username is not None:
            self.ssh_username = ssh_username
        if tags is not None:
            self.tags = tags
        self.type = type

    @property
    def bootstrap_script(self):
        """Gets the bootstrap_script of this InstanceTemplate.  # noqa: E501

        Custom script executed before anything else  # noqa: E501

        :return: The bootstrap_script of this InstanceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._bootstrap_script

    @bootstrap_script.setter
    def bootstrap_script(self, bootstrap_script):
        """Sets the bootstrap_script of this InstanceTemplate.

        Custom script executed before anything else  # noqa: E501

        :param bootstrap_script: The bootstrap_script of this InstanceTemplate.  # noqa: E501
        :type: str
        """

        self._bootstrap_script = bootstrap_script

    @property
    def config(self):
        """Gets the config of this InstanceTemplate.  # noqa: E501

        Instance configuration properties  # noqa: E501

        :return: The config of this InstanceTemplate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this InstanceTemplate.

        Instance configuration properties  # noqa: E501

        :param config: The config of this InstanceTemplate.  # noqa: E501
        :type: dict(str, str)
        """

        self._config = config

    @property
    def image(self):
        """Gets the image of this InstanceTemplate.  # noqa: E501

        Operating system image  # noqa: E501

        :return: The image of this InstanceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this InstanceTemplate.

        Operating system image  # noqa: E501

        :param image: The image of this InstanceTemplate.  # noqa: E501
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def name(self):
        """Gets the name of this InstanceTemplate.  # noqa: E501

        Instance template name  # noqa: E501

        :return: The name of this InstanceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceTemplate.

        Instance template name  # noqa: E501

        :param name: The name of this InstanceTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def normalize_instance(self):
        """Gets the normalize_instance of this InstanceTemplate.  # noqa: E501

        Flag indicating whether to normalize the instance  # noqa: E501

        :return: The normalize_instance of this InstanceTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_instance

    @normalize_instance.setter
    def normalize_instance(self, normalize_instance):
        """Sets the normalize_instance of this InstanceTemplate.

        Flag indicating whether to normalize the instance  # noqa: E501

        :param normalize_instance: The normalize_instance of this InstanceTemplate.  # noqa: E501
        :type: bool
        """

        self._normalize_instance = normalize_instance

    @property
    def ssh_username(self):
        """Gets the ssh_username of this InstanceTemplate.  # noqa: E501

        Optional SSH username to override username specified in environment  # noqa: E501

        :return: The ssh_username of this InstanceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._ssh_username

    @ssh_username.setter
    def ssh_username(self, ssh_username):
        """Sets the ssh_username of this InstanceTemplate.

        Optional SSH username to override username specified in environment  # noqa: E501

        :param ssh_username: The ssh_username of this InstanceTemplate.  # noqa: E501
        :type: str
        """

        self._ssh_username = ssh_username

    @property
    def tags(self):
        """Gets the tags of this InstanceTemplate.  # noqa: E501

        Instance tags  # noqa: E501

        :return: The tags of this InstanceTemplate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceTemplate.

        Instance tags  # noqa: E501

        :param tags: The tags of this InstanceTemplate.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this InstanceTemplate.  # noqa: E501

        Instance type  # noqa: E501

        :return: The type of this InstanceTemplate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InstanceTemplate.

        Instance type  # noqa: E501

        :param type: The type of this InstanceTemplate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
