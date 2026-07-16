from __future__ import unicode_literals
import json
import os
from unittest import TestCase, mock
from telesign.voice import VoiceClient

class TestVoice(TestCase):
    def setUp(self):
        self.customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
        self.api_key = os.getenv('API_KEY', 'EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')
        self.phone_number_test = os.getenv('PHONE_NUMBER', 'phone_number')
        self.client = VoiceClient(self.customer_id, self.api_key)

    def test_voice_constructor(self):
        self.assertEqual(self.client.customer_id, self.customer_id)
        self.assertEqual(self.client.api_key, self.api_key)

    @mock.patch('telesign.rest.requests.Session.post')
    def test_voice_call(self, mock_post):
        expected_response =  {
            "reference_id": "0123456789ABCDEF0123456789ABCDEF",
            "external_id": None,
            "status": {
                "code": 130,
                "description": "Call blocked by TeleSign",
                "updated_on": "2026-05-29T21:09:19.378673Z"
            },
            "voice": {
                "caller_id": "+16268723943"
            }
        }
        mock_response = mock.Mock(
            status_code=200,
            headers={'Content-Type': 'application/json'},
            ok=True,
            text=json.dumps(expected_response)
        )
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        response = self.client.call(self.phone_number_test, "Hello, this is a test message!", "ARN")

        called_url = mock_post.call_args[0][0]
        self.assertIn('/v1/voice', called_url)
        called_kwargs = mock_post.call_args[1] if mock_post.call_args else {}
        called_data = called_kwargs.get('data', '')

        self.assertTrue(called_data, "POST data is empty, expected form parameters")
        self.assertEqual(response.headers.get('Content-Type'), 'application/json', "Content-Type args do not match expected")
        self.assertEqual(response.status_code, 200, "Status code args do not match expected")
        self.assertEqual(response.json, expected_response, "Response does not match expected mock response")

    @mock.patch('telesign.rest.requests.Session.get')
    def test_voice_status(self, mock_get):
        expected_response =  {
            "reference_id": "0123456789ABCDEF0123456789ABCDEF",
            "status": {
                "code": 100,
                "description": "Call answered",
                "updated_on": "2026-05-29T17:38:49.049000Z"
            },
        }
        mock_response = mock.Mock(
            status_code=201,
            headers={'Content-Type': 'application/json'},
            ok=True,
            text=json.dumps(expected_response)
        )
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = self.client.status("0123456789ABCDEF0123456789ABCDEF")

        called_url = mock_get.call_args[0][0]
        self.assertIn('/v1/voice/0123456789ABCDEF0123456789ABCDEF', called_url)

        self.assertEqual(response.headers.get('Content-Type'), 'application/json', "Content-Type args do not match expected")
        self.assertEqual(response.status_code, 201, "Status code args do not match expected")
        self.assertEqual(response.json, expected_response, "Response does not match expected mock response")