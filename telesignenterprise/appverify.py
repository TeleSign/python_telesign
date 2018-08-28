from __future__ import unicode_literals

from telesign.appverify import AppVerifyClient as _AppVerifyClient


APP_VERIFY_INITIATE_RESOURCE = '/v1/verify/auto/voice/initiate'
APP_VERIFY_FINALIZE_RESOURCE = '/v1/verify/auto/voice/finalize'
APP_VERIFY_STATUS_RESOURCE = '/v1/verify/auto/voice/{}'


class AppVerifyClient(_AppVerifyClient):
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

    def status(self, reference_id, **params):
        """
        TeleSign looks up the status for the verification call in the
        Initiate request to determine status of the AV call, including
        intermediate call status such as call failed, or retry.

        See https://enterprise.telesign.com/docs/app-verify-api for detailed API documentation.
        """
        return self.get(APP_VERIFY_STATUS_RESOURCE.format(reference_id), **params)
