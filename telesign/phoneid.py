from __future__ import unicode_literals

import json

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

        content_type = "application/json" if method_name in ("POST", "PUT") else ""

        headers = self.generate_telesign_headers(self.customer_id,
                                                 self.api_key,
                                                 method_name,
                                                 resource,
                                                 json_fields,
                                                 user_agent=self.user_agent,
                                                 content_type=content_type)

        if method_name in ['POST', 'PUT']:
            payload = {'data': json_fields}
        else:
            payload = {'params': json_fields}

        response = self.Response(method_function(resource_uri,
                                                 headers=headers,
                                                 timeout=self.timeout,
                                                 **payload))

        return response
