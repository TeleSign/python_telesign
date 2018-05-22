from __future__ import unicode_literals

from telesign.voice import VoiceClient as _VoiceClient


class VoiceClient(_VoiceClient):
    """
    TeleSign's Voice API allows you to easily send voice messages. You can send alerts, reminders, and notifications,
    or you can send verification messages containing time-based, one-time passcodes (TOTP).
    """

    def __init__(self, customer_id, api_key, rest_endpoint="https://rest-ww.telesign.com", **kwargs):
        super(VoiceClient, self).__init__(customer_id, api_key, rest_endpoint=rest_endpoint, **kwargs)
