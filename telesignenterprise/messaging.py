from __future__ import unicode_literals

from telesign.messaging import MessagingClient as _MessagingClient


class MessagingClient(_MessagingClient):
    """
    TeleSign's Messaging API allows you to easily send SMS messages. You can send alerts, reminders, and notifications,
    or you can send verification messages containing one-time passcodes (OTP).
    """

    def __init__(self, customer_id, api_key, rest_endpoint="https://rest-ww.telesign.com", **kwargs):
        super(MessagingClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)
