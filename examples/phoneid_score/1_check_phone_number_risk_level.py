from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
ucid = "BACF"

phoneid = PhoneIdClient(customer_id, secret_key)
response = phoneid.score(phone_number, ucid)

if response.ok:
    print("Phone number {} has a '{}' risk level and the recommendation is to '{}' the transaction.".format(
        phone_number,
        response.json['risk']['level'],
        response.json['risk']['recommendation']))
