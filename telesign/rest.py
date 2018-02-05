from __future__ import unicode_literals

from requests import post
import hmac
import uuid
from base64 import b64encode, b64decode
from email.utils import formatdate
from hashlib import sha256
from platform import python_version

import requests

import telesign


class RestClient(requests.models.RequestEncodingMixin):
    """
    The TeleSign RestClient is a generic HTTP REST client that can be extended to make requests against any of
    TeleSign's REST API endpoints.

    RequestEncodingMixin offers the function _encode_params for url encoding the body for use in string_to_sign outside
    of a regular HTTP request.

    See https://developer.telesign.com for detailed API documentation.
    """
    user_agent = "TeleSignSDK/python-{sdk_version} Python/{python_version} Requests/{requests_version}".format(
        sdk_version=telesign.__version__,
        python_version=python_version(),
        requests_version=requests.__version__)

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
                 proxies=None,
                 timeout=10):
        """
        TeleSign RestClient useful for making generic RESTful requests against our API.

        :param customer_id: Your customer_id string associated with your account.
        :param api_key: Your api_key string associated with your account.
        :param rest_endpoint: (optional) Override the default rest_endpoint to target another endpoint string.
        :param proxies: (optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy.
        :param timeout: (optional) How long to wait for the server to send data before giving up, as a float,
                        or as a (connect timeout, read timeout) tuple
        """
        self.customer_id = customer_id
        self.api_key = api_key

        self.api_host = rest_endpoint

        self.session = requests.Session()

        self.session.proxies = proxies if proxies else {}

        self.timeout = timeout

    @staticmethod
    def generate_telesign_headers(customer_id,
                                  api_key,
                                  method_name,
                                  resource,
                                  url_encoded_fields,
                                  date_rfc2616=None,
                                  nonce=None,
                                  user_agent=None,
                                  content_type=None):
        """
        Generates the TeleSign REST API headers used to authenticate requests.

        Creates the canonicalized string_to_sign and generates the HMAC signature. This is used to authenticate requests
        against the TeleSign REST API.

        See https://developer.telesign.com/docs/authentication for detailed API documentation.

        :param customer_id: Your account customer_id.
        :param api_key: Your account api_key.
        :param method_name: The HTTP method name of the request as a upper case string, should be one of 'POST', 'GET',
            'PUT' or 'DELETE'.
        :param resource: The partial resource URI to perform the request against, as a string.
        :param url_encoded_fields: HTTP body parameters to perform the HTTP request with, must be a urlencoded string.
        :param date_rfc2616: The date and time of the request formatted in rfc 2616, as a string.
        :param nonce: A unique cryptographic nonce for the request, as a string.
        :param user_agent: (optional) User Agent associated with the request, as a string.
        :param content_type: (optional) ContentType of the request, as a string.
        :return: The TeleSign authentication headers.
        """
        if date_rfc2616 is None:
            date_rfc2616 = formatdate(usegmt=True)

        if nonce is None:
            nonce = str(uuid.uuid4())
        
        if not content_type:
            content_type = "application/x-www-form-urlencoded" if method_name in ("POST", "PUT") else ""

        auth_method = "HMAC-SHA256"

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

    def post(self, resource, **params):
        """
        Generic TeleSign REST API POST handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param params: Body params to perform the POST request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.post, 'POST', resource, **params)

    def get(self, resource, **params):
        """
        Generic TeleSign REST API GET handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param params: Body params to perform the GET request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.get, 'GET', resource, **params)

    def put(self, resource, **params):
        """
        Generic TeleSign REST API PUT handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param params: Body params to perform the PUT request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.put, 'PUT', resource, **params)

    def delete(self, resource, **params):
        """
        Generic TeleSign REST API DELETE handler.

        :param resource: The partial resource URI to perform the request against, as a string.
        :param params: Body params to perform the DELETE request with, as a dictionary.
        :return: The RestClient Response object.
        """
        return self._execute(self.session.delete, 'DELETE', resource, **params)

    def _execute(self, method_function, method_name, resource, **params):
        """
        Generic TeleSign REST API request handler.

        :param method_function: The Requests HTTP request function to perform the request.
        :param method_name: The HTTP method name, as an upper case string.
        :param resource: The partial resource URI to perform the request against, as a string.
        :param params: Body params to perform the HTTP request with, as a dictionary.
        :return: The RestClient Response object.
        """
        resource_uri = "{api_host}{resource}".format(api_host=self.api_host, resource=resource)

        url_encoded_fields = self._encode_params(params)

        headers = RestClient.generate_telesign_headers(self.customer_id,
                                                       self.api_key,
                                                       method_name,
                                                       resource,
                                                       url_encoded_fields,
                                                       user_agent=self.user_agent)

        if method_name in ['POST', 'PUT']:
            payload = {'data': url_encoded_fields}
        else:
            payload = {'params': url_encoded_fields}

        response = self.Response(method_function(resource_uri,
                                                 headers=headers,
                                                 timeout=self.timeout,
                                                 **payload))

        return response
