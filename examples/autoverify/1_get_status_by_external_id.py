from __future__ import print_function
from telesign.autoverify import AutoVerifyClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

external_id = "external_id"

autoverify = AutoVerifyClient(customer_id, api_key)
response = autoverify.status(external_id)

if response.ok:
    print("AutoVerify transaction with external_id {} has status code {} and status description {}.".format(
        external_id,
        response.json['status']['code'],
        response.json['status']['description']))
