# coding=utf-8
from __future__ import print_function
from telesignenterprise.verify import VerifyClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
template = u"Votre code de vérification Widgets 'n' More est $$CODE$$."

verify = VerifyClient(customer_id, secret_key)
response = verify.sms(phone_number, template=template)
