from __future__ import unicode_literals

from telesign.rest import RestClient


APP_VERIFY_INITIATE_RESOURCE = '/v1/verify/auto/voice/initiate'
APP_VERIFY_FINALIZE_RESOURCE = '/v1/verify/auto/voice/finalize'
APP_VERIFY_FINALIZE_CALLERID_RESOURCE = '/v1/verify/auto/voice/finalize/callerid'
APP_VERIFY_TIMEOUT_RESOURCE = '/v1/verify/auto/voice/finalize/timeout'


class AppVerifyClient(RestClient):
    """
    The TeleSign App Verify web service enables customers to verify devices
    through a voice call by a verification code provided in the caller ID.
    """

    def __init__(self, customer_id, api_key, rest_endpoint='https://rest-ww.telesign.com', **kwargs):
        super(AppVerifyClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)


    def initiate(self, phone_number, **params):
        """
        Make an Initiate request to TeleSign that includes the phone number used for the handset.
        TeleSign places a call to the handset. This call will be terminated by the finalize request,
        if not by the handset terminating the call in your application

        See https://enterprise.telesign.com/docs/app-verify-api for detailed API documentation.
        """
        return self.post(APP_VERIFY_INITIATE_RESOURCE,
                         phone_number=phone_number,
                         **params)

    def finalize(self, reference_id, **params):
        """
        TeleSign compares the verify code generated for the call with the verify code
        in the Finalize request to determine whether they match.
        The result indicates whether the transaction is successful or not ('success' or 'failed').

        See https://enterprise.telesign.com/docs/app-verify-api for detailed API documentation.
        """
        return self.post(APP_VERIFY_FINALIZE_RESOURCE,
                         reference_id=reference_id,
                         **params)

    def finalize_caller_id(self, reference_id, unknown_caller_id, **params):
        """
        If a call is unsuccessful, the device will not receive the call.
        If there is a prefix sent by TeleSign in the initiate request and it cannot be matched
        to the CLI of the verification call, you can use the Finalize CallerID Unknown endpoint
        to report the issue to TeleSign for troubleshooting.

        See https://enterprise.telesign.com/docs/app-verify-api for detailed API documentation.
        """
        return self.post(APP_VERIFY_FINALIZE_CALLERID_RESOURCE,
                         reference_id=reference_id,
                         unknown_caller_id=unknown_caller_id,
                         **params)

    def finalize_timeout(self, reference_id, **params):
        """
        If a mobile device verification call does not make it to the designated handset within
        the specified amount of time, you can use the Finalize Timeout endpoint
        to report the issue to TeleSign.

        See https://enterprise.telesign.com/docs/app-verify-api for detailed API documentation.
        """
        return self.post(APP_VERIFY_TIMEOUT_RESOURCE,
                         reference_id=reference_id,
                         **params)
