from __future__ import unicode_literals

from telesign.rest import RestClient

MESSAGING_RESOURCE = "/v1/messaging"
MESSAGING_STATUS_RESOURCE = "/v1/messaging/{reference_id}"


class MessagingClient(RestClient):
    """
    TeleSign's Messaging API allows you to easily send SMS messages. You can send alerts, reminders, and notifications,
    or you can send verification messages containing one-time passcodes (OTP).
    """

    def __init__(self, customer_id, api_key, **kwargs):
        super(MessagingClient, self).__init__(customer_id, api_key, **kwargs)

    def message(self, phone_number, message, message_type, **params):
        """
        Send a message to the target phone_number.

        See https://developer.telesign.com/docs/messaging-api for detailed API documentation.
        """
        return self.post(MESSAGING_RESOURCE,
                         phone_number=phone_number,
                         message=message,
                         message_type=message_type,
                         **params)

    def status(self, reference_id, **params):
        """
        Retrieves the current status of the message.

        See https://developer.telesign.com/docs/messaging-api for detailed API documentation.
        """
        return self.get(MESSAGING_STATUS_RESOURCE.format(reference_id=reference_id),
                        **params)
