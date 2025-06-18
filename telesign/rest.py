from __future__ import unicode_literals

import hmac
import uuid
from base64 import b64encode, b64decode
from email.utils import formatdate
from hashlib import sha256
from platform import python_version
import time

import requests
import json

import telesign
from telesign.util import AuthMethod


class RestClient(requests.models.RequestEncodingMixin):
    """
    The Telesign RestClient is a generic HTTP REST client that can be extended to make requests against any of
    Telesign's REST API endpoints.

    RequestEncodingMixin offers the function _encode_params for url encoding the body for use in string_to_sign outside
    of a regular HTTP request.

    See https://developer.telesign.com for detailed API documentation.
    """

    class Response(object):
        """
        A simple HTTP Response object to abstract the underlying Requests library response.

        :param requests_response: A Requests response object.
        """

        def __init__(self, requests_response):
            self.status_code = requests_response.status_code
            self.headers = requests_response.headers
            self.body = requests_response.text
            self.ok = requests_response.ok

            try:
                self.json = requests_response.json()
            except (Exception, ValueError):
                self.json = None

    def __init__(self,
                 customer_id,
                 api_key,
                 rest_endpoint='https://rest-api.telesign.com',
                 source="python_telesign",
                 sdk_version_origin=None,
                 sdk_version_dependency=None,
                 proxies=None,
                 timeout=10,
                 auth_method=None,
                 pool_recycle=480):
        """
        Telesign RestClient useful for making generic RESTful requests against our API.

        :param customer_id: Your customer_id string associated with your account.
        :param api_key: Your api_key string associated with your account.
        :param rest_endpoint: (optional) Override the default rest_endpoint to target another endpoint string.
        :param proxies: (optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
        :param timeout: (optional) How long to wait for the server to send data before giving up, as a float,
                        or as a (connect timeout, read timeout) tuple
        :param pool_recycle: (optional) Time in seconds to recycle the HTTP session to avoid stale connections (default 480).
            If a session is older than this value, it will be closed and a new session will be created automatically before each request.
            This helps prevent errors due to HTTP keep-alive connections being closed by the server after inactivity.

        HTTP Keep-Alive behavior:
            TeleSign endpoints close idle HTTP keep-alive connections after 499 seconds. If you attempt to reuse a connection older than this, you may get a 'connection reset by peer' error.
            By default, pool_recycle=480 ensures sessions are refreshed before this limit.
        """
        self.customer_id = customer_id
        self.api_key = api_key

        self.api_host = rest_endpoint

        self.pool_recycle = pool_recycle
        self._session_created_at = None
        self.session = self._create_session()

        self.session.proxies = proxies if proxies else {}

        self.timeout = timeout

        self.auth_method = auth_method

        current_version_sdk = telesign.__version__ if source == "python_telesign" else sdk_version_origin

        self.user_agent = "TeleSignSDK/python Python/{python_version} Requests/{requests_version} OriginatingSDK/{source} SDKVersion/{sdk_version}".format(
        python_version=python_version(),
        requests_version=requests.__version__,
        source=source,
        sdk_version=current_version_sdk)

        if source != "python_telesign":
            self.user_agent = self.user_agent + " DependencySDKVersion/{sdk_version_dependency}".format(sdk_version_dependency=sdk_version_dependency)

    @staticmethod
    def generate_telesign_headers(customer_id,
                                  api_key,
                                  method_name,
                                  resource,
                                  url_encoded_fields,
                                  date_rfc2616=None,
                                  nonce=None,
                                  user_agent=None,
                                  content_type=None,
                                  auth_method=None):
        """
        Generates the Telesign REST API headers used to authenticate requests.

        Creates the canonicalized string_to_sign and generates the HMAC signature. This is used to authenticate requests
        against the Telesign REST API.

        See https://developer.telesign.com/docs/authentication for detailed API documentation.

        :param customer_id: Your account customer_id.
        :param api_key: Your account api_key.
        :param method_name: The HTTP method name of the request as a upper case string, should be one of 'POST', 'GET',
            'PUT', 'PATCH' or 'DELETE'.
        :param resource: The partial resource URI to perform the request against, as a string.
        :param url_encoded_fields: HTTP body parameters to perform the HTTP request with, must be a urlencoded string.
        :param date_rfc2616: The date and time of the request formatted in rfc 2616, as a string.
        :param nonce: A unique cryptographic nonce for the request, as a string.
        :param user_agent: (optional) User Agent associated with the request, as a string.
        :param content_type: (optional) ContentType of the request, as a string.
        :param auth_method: (optional) Authentication type ex: Basic, HMAC etc
        :return: The Telesign authentication headers.
        """
        if date_rfc2616 is None:
            date_rfc2616 = formatdate(usegmt=True)

        if nonce is None:
            nonce = str(uuid.uuid4())
        
        if not content_type:
            content_type = "application/x-www-form-urlencoded" if method_name in ("POST", "PUT") else ""

        # Default auth_method is Digest if not explicitly specified
        if auth_method == AuthMethod.BASIC.value:
            usr_apikey = "{customer_id}:{api_key}".format(customer_id=customer_id,
                                                          api_key=api_key)
            b64val = b64encode(usr_apikey.encode())
            authorization = "{auth_method} {b64val}".format(auth_method=AuthMethod.BASIC.value,
                                                            b64val=b64val.decode())
        else:
            auth_method = AuthMethod.HMAC_SHA256.value

            string_to_sign_builder = ["{method}".format(method=method_name)]

            string_to_sign_builder.append("\n{content_type}".format(content_type=content_type))

            string_to_sign_builder.append("\n{date}".format(date=date_rfc2616))

            string_to_sign_builder.append("\nx-ts-auth-method:{auth_method}".format(auth_method=auth_method))

            string_to_sign_builder.append("\nx-ts-nonce:{nonce}".format(nonce=nonce))

            if content_type and url_encoded_fields:
                string_to_sign_builder.append("\n{fields}".format(fields=url_encoded_fields))

            string_to_sign_builder.append("\n{resource}".format(resource=resource))

            string_to_sign = "".join(string_to_sign_builder)

            signer = hmac.new(b64decode(api_key), string_to_sign.encode("utf-8"), sha256)
            signature = b64encode(signer.digest()).decode("utf-8")

            authorization = "TSA {customer_id}:{signature}".format(
                customer_id=customer_id,
                signature=signature)

        headers = {
            "Authorization": authorization,
            "Date": date_rfc2616,
            "Content-Type": content_type,
            "x-ts-auth-method": auth_method,
            "x-ts-nonce": nonce
        }

        if user_agent:
            headers['User-Agent'] = user_agent

        return headers

    def post(self, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API POST handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param query_params: query_params to perform the POST request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.post, 'POST', resource, body, json_fields, **query_params)

    def get(self, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API GET handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param query_params: query_params to perform the GET request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.get, 'GET', resource, body, json_fields, **query_params)

    def put(self, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API PUT handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param query_params: query_params to perform the PUT request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.put, 'PUT', resource, body, json_fields, **query_params)

    def set_endpoint(self, rest_endpoint):
        self.api_host = rest_endpoint

    def delete(self, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API DELETE handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param query_params: query_params to perform the DELETE request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.delete, 'DELETE', resource, body, json_fields, **query_params)
    
    def patch(self, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API PATCH handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param json_fields: (optional) A dictionary sent as a JSON body.
        :param query_params: query_params to perform the PATCH request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.patch, 'PATCH', resource, body, json_fields, **query_params)

    def _create_session(self):
        session = requests.Session()
        self._session_created_at = time.time()
        return session

    def _ensure_session(self):
        if self._session_created_at is None or (time.time() - self._session_created_at > self.pool_recycle):
            if self.session:
                self.session.close()
            self.session = self._create_session()

    def _execute(self, method_function, method_name, resource, body=None, json_fields=None, **query_params):
        """
        Generic Telesign REST API request handler.

        :param method_function: The Requests HTTP request function to perform the request.
        :param method_name: The HTTP method name, as an upper case string.
        :param resource: The partial resource URI to perform the request against, as a string.
        :param body: (optional) A dictionary sent as a part of request body.
        :param query_params: query_params to perform the HTTP request with, as a dictionary.
        :return: The RestClient Response object.
        """
        self._ensure_session()
        resource_uri = "{api_host}{resource}".format(api_host=self.api_host, resource=resource)

        url_encoded_fields = self._encode_params(query_params)
        if json_fields:
            fields = json.dumps(json_fields)
            url_encoded_fields = fields

        if body or json_fields:
            content_type = "application/json"
        else:
            content_type = None  # set later

        headers = RestClient.generate_telesign_headers(self.customer_id,
                                                       self.api_key,
                                                       method_name,
                                                       resource,
                                                       url_encoded_fields,
                                                       user_agent=self.user_agent,
                                                       content_type=content_type,
                                                       auth_method=self.auth_method)
        if method_name in ['POST', 'PUT']:
            payload = {}
            if body:
                payload['json'] = body
            if query_params:
                payload['data'] = url_encoded_fields
            if json_fields:
                payload = {'data': url_encoded_fields}
        else:
            payload = {'params': url_encoded_fields}

        response = self.Response(method_function(resource_uri,
                                                 headers=headers,
                                                 timeout=self.timeout,
                                                 **payload))

        return response
