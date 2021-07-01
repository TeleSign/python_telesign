from __future__ import unicode_literals
from json import dumps

from telesign.rest import RestClient

KES_HOST = "https://data.telesign.com"
KES_RESOURCE = "/kes"
HMAC_METHOD = "hmac-sha256"


class KESClient(RestClient):
    """
    KES or Known Event Share consumes customer events for data product quality improvement.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(KESClient, self).__init__(customer_id=customer_id,
                                        api_key=api_key,
                                        rest_endpoint=KES_HOST,
                                        **kwargs)
        self.customer_id = customer_id
        self.hmac_method = HMAC_METHOD

    def _execute(self, method_function, method_name, resource, **params):
        resource_uri = "{api_host}{resource}".format(api_host=self.api_host, resource=resource)
        json_fields = dumps(params)
        headers = RestClient.generate_telesign_headers(self.customer_id,
                                                       self.api_key,
                                                       method_name,
                                                       resource,
                                                       json_fields,
                                                       user_agent=self.user_agent,
                                                       content_type='application/json')
        payload = {'data': ""}
        if method_name in ['POST', 'PUT']:
            payload['data'] = dumps(params)

        response = self.Response(method_function(resource_uri,
                                                 headers=headers,
                                                 timeout=self.timeout,
                                                 **payload))
        return response

    def kes(self, **params):
        """
        KES is an API that consumes known event type data

        See https://enterprise-beta.telesign.com/api-reference/apis/known-events-share-api for Beta API documentation.
        """
        return self._execute(resource=KES_RESOURCE, **params)
