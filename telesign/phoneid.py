from __future__ import unicode_literals

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
