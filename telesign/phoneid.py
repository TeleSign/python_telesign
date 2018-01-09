from __future__ import unicode_literals

import json
import uuid
import hmac

from base64 import b64encode, b64decode
from hashlib import sha256
from email.utils import formatdate

from telesign.rest import RestClient

PHONEID_RESOURCE = "/v1/phoneid/{phone_number}"


class PhoneIdClient(RestClient):
    """
    A set of APIs that deliver deep phone number data attributes that help optimize the end user
    verification process and evaluate risk.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(PhoneIdClient, self).__init__(customer_id, api_key, **kwargs)

    def phoneid(self, phone_number, **params):
        """
        The PhoneID API provides a cleansed phone number, phone type, and telecom carrier information to determine the
        best communication method - SMS or voice.

        See https://developer.telesign.com/docs/phoneid-api for detailed API documentation.
        """
        return self.post(PHONEID_RESOURCE.format(phone_number=phone_number),
                         **params)

    def _execute(self, method_function, method_name, resource, **params):
        resource_uri = "{api_host}{resource}".format(api_host=self.api_host, resource=resource)

        json_fields = json.dumps(params)

        headers = self.generate_telesign_headers(self.customer_id,
                                                 self.api_key,
                                                 method_name,
                                                 resource,
                                                 json_fields,
                                                 user_agent=self.user_agent)

        if method_name in ['POST', 'PUT']:
            payload = {'data': json_fields}
        else:
            payload = {'params': json_fields}

        response = self.Response(method_function(resource_uri,
                                                 headers=headers,
                                                 timeout=1000,
                                                 **payload))

        return response

    @staticmethod
    def generate_telesign_headers(customer_id, api_key, method_name, resource, json_fields, date_rfc2616=None,
                                  nonce=None, user_agent=None):

        if date_rfc2616 is None:
            date_rfc2616 = formatdate(usegmt=True)

        if nonce is None:
            nonce = str(uuid.uuid4())

        content_type = "application/json" if method_name in ("POST", "PUT") else ""

        auth_method = "HMAC-SHA256"

        string_to_sign_builder = ["{method}".format(method=method_name)]

        string_to_sign_builder.append("\n{content_type}".format(content_type=content_type))

        string_to_sign_builder.append("\n{date}".format(date=date_rfc2616))

        string_to_sign_builder.append("\nx-ts-auth-method:{auth_method}".format(auth_method=auth_method))

        string_to_sign_builder.append("\nx-ts-nonce:{nonce}".format(nonce=nonce))

        if content_type and json_fields:
            string_to_sign_builder.append("\n{fields}".format(fields=json_fields))

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
