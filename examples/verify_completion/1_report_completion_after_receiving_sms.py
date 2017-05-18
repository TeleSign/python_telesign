from __future__ import print_function
from telesignenterprise.verify import VerifyClient
from telesign.util import random_with_n_digits

customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

phone_number = "phone_number"
verify_code = random_with_n_digits(5)

verify = VerifyClient(customer_id, api_key)
response = verify.sms(phone_number, verify_code=verify_code)

reference_id = response.json.get('reference_id')

user_entered_verify_code = raw_input("Please enter the verification code you were sent: ")

if verify_code == user_entered_verify_code.strip():
    print("Your code is correct.")

    response = verify.completion(reference_id)
    if response.status_code == 200 and response.json.get('status').get('code') == 1900:
        print("Completion successfully reported.")
    else:
        print("Error reporting completion.")

else:
    print("Your code is incorrect.")
