from __future__ import print_function
from telesign.autoverify import AutoVerifyClient

customer_id = "customer_id"
secret_key = "secret_key"

external_id = "external_id"

autoverify = AutoVerifyClient(customer_id, secret_key)
response = autoverify.status(external_id)

if response.ok:
    print("AutoVerify transaction with external_id {} has status code {} and status description {}.".format(
        external_id,
        response.json['status']['code'],
        response.json['status']['description']))
