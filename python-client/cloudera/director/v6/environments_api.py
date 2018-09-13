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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudera.director.common.client import ApiClient


class EnvironmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, environment, **kwargs):  # noqa: E501
        """Create a new environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create(environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param Environment environment: environment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_with_http_info(environment, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(environment, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, environment, **kwargs):  # noqa: E501
        """Create a new environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_with_http_info(environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param Environment environment: environment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['environment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'environment' in params:
            body_params = params['environment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, name, **kwargs):  # noqa: E501
        """Delete an environment by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, name, **kwargs):  # noqa: E501
        """Delete an environment by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_redacted(self, name, **kwargs):  # noqa: E501
        """Get an environment by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_redacted(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: Environment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_redacted_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_redacted_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_redacted_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get an environment by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_redacted_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :return: Environment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_redacted" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_redacted`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Environment',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List all environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List all environments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, name, environment, **kwargs):  # noqa: E501
        """Update an existing environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update(name, environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :param Environment environment: environment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_with_http_info(name, environment, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(name, environment, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, name, environment, **kwargs):  # noqa: E501
        """Update an existing environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_with_http_info(name, environment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :param Environment environment: environment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'environment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update`")  # noqa: E501
        # verify the required parameter 'environment' is set
        if ('environment' not in params or
                params['environment'] is None):
            raise ValueError("Missing the required parameter `environment` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'environment' in params:
            body_params = params['environment']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_provider_credentials(self, name, credentials, **kwargs):  # noqa: E501
        """Update provider credentials for a specific environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_provider_credentials(name, credentials, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :param object credentials: credentials (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_provider_credentials_with_http_info(name, credentials, **kwargs)  # noqa: E501
        else:
            (data) = self.update_provider_credentials_with_http_info(name, credentials, **kwargs)  # noqa: E501
            return data

    def update_provider_credentials_with_http_info(self, name, credentials, **kwargs):  # noqa: E501
        """Update provider credentials for a specific environment  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_provider_credentials_with_http_info(name, credentials, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: name (required)
        :param object credentials: credentials (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'credentials']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_provider_credentials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_provider_credentials`")  # noqa: E501
        # verify the required parameter 'credentials' is set
        if ('credentials' not in params or
                params['credentials'] is None):
            raise ValueError("Missing the required parameter `credentials` when calling `update_provider_credentials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credentials' in params:
            body_params = params['credentials']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/api/v6/environments/{name}/provider/credentials', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            model_package="cloudera.director.v6.models",
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
