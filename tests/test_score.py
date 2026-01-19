from __future__ import unicode_literals
import os
from unittest import TestCase, mock
from telesign.score import ScoreClient

class TestScoreClient(TestCase):
    def setUp(self):
        self.customer_id = os.getenv('CUSTOMER_ID', 'FFFFFFFF-EEEE-DDDD-1234-AB1234567890')
        self.api_key = os.getenv('API_KEY', 'ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==')
        self.phone_number_test = os.getenv('PHONE_NUMBER', 'phone_number')
        self.account_lifecycle_event = "create"

    @mock.patch('telesign.rest.requests.Session.post')
    def test_score_method(self, mock_post):
        mock_response = mock.Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {
            "risk": {
                "level": "LOW",
                "recommendation": "allow"
            }
        }
        mock_post.return_value = mock_response

        client = ScoreClient(self.customer_id, self.api_key)
        response = client.score(self.phone_number_test, self.account_lifecycle_event)

        called_url = mock_post.call_args[0][0]
        self.assertIn('/intelligence/phone', called_url)

        called_kwargs = mock_post.call_args[1] if mock_post.call_args else {}
        called_data = called_kwargs.get('data', '')

        self.assertTrue(called_data, "POST data is empty, expected form parameters")
        self.assertIn(f'phone_number={self.phone_number_test}', called_data)
        self.assertIn(f'account_lifecycle_event={self.account_lifecycle_event}', called_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertEqual(response.headers.get('Content-Type'), 'application/json')
        self.assertIn('risk', response.json)
        self.assertEqual(response.json['risk']['level'], 'LOW')
        self.assertEqual(response.json['risk']['recommendation'], 'allow')
