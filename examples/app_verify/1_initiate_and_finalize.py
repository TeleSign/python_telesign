from __future__ import print_function
from telesignenterprise.appverify import AppVerifyClient


customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="
phone_number = "phone_number"

verify = AppVerifyClient(customer_id, api_key)

initiate_response = verify.initiate(phone_number)
print("initiate response: {}\n".format(initiate_response.json))

reference_id = initiate_response.json['reference_id']
verify_code = raw_input("Please enter the verification code from the caller id: ")
finalize_response = verify.finalize(reference_id, verify_code=verify_code)
print("\nfinalize response: {}\n".format(finalize_response.json))
