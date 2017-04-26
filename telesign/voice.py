from __future__ import unicode_literals

from telesign.rest import RestClient

VOICE_RESOURCE = "/v1/voice"
VOICE_STATUS_RESOURCE = "/v1/voice/{reference_id}"


class VoiceClient(RestClient):
    """
    TeleSign's Voice API allows you to easily send voice messages. You can send alerts, reminders, and notifications,
    or you can send verification messages containing time-based, one-time passcodes (TOTP).
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(VoiceClient, self).__init__(customer_id, api_key, **kwargs)

    def call(self, phone_number, message, message_type, **params):
        """
        Send a voice call to the target phone_number.

        See https://developer.telesign.com/docs/voice-api for detailed API documentation.
        """
        return self.post(VOICE_RESOURCE,
                         phone_number=phone_number,
                         message=message,
                         message_type=message_type,
                         **params)

    def status(self, reference_id, **params):
        """
        Retrieves the current status of the voice call.

        See https://developer.telesign.com/docs/voice-api for detailed API documentation.
        """
        return self.get(VOICE_STATUS_RESOURCE.format(reference_id=reference_id),
                        **params)
