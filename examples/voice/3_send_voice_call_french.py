# -*- coding: utf-8 -*-
from __future__ import print_function
from telesign.voice import VoiceClient

customer_id = "customer id"
secret_key = "secret key"

phone_number = "phone number"

message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain."
message_type = "ARN"

voice_client = VoiceClient(customer_id, secret_key)
response = voice_client.call(phone_number, message, message_type, voice="f-FR-fr")
