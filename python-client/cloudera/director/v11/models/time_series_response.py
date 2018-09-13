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


class TimeSeriesResponse(object):
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
        'time_series': 'list[TimeSeries]',
        'time_series_query': 'str',
        'warnings': 'list[str]'
    }

    attribute_map = {
        'time_series': 'timeSeries',
        'time_series_query': 'timeSeriesQuery',
        'warnings': 'warnings'
    }

    def __init__(self, time_series=None, time_series_query=None, warnings=None):  # noqa: E501
        """TimeSeriesResponse - a model defined in Swagger"""  # noqa: E501

        self._time_series = None
        self._time_series_query = None
        self._warnings = None
        self.discriminator = None

        if time_series is not None:
            self.time_series = time_series
        self.time_series_query = time_series_query
        if warnings is not None:
            self.warnings = warnings

    @property
    def time_series(self):
        """Gets the time_series of this TimeSeriesResponse.  # noqa: E501

        Time series  # noqa: E501

        :return: The time_series of this TimeSeriesResponse.  # noqa: E501
        :rtype: list[TimeSeries]
        """
        return self._time_series

    @time_series.setter
    def time_series(self, time_series):
        """Sets the time_series of this TimeSeriesResponse.

        Time series  # noqa: E501

        :param time_series: The time_series of this TimeSeriesResponse.  # noqa: E501
        :type: list[TimeSeries]
        """

        self._time_series = time_series

    @property
    def time_series_query(self):
        """Gets the time_series_query of this TimeSeriesResponse.  # noqa: E501

        Time series query  # noqa: E501

        :return: The time_series_query of this TimeSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._time_series_query

    @time_series_query.setter
    def time_series_query(self, time_series_query):
        """Sets the time_series_query of this TimeSeriesResponse.

        Time series query  # noqa: E501

        :param time_series_query: The time_series_query of this TimeSeriesResponse.  # noqa: E501
        :type: str
        """
        if time_series_query is None:
            raise ValueError("Invalid value for `time_series_query`, must not be `None`")  # noqa: E501

        self._time_series_query = time_series_query

    @property
    def warnings(self):
        """Gets the warnings of this TimeSeriesResponse.  # noqa: E501

        Warnings  # noqa: E501

        :return: The warnings of this TimeSeriesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this TimeSeriesResponse.

        Warnings  # noqa: E501

        :param warnings: The warnings of this TimeSeriesResponse.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

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
        if not isinstance(other, TimeSeriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
