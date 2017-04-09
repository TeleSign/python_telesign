from __future__ import print_function
from telesign.phoneid import PhoneIdClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
phone_type_voip = "5"

data = PhoneIdClient(customer_id, secret_key)
response = data.phoneid(phone_number)

if response.ok:
    if response.json['phone_type']['code'] == phone_type_voip:
        print("Phone number {} is a VOIP phone.".format(
            phone_number))
    else:
        print("Phone number {} is not a VOIP phone.".format(
            phone_number))
