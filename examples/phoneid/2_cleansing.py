from __future__ import print_function
from telesign.phoneid import PhoneIdClient

customer_id = "customer_id"
secret_key = "secret_key"

extra_digit = "0"
phone_number = "phone_number"
incorrect_phone_number = "{}{}".format(phone_number, extra_digit)

data = PhoneIdClient(customer_id, secret_key)
response = data.phoneid(incorrect_phone_number)

if response.ok:
    print("Cleansed phone number has country code {} and phone number is {}.".format(
        response.json['numbering']['cleansing']['call']['country_code'],
        response.json['numbering']['cleansing']['call']['phone_number']))

    print("Original phone number was {}.".format(
        response.json['numbering']['original']['complete_phone_number']))
