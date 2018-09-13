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


class TimeSeriesAggregateStatistics(object):
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
        'count': 'int',
        'cross_entity_metadata': 'TimeSeriesCrossEntityMetadata',
        'max': 'float',
        'max_time': 'int',
        'mean': 'float',
        'min': 'float',
        'min_time': 'int',
        'sample_time': 'int',
        'sample_value': 'float',
        'std_dev': 'float'
    }

    attribute_map = {
        'count': 'count',
        'cross_entity_metadata': 'crossEntityMetadata',
        'max': 'max',
        'max_time': 'maxTime',
        'mean': 'mean',
        'min': 'min',
        'min_time': 'minTime',
        'sample_time': 'sampleTime',
        'sample_value': 'sampleValue',
        'std_dev': 'stdDev'
    }

    def __init__(self, count=None, cross_entity_metadata=None, max=None, max_time=None, mean=None, min=None, min_time=None, sample_time=None, sample_value=None, std_dev=None):  # noqa: E501
        """TimeSeriesAggregateStatistics - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._cross_entity_metadata = None
        self._max = None
        self._max_time = None
        self._mean = None
        self._min = None
        self._min_time = None
        self._sample_time = None
        self._sample_value = None
        self._std_dev = None
        self.discriminator = None

        self.count = count
        if cross_entity_metadata is not None:
            self.cross_entity_metadata = cross_entity_metadata
        self.max = max
        self.max_time = max_time
        self.mean = mean
        self.min = min
        self.min_time = min_time
        self.sample_time = sample_time
        self.sample_value = sample_value
        self.std_dev = std_dev

    @property
    def count(self):
        """Gets the count of this TimeSeriesAggregateStatistics.  # noqa: E501

        Count  # noqa: E501

        :return: The count of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TimeSeriesAggregateStatistics.

        Count  # noqa: E501

        :param count: The count of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def cross_entity_metadata(self):
        """Gets the cross_entity_metadata of this TimeSeriesAggregateStatistics.  # noqa: E501

        Cross-entity metadata  # noqa: E501

        :return: The cross_entity_metadata of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: TimeSeriesCrossEntityMetadata
        """
        return self._cross_entity_metadata

    @cross_entity_metadata.setter
    def cross_entity_metadata(self, cross_entity_metadata):
        """Sets the cross_entity_metadata of this TimeSeriesAggregateStatistics.

        Cross-entity metadata  # noqa: E501

        :param cross_entity_metadata: The cross_entity_metadata of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: TimeSeriesCrossEntityMetadata
        """

        self._cross_entity_metadata = cross_entity_metadata

    @property
    def max(self):
        """Gets the max of this TimeSeriesAggregateStatistics.  # noqa: E501

        Maximum value  # noqa: E501

        :return: The max of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this TimeSeriesAggregateStatistics.

        Maximum value  # noqa: E501

        :param max: The max of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def max_time(self):
        """Gets the max_time of this TimeSeriesAggregateStatistics.  # noqa: E501

        Timestamp for maximum value  # noqa: E501

        :return: The max_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: int
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        """Sets the max_time of this TimeSeriesAggregateStatistics.

        Timestamp for maximum value  # noqa: E501

        :param max_time: The max_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: int
        """
        if max_time is None:
            raise ValueError("Invalid value for `max_time`, must not be `None`")  # noqa: E501

        self._max_time = max_time

    @property
    def mean(self):
        """Gets the mean of this TimeSeriesAggregateStatistics.  # noqa: E501

        Mean  # noqa: E501

        :return: The mean of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this TimeSeriesAggregateStatistics.

        Mean  # noqa: E501

        :param mean: The mean of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: float
        """
        if mean is None:
            raise ValueError("Invalid value for `mean`, must not be `None`")  # noqa: E501

        self._mean = mean

    @property
    def min(self):
        """Gets the min of this TimeSeriesAggregateStatistics.  # noqa: E501

        Minimum value  # noqa: E501

        :return: The min of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this TimeSeriesAggregateStatistics.

        Minimum value  # noqa: E501

        :param min: The min of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def min_time(self):
        """Gets the min_time of this TimeSeriesAggregateStatistics.  # noqa: E501

        Timestamp for minimum value  # noqa: E501

        :return: The min_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: int
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time):
        """Sets the min_time of this TimeSeriesAggregateStatistics.

        Timestamp for minimum value  # noqa: E501

        :param min_time: The min_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: int
        """
        if min_time is None:
            raise ValueError("Invalid value for `min_time`, must not be `None`")  # noqa: E501

        self._min_time = min_time

    @property
    def sample_time(self):
        """Gets the sample_time of this TimeSeriesAggregateStatistics.  # noqa: E501

        Sample time  # noqa: E501

        :return: The sample_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: int
        """
        return self._sample_time

    @sample_time.setter
    def sample_time(self, sample_time):
        """Sets the sample_time of this TimeSeriesAggregateStatistics.

        Sample time  # noqa: E501

        :param sample_time: The sample_time of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: int
        """
        if sample_time is None:
            raise ValueError("Invalid value for `sample_time`, must not be `None`")  # noqa: E501

        self._sample_time = sample_time

    @property
    def sample_value(self):
        """Gets the sample_value of this TimeSeriesAggregateStatistics.  # noqa: E501

        Sample value  # noqa: E501

        :return: The sample_value of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: float
        """
        return self._sample_value

    @sample_value.setter
    def sample_value(self, sample_value):
        """Sets the sample_value of this TimeSeriesAggregateStatistics.

        Sample value  # noqa: E501

        :param sample_value: The sample_value of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: float
        """
        if sample_value is None:
            raise ValueError("Invalid value for `sample_value`, must not be `None`")  # noqa: E501

        self._sample_value = sample_value

    @property
    def std_dev(self):
        """Gets the std_dev of this TimeSeriesAggregateStatistics.  # noqa: E501

        Standard deviation  # noqa: E501

        :return: The std_dev of this TimeSeriesAggregateStatistics.  # noqa: E501
        :rtype: float
        """
        return self._std_dev

    @std_dev.setter
    def std_dev(self, std_dev):
        """Sets the std_dev of this TimeSeriesAggregateStatistics.

        Standard deviation  # noqa: E501

        :param std_dev: The std_dev of this TimeSeriesAggregateStatistics.  # noqa: E501
        :type: float
        """
        if std_dev is None:
            raise ValueError("Invalid value for `std_dev`, must not be `None`")  # noqa: E501

        self._std_dev = std_dev

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
        if not isinstance(other, TimeSeriesAggregateStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
