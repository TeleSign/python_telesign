# -*- coding: utf-8 -*-
from __future__ import print_function
from telesign.voice import VoiceClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"

message = "N'oubliez pas d'appeler votre mère pour son anniversaire demain."
message_type = "ARN"

voice_client = VoiceClient(customer_id, api_key)
response = voice_client.call(phone_number, message, message_type, voice="f-FR-fr")
