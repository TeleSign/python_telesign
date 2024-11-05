from __future__ import unicode_literals
import os
from unittest import TestCase
from telesign.phoneid import PhoneIdClient

class TestPhoneId(TestCase):
    def setUp(self):
        self.customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
        self.api_key = os.getenv('API_KEY', 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')
        self.phone_number_test = "11234567890"

    def test_phoneid_constructor(self):

        client = PhoneIdClient(self.customer_id,
                            self.api_key)

        self.assertEqual(client.customer_id, self.customer_id)
        self.assertEqual(client.api_key, self.api_key)
        

    def test_phoneid_pid_contact(self):

        client = PhoneIdClient(self.customer_id, self.api_key)
        content_type_expected = 'application/json'
        status_code_expected = 200
        
        payload = {  
            "addons": {
                "contact": {}
            },
            "phone_number": self.phone_number_test
        }

        response = client.phoneid(**payload)

        self.assertEqual(response.headers.get('Content-Type'), content_type_expected, "Content-Type args do not match expected")
        self.assertEqual(response.status_code, status_code_expected, "Status code args do not match expected")

    def test_phoneid_pid(self):

        client = PhoneIdClient(self.customer_id, self.api_key)
        content_type_expected = 'application/json'
        status_code_expected = 200

        response = client.phoneid(self.phone_number_test)

        self.assertEqual(response.headers.get('Content-Type'), content_type_expected, "Content-Type args do not match expected")
        self.assertEqual(response.status_code, status_code_expected, "Status code args do not match expected")
