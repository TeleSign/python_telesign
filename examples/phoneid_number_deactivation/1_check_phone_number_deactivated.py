from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
ucid = "ATCK"

phoneid = PhoneIdClient(customer_id, api_key)
response = phoneid.number_deactivation(phone_number, ucid)

if response.ok:
    if response.json['number_deactivation']['last_deactivated']:
        print("Phone number {} was last deactivated {}.".format(
            response.json['number_deactivation']['number'],
            response.json['number_deactivation']['last_deactivated']))
    else:
        print("Phone number {} has not been deactivated.".format(response.json['number_deactivation']['number']))
