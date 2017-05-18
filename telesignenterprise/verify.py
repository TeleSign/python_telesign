from __future__ import unicode_literals

from telesign.rest import RestClient

VERIFY_SMS_RESOURCE = "/v1/verify/sms"
VERIFY_VOICE_RESOURCE = "/v1/verify/call"
VERIFY_SMART_RESOURCE = "/v1/verify/smart"
VERIFY_PUSH_RESOURCE = "/v2/verify/push"
VERIFY_STATUS_RESOURCE = "/v1/verify/{reference_id}"
VERIFY_COMPLETION_RESOURCE = "/v1/verify/completion/{reference_id}"


class VerifyClient(RestClient):
    """
    The Verify API delivers phone-based verification and two-factor authentication using a time-based, one-time passcode
    sent via SMS message, Voice call or Push Notification.
    """

    def __init__(self, customer_id, api_key, rest_endpoint='https://rest-ww.telesign.com', **kwargs):
        super(VerifyClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)

    def sms(self, phone_number, **params):
        """
        The SMS Verify API delivers phone-based verification and two-factor authentication using a time-based,
        one-time passcode sent over SMS.

        See https://developer.telesign.com/docs/rest_api-verify-sms for detailed API documentation.
        """
        return self.post(VERIFY_SMS_RESOURCE,
                         phone_number=phone_number,
                         **params)

    def voice(self, phone_number, **params):
        """
        The Voice Verify API delivers patented phone-based verification and two-factor authentication using a one-time
        passcode sent over voice message.

        See https://developer.telesign.com/docs/rest_api-verify-call for detailed API documentation.
        """
        return self.post(VERIFY_VOICE_RESOURCE,
                         phone_number=phone_number,
                         **params)

    def smart(self, phone_number, ucid, **params):
        """
        The Smart Verify web service simplifies the process of verifying user identity by integrating several TeleSign
        web services into a single API call. This eliminates the need for you to make multiple calls to the TeleSign
        Verify resource.

        See https://developer.telesign.com/docs/rest_api-smart-verify for detailed API documentation.
        """
        return self.post(VERIFY_SMART_RESOURCE,
                         phone_number=phone_number,
                         ucid=ucid,
                         **params)

    def push(self, phone_number, ucid, **params):
        """
        The Push Verify web service allows you to provide on-device transaction authorization for your end users. It
        works by delivering authorization requests to your end users via push notification, and then by receiving their
        permission responses via their mobile device's wireless Internet connection.

        See https://developer.telesign.com/docs/rest_api-verify-push for detailed API documentation.
        """
        return self.post(VERIFY_PUSH_RESOURCE,
                         phone_number=phone_number,
                         ucid=ucid,
                         **params)

    def status(self, reference_id, **params):
        """
        Retrieves the verification result for any verify resource.

        See https://developer.telesign.com/docs/rest_api-verify-transaction-callback for detailed API documentation.
        """
        return self.get(VERIFY_STATUS_RESOURCE.format(reference_id=reference_id),
                        **params)

    def completion(self, reference_id, **params):
        """
        Notifies TeleSign that a verification was successfully delivered to the user in order to help improve
        the quality of message delivery routes.

        See https://developer.telesign.com/docs/completion-service-for-verify-products for detailed API documentation.
        """
        return self.put(VERIFY_COMPLETION_RESOURCE.format(reference_id=reference_id),
                        **params)
