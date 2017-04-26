from __future__ import unicode_literals

from telesign.rest import RestClient

AUTOVERIFY_STATUS_RESOURCE = "/v1/mobile/verification/status/{external_id}"


class AutoVerifyClient(RestClient):
    """
    AutoVerify is a secure, lightweight SDK that integrates a frictionless user verification process into existing
    native mobile applications.
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(AutoVerifyClient, self).__init__(customer_id, api_key, **kwargs)

    def status(self, external_id, **params):
        """
        Retrieves the verification result for an AutoVerify transaction by external_id. To ensure a secure verification
        flow you must check the status using TeleSign's servers on your backend. Do not rely on the SDK alone to
        indicate a successful verification.

        See https://developer.telesign.com/docs/auto-verify-sdk-self#section-obtaining-verification-status for detailed 
        API documentation.
        """
        return self.get(AUTOVERIFY_STATUS_RESOURCE.format(external_id=external_id),
                        **params)
