from __future__ import print_function
from telesignenterprise.phoneid import PhoneIdClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
ucid = "BACF"

phoneid = PhoneIdClient(customer_id, api_key)
response = phoneid.score(phone_number, ucid)

if response.ok:
    print("Phone number {} has a '{}' risk level and the recommendation is to '{}' the transaction.".format(
        phone_number,
        response.json['risk']['level'],
        response.json['risk']['recommendation']))
