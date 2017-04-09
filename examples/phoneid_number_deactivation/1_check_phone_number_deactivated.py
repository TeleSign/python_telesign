from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "customer_id"
secret_key = "secret_key"

phone_number = "phone_number"
ucid = "ATCK"

phoneid = PhoneIdClient(customer_id, secret_key)
response = phoneid.number_deactivation(phone_number, ucid)

if response.ok:
    if response.json['number_deactivation']['last_deactivated']:
        print("Phone number {} was last deactivated {}.".format(
            response.json['number_deactivation']['number'],
            response.json['number_deactivation']['last_deactivated']))
    else:
        print("Phone number {} has not been deactivated.".format(response.json['number_deactivation']['number']))
