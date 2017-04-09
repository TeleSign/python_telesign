from __future__ import print_function
from telesign.score import ScoreClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
account_lifecycle_event = "create"

data = ScoreClient(customer_id, secret_key)
response = data.score(phone_number, account_lifecycle_event)

if response.ok:
    print("Phone number {} has a '{}' risk level and the recommendation is to '{}' the transaction.".format(
        phone_number,
        response.json['risk']['level'],
        response.json['risk']['recommendation']))
