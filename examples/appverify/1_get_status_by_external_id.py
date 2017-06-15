from __future__ import print_function
from telesign.appverify import AppVerifyClient

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

external_id = "external_id"

appverify = AppVerifyClient(customer_id, api_key)
response = appverify.status(external_id)

if response.ok:
    print("App Verify transaction with external_id {} has status code {} and status description {}.".format(
        external_id,
        response.json['status']['code'],
        response.json['status']['description']))
