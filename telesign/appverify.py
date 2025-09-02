from __future__ import unicode_literals

from telesign.rest import RestClient


class AppVerifyClient(RestClient):
    """
    App Verify is a secure, lightweight SDK that integrates a frictionless user verification process into existing
    native mobile applications.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(AppVerifyClient, self).__init__(customer_id, api_key, **kwargs)