from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
message = "You're scheduled for a dentist appointment at 2:30PM."
message_type = "ARN"

messaging = MessagingClient(customer_id, secret_key)
response = messaging.message(phone_number, message, message_type)
