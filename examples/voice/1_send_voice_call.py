from __future__ import print_function
from telesign.voice import VoiceClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
message = "You're scheduled for a dentist appointment at 2:30PM."
message_type = "ARN"

voice = VoiceClient(customer_id, secret_key)
response = voice.call(phone_number, message, message_type)
