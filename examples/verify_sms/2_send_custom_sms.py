from __future__ import print_function
from telesignenterprise.verify import VerifyClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
template = "Your Widgets 'n' More verification code is $$CODE$$."

verify = VerifyClient(customer_id, secret_key)
response = verify.sms(phone_number, template=template)
