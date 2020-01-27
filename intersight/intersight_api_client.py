'''
Created on Nov 6, 2017

@author: dipeshah
'''

from __future__ import absolute_import

import os
import re
import json
import threading

from six.moves.urllib.parse import quote, urlencode, urlparse
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode
from intersight import ApiClient
from intersight.configuration import Configuration

class IntersightApiClient(ApiClient):
    '''
    Intersight API client for Swagger client library builds. Its defined as
    a child to ApiClient class which is auto-generated as part of Intersight Python SDK
    
    This client handles the support for api keys feature for Intersight project.

    NOTE: This class calculates digest based on RFC 
    https://datatracker.ietf.org/doc/draft-cavage-http-signatures/?include_text=1

    :param host: The base path for the server to call.
    :param private_key: a private key (pem) file calls to the API.
    :param api_key_id: a string value which is a combination of unique user, account and id calls to the API.
    '''

    def __init__(self, host=None, header_name=None, header_value=None, cookie=None, private_key=None, api_key_id=None):
        '''
        Constructor of the class IntersightApiClient
        '''
        super(IntersightApiClient, self).__init__(
            configuration=Configuration(host=host),
            header_name=header_name,
            header_value=header_value,
            cookie=cookie,
        )
        self.host = host
        self.private_key_file = private_key
        self.api_key_id = api_key_id
        self.digest_algorithm = "rsa-sha256"
    
    
    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, callback=None,
                 _return_http_data_only=None, collection_formats=None, _preload_content=True,
                 _request_timeout=None):
        
        '''
        This method overrides a same name method in parent class ApiClient to calculate digest
        for api key support.
        '''
        
        
        # Store the original body so you can pass it back to call_api, since call_api also does sanitize_for_serialization. and
        # we don't want to modify api_client file. 
        unsanitized_body = body
        
        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=''))  # no safe chars, encode everything
        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
        
        # body
        if body:
            body = self.sanitize_for_serialization(body)
            
        self.prepare_auth_header(resource_path, method, body, query_params)
        
        return super(IntersightApiClient, self).call_api(resource_path, method, path_params, query_params, header_params, 
                                                unsanitized_body, post_params, files, response_type, auth_settings, callback,
                                                _return_http_data_only, collection_formats, _preload_content, _request_timeout)
    
    
    def get_sha256_digest(self, data):
        """
        :param data: Data set by User
        :return: instance of digest object 
        """
        digest = SHA256.new()
        digest.update(data)
        
        return digest
    
    def get_rsasig_b64encode(self, private_key_path, digest):
        """
        :param private_key_path : abs path to private key .pem file.
        :param digest: digest
        :return: instance of digest object 
        """
        
        key = open(private_key_path, "r").read()
        rsakey = RSA.importKey(key)
        signer = PKCS1_v1_5.new(rsakey)
        sign = signer.sign(digest)
        
        return b64encode(sign)
    
    def prepare_str_to_sign(self, req_tgt, hdrs):
        """
        :param req_tgt : Request Target as stored in http header.
        :param hdrs: HTTP Headers to be signed.
        :return: instance of digest object 
        """
        ss = ""
        ss = ss + "(request-target): " + req_tgt.lower() + "\n"
    
        length = len(hdrs.items())
    
        i = 0
        for key, value in hdrs.items():
            ss = ss + key.lower() + ": " + value
            if i < length-1:
                ss = ss + "\n"
            i += 1
        
        return ss

    def get_auth_header(self, hdrs, signed_msg):
        """
        This method prepares the Auth header string
        
        :param hdrs : HTTP Headers
        :param signed_msg: Signed Digest
        :return: instance of digest object 
        """
        
        auth_str = ""
        auth_str = auth_str + "Signature"
    
        auth_str = auth_str + " " + "keyId=\"" + self.api_key_id + "\"," + "algorithm=\"" + self.digest_algorithm + "\"," + "headers=\"(request-target)"
    
        for key, _ in hdrs.items():
            auth_str = auth_str + " " + key.lower()
        auth_str = auth_str + "\""
    
        auth_str = auth_str + "," + "signature=\"" + signed_msg.decode('ascii') + "\""
    
        return auth_str
    
    def prepare_auth_header(self, resource_path, method, body, query_params):
        """
        Method to perform operations required to prepare the auth header and eventually
        add the signed headers to default_header object used by ApiClient class.
        
        :param resource_path : resource path which is the api being called upon.
        :param method: request type
        :param body: body passed in the http request.
        :param query_params: query parameters used by the API 
        :return: instance of digest object 
        """
        if body is None:
            body = ''
        else:
            body = json.dumps(body)
        
        
        target_host = urlparse(self.host).netloc
        target_path = urlparse(self.host).path
        
        request_target = method + " " + target_path + resource_path
        
        if query_params:
            raw_query = urlencode(query_params).replace('+', '%20')
            request_target += "?" + raw_query
        
        from email.utils import formatdate
        cdate=formatdate(timeval=None, localtime=False, usegmt=True)
        
        request_body = body.encode()
        body_digest = self.get_sha256_digest(request_body)
        b64_body_digest = b64encode(body_digest.digest())
        
        headers = {'Content-Type': 'application/json', 'Date' : cdate, 'Host' : target_host, 'Digest' : "SHA-256=" + b64_body_digest.decode('ascii')}
        
        string_to_sign = self.prepare_str_to_sign(request_target, headers)
        
        digest = self.get_sha256_digest(string_to_sign.encode())
        
        b64_signed_msg = self.get_rsasig_b64encode(self.private_key_file, digest)
        
        auth_header = self.get_auth_header(headers, b64_signed_msg)
        
        self.set_default_header('Date', '{0}'.format(cdate))
        self.set_default_header('Host', '{0}'.format(target_host))
        self.set_default_header('Digest', 'SHA-256={0}'.format(b64_body_digest.decode('ascii')))
        self.set_default_header('Authorization', '{0}'.format(auth_header))
        
