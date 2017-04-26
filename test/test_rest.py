from __future__ import unicode_literals

from unittest import TestCase
from email.utils import parsedate_tz
from uuid import UUID
from mock import Mock, patch

from telesign.rest import RestClient


class TestRest(TestCase):
    def setUp(self):
        self.customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
        self.api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

    def test_rest_client_constructor_basic(self):

        client = RestClient(self.customer_id,
                            self.api_key)

        self.assertEqual(client.customer_id, self.customer_id)
        self.assertEqual(client.api_key, self.api_key)

    def test_rest_client_response_constructor_basic(self):

        requests_response = Mock(status_code=200,
                                 headers={'Header': 'Value'},
                                 text="{'test': 123}",
                                 ok=True)

        requests_response.json.return_value = {'test': 123}

        response = RestClient.Response(requests_response)
        self.assertEqual(response.status_code, requests_response.status_code)
        self.assertEqual(response.headers, requests_response.headers)
        self.assertEqual(response.body, requests_response.text)
        self.assertEqual(response.ok, requests_response.ok)
        self.assertEqual(response.json, requests_response.json())

    def test_generate_telesign_headers_with_post(self):
        method_name = 'POST'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 GMT'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'
        body_params_url_encoded = 'test=param'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         '2xVlmbrxLjYrrPun3G3WMNG6Jon4yKcTeOoK9DjXJ/Q=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.api_key,
                                                              method_name,
                                                              resource,
                                                              body_params_url_encoded,
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])

    def test_generate_telesign_headers_unicode_content(self):
        method_name = 'POST'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 GMT'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'
        body_params_url_encoded = 'test=%CF%BF'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         'h8d4I0RTxErbxYXuzCOtNqb/f0w3Ck8e5SEkGNj01+8=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.api_key,
                                                              method_name,
                                                              resource,
                                                              body_params_url_encoded,
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])

    def test_generate_telesign_headers_with_get(self):
        method_name = 'GET'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 GMT'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         'aUm7I+9GKl3ww7PNeeJntCT0iS7b+EmRKEE4LnRzChQ=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.api_key,
                                                              method_name,
                                                              resource,
                                                              '',
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])

    def test_generate_telesign_headers_default_date_and_nonce(self):
        method_name = 'GET'
        resource = '/v1/resource'

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.api_key,
                                                              method_name,
                                                              resource,
                                                              '',
                                                              user_agent='unit_test')

        self.assertFalse(parsedate_tz(actual_headers.get('Date')) is None)

        try:
            UUID(actual_headers.get('x-ts-nonce'))
        except (TypeError, ValueError):
            self.fail("x-ts-nonce is not a UUID")

    @patch('telesign.rest.RestClient.generate_telesign_headers', return_value={})
    def test_post(self, mock_generate_telesign_headers):
        test_host = 'https://test.com'
        test_resource = '/test/resource'
        test_params = {'test': '123_\u03ff_test'}

        client = RestClient(self.customer_id, self.api_key, rest_endpoint=test_host)
        client.session.post = Mock()

        expected_post_args = (u'https://test.com/test/resource',)
        expected_post_kwargs = {'headers': {}, 'data': 'test=123_%CF%BF_test', 'timeout': client.timeout}

        client.post(test_resource, **test_params)

        self.assertEqual(client.session.post.call_count, 1, "client.session.post not called")

        post_args, post_kwargs = client.session.post.call_args
        self.assertEqual(post_args, expected_post_args,
                         "client.session.post.call_args args do not match expected")
        self.assertEqual(post_kwargs, expected_post_kwargs,
                         "client.session.post.call_args kwargs do not match expected")

    @patch('telesign.rest.RestClient.generate_telesign_headers', return_value={})
    def test_get(self, mock_generate_telesign_headers):
        test_host = 'https://test.com'
        test_resource = '/test/resource'
        test_params = {'test': '123_\u03ff_test'}

        client = RestClient(self.customer_id, self.api_key, rest_endpoint=test_host)
        client.session.get = Mock()

        expected_get_args = (u'https://test.com/test/resource',)
        expected_get_kwargs = {'headers': {}, 'data': 'test=123_%CF%BF_test', 'timeout': client.timeout}

        client.get(test_resource, **test_params)

        self.assertEqual(client.session.get.call_count, 1, "client.session.get not called")

        get_args, get_kwargs = client.session.get.call_args
        self.assertEqual(get_args, expected_get_args,
                         "client.session.get.call_args args do not match expected")
        self.assertEqual(get_kwargs, expected_get_kwargs,
                         "client.session.get.call_args kwargs do not match expected")

    @patch('telesign.rest.RestClient.generate_telesign_headers', return_value={})
    def test_put(self, mock_generate_telesign_headers):
        test_host = 'https://test.com'
        test_resource = '/test/resource'
        test_params = {'test': '123_\u03ff_test'}

        client = RestClient(self.customer_id, self.api_key, rest_endpoint=test_host)
        client.session.put = Mock()

        expected_put_args = (u'https://test.com/test/resource',)
        expected_put_kwargs = {'headers': {}, 'data': 'test=123_%CF%BF_test', 'timeout': client.timeout}

        client.put(test_resource, **test_params)

        self.assertEqual(client.session.put.call_count, 1, "client.session.put not called")

        put_args, put_kwargs = client.session.put.call_args
        self.assertEqual(put_args, expected_put_args,
                         "client.session.put.call_args args do not match expected")
        self.assertEqual(put_kwargs, expected_put_kwargs,
                         "client.session.put.call_args kwargs do not match expected")

    @patch('telesign.rest.RestClient.generate_telesign_headers', return_value={})
    def test_delete(self, mock_generate_telesign_headers):
        test_host = 'https://test.com'
        test_resource = '/test/resource'
        test_params = {'test': '123_\u03ff_test'}

        client = RestClient(self.customer_id, self.api_key, rest_endpoint=test_host)
        client.session.delete = Mock()

        expected_delete_args = (u'https://test.com/test/resource',)
        expected_delete_kwargs = {'headers': {}, 'data': 'test=123_%CF%BF_test', 'timeout': client.timeout}

        client.delete(test_resource, **test_params)

        self.assertEqual(client.session.delete.call_count, 1, "client.session.delete not called")

        delete_args, delete_kwargs = client.session.delete.call_args
        self.assertEqual(delete_args, expected_delete_args,
                         "client.session.delete.call_args args do not match expected")
        self.assertEqual(delete_kwargs, expected_delete_kwargs,
                         "client.session.delete.call_args kwargs do not match expected")
