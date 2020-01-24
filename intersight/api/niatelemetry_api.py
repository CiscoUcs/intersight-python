# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intersight.api_client import ApiClient
from intersight.exceptions import (ApiTypeError, ApiValueError)


class NiatelemetryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_niatelemetry_nia_inventory_by_moid(self, moid,
                                               **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_inventory_by_moid(moid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str moid: The unique Moid identifier of a resource instance. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NiatelemetryNiaInventory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_niatelemetry_nia_inventory_by_moid_with_http_info(
            moid, **kwargs)  # noqa: E501

    def get_niatelemetry_nia_inventory_by_moid_with_http_info(
            self, moid, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_inventory_by_moid_with_http_info(moid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str moid: The unique Moid identifier of a resource instance. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NiatelemetryNiaInventory, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['moid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_niatelemetry_nia_inventory_by_moid" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'moid' is set
        if self.api_client.client_side_validation and (
                'moid' not in local_var_params or  # noqa: E501
                local_var_params['moid'] is None):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `moid` when calling `get_niatelemetry_nia_inventory_by_moid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'moid' in local_var_params:
            path_params['Moid'] = local_var_params['moid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([
            'application/json', 'text/csv',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/niatelemetry/NiaInventories/{Moid}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NiatelemetryNiaInventory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_niatelemetry_nia_inventory_list(self, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_inventory_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter: Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). 
        :param str orderby: Determines what properties are used to sort the collection of resources.
        :param int top: Specifies the maximum number of resources to return in the response.
        :param int skip: Specifies the number of resources to skip in the response.
        :param str select: Specifies a subset of properties to return.
        :param str expand: Specify additional attributes or related resources to return in addition to the primary resources.
        :param str apply: Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. 
        :param bool count: The $count query specifies the service should return the count of the matching resources, instead of returning the resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response.
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NiatelemetryNiaInventoryList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_niatelemetry_nia_inventory_list_with_http_info(
            **kwargs)  # noqa: E501

    def get_niatelemetry_nia_inventory_list_with_http_info(
            self, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_inventory_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter: Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). 
        :param str orderby: Determines what properties are used to sort the collection of resources.
        :param int top: Specifies the maximum number of resources to return in the response.
        :param int skip: Specifies the number of resources to skip in the response.
        :param str select: Specifies a subset of properties to return.
        :param str expand: Specify additional attributes or related resources to return in addition to the primary resources.
        :param str apply: Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. 
        :param bool count: The $count query specifies the service should return the count of the matching resources, instead of returning the resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response.
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NiatelemetryNiaInventoryList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'filter', 'orderby', 'top', 'skip', 'select', 'expand', 'apply',
            'count', 'inlinecount', 'at'
        ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_niatelemetry_nia_inventory_list" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params and local_var_params[
                'filter'] is not None:  # noqa: E501
            query_params.append(
                ('$filter', local_var_params['filter']))  # noqa: E501
        if 'orderby' in local_var_params and local_var_params[
                'orderby'] is not None:  # noqa: E501
            query_params.append(
                ('$orderby', local_var_params['orderby']))  # noqa: E501
        if 'top' in local_var_params and local_var_params[
                'top'] is not None:  # noqa: E501
            query_params.append(
                ('$top', local_var_params['top']))  # noqa: E501
        if 'skip' in local_var_params and local_var_params[
                'skip'] is not None:  # noqa: E501
            query_params.append(
                ('$skip', local_var_params['skip']))  # noqa: E501
        if 'select' in local_var_params and local_var_params[
                'select'] is not None:  # noqa: E501
            query_params.append(
                ('$select', local_var_params['select']))  # noqa: E501
        if 'expand' in local_var_params and local_var_params[
                'expand'] is not None:  # noqa: E501
            query_params.append(
                ('$expand', local_var_params['expand']))  # noqa: E501
        if 'apply' in local_var_params and local_var_params[
                'apply'] is not None:  # noqa: E501
            query_params.append(
                ('$apply', local_var_params['apply']))  # noqa: E501
        if 'count' in local_var_params and local_var_params[
                'count'] is not None:  # noqa: E501
            query_params.append(
                ('$count', local_var_params['count']))  # noqa: E501
        if 'inlinecount' in local_var_params and local_var_params[
                'inlinecount'] is not None:  # noqa: E501
            query_params.append(
                ('$inlinecount',
                 local_var_params['inlinecount']))  # noqa: E501
        if 'at' in local_var_params and local_var_params[
                'at'] is not None:  # noqa: E501
            query_params.append(('at', local_var_params['at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([
            'application/json', 'text/csv',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/niatelemetry/NiaInventories',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NiatelemetryNiaInventoryList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_niatelemetry_nia_license_state_by_moid(self, moid,
                                                   **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaLicenseState' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_license_state_by_moid(moid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str moid: The unique Moid identifier of a resource instance. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NiatelemetryNiaLicenseState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_niatelemetry_nia_license_state_by_moid_with_http_info(
            moid, **kwargs)  # noqa: E501

    def get_niatelemetry_nia_license_state_by_moid_with_http_info(
            self, moid, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaLicenseState' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_license_state_by_moid_with_http_info(moid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str moid: The unique Moid identifier of a resource instance. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NiatelemetryNiaLicenseState, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['moid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_niatelemetry_nia_license_state_by_moid" %
                    key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'moid' is set
        if self.api_client.client_side_validation and (
                'moid' not in local_var_params or  # noqa: E501
                local_var_params['moid'] is None):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `moid` when calling `get_niatelemetry_nia_license_state_by_moid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'moid' in local_var_params:
            path_params['Moid'] = local_var_params['moid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([
            'application/json', 'text/csv',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/niatelemetry/NiaLicenseStates/{Moid}',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NiatelemetryNiaLicenseState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_niatelemetry_nia_license_state_list(self, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaLicenseState' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_license_state_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter: Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). 
        :param str orderby: Determines what properties are used to sort the collection of resources.
        :param int top: Specifies the maximum number of resources to return in the response.
        :param int skip: Specifies the number of resources to skip in the response.
        :param str select: Specifies a subset of properties to return.
        :param str expand: Specify additional attributes or related resources to return in addition to the primary resources.
        :param str apply: Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. 
        :param bool count: The $count query specifies the service should return the count of the matching resources, instead of returning the resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response.
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NiatelemetryNiaLicenseStateList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_niatelemetry_nia_license_state_list_with_http_info(
            **kwargs)  # noqa: E501

    def get_niatelemetry_nia_license_state_list_with_http_info(
            self, **kwargs):  # noqa: E501
        """Read a 'niatelemetry.NiaLicenseState' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_niatelemetry_nia_license_state_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str filter: Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). 
        :param str orderby: Determines what properties are used to sort the collection of resources.
        :param int top: Specifies the maximum number of resources to return in the response.
        :param int skip: Specifies the number of resources to skip in the response.
        :param str select: Specifies a subset of properties to return.
        :param str expand: Specify additional attributes or related resources to return in addition to the primary resources.
        :param str apply: Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. 
        :param bool count: The $count query specifies the service should return the count of the matching resources, instead of returning the resources.
        :param str inlinecount: The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response.
        :param str at: Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NiatelemetryNiaLicenseStateList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'filter', 'orderby', 'top', 'skip', 'select', 'expand', 'apply',
            'count', 'inlinecount', 'at'
        ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_niatelemetry_nia_license_state_list" % key)
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params and local_var_params[
                'filter'] is not None:  # noqa: E501
            query_params.append(
                ('$filter', local_var_params['filter']))  # noqa: E501
        if 'orderby' in local_var_params and local_var_params[
                'orderby'] is not None:  # noqa: E501
            query_params.append(
                ('$orderby', local_var_params['orderby']))  # noqa: E501
        if 'top' in local_var_params and local_var_params[
                'top'] is not None:  # noqa: E501
            query_params.append(
                ('$top', local_var_params['top']))  # noqa: E501
        if 'skip' in local_var_params and local_var_params[
                'skip'] is not None:  # noqa: E501
            query_params.append(
                ('$skip', local_var_params['skip']))  # noqa: E501
        if 'select' in local_var_params and local_var_params[
                'select'] is not None:  # noqa: E501
            query_params.append(
                ('$select', local_var_params['select']))  # noqa: E501
        if 'expand' in local_var_params and local_var_params[
                'expand'] is not None:  # noqa: E501
            query_params.append(
                ('$expand', local_var_params['expand']))  # noqa: E501
        if 'apply' in local_var_params and local_var_params[
                'apply'] is not None:  # noqa: E501
            query_params.append(
                ('$apply', local_var_params['apply']))  # noqa: E501
        if 'count' in local_var_params and local_var_params[
                'count'] is not None:  # noqa: E501
            query_params.append(
                ('$count', local_var_params['count']))  # noqa: E501
        if 'inlinecount' in local_var_params and local_var_params[
                'inlinecount'] is not None:  # noqa: E501
            query_params.append(
                ('$inlinecount',
                 local_var_params['inlinecount']))  # noqa: E501
        if 'at' in local_var_params and local_var_params[
                'at'] is not None:  # noqa: E501
            query_params.append(('at', local_var_params['at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([
            'application/json', 'text/csv',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/niatelemetry/NiaLicenseStates',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NiatelemetryNiaLicenseStateList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
