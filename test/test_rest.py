from __future__ import unicode_literals

from unittest import TestCase

from telesign.rest import RestClient


class TestRest(TestCase):
    def setUp(self):
        self.customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
        self.secret_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

    def test_generate_telesign_headers_with_post(self):
        method_name = 'POST'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 -0000'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'
        body_params_url_encoded = 'test=param'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         'lA6VIW3840IUwp5QwYJtLgQHeXbV+KW89vv2GoKi+OY=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.secret_key,
                                                              method_name,
                                                              resource,
                                                              body_params_url_encoded,
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])

    def test_make_string_to_sign_with_post_unicode_content(self):
        method_name = 'POST'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 -0000'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'
        body_params_url_encoded = 'test=%CF%BF'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         'SbILhQhkgBFXokzXQOoraTypjLK2Bv2pK2TlSaRs5ZE=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.secret_key,
                                                              method_name,
                                                              resource,
                                                              body_params_url_encoded,
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])

    def test_make_string_to_sign_with_get(self):
        method_name = 'GET'
        date_rfc2616 = 'Wed, 14 Dec 2016 18:20:12 -0000'
        nonce = 'A1592C6F-E384-4CDB-BC42-C3AB970369E9'
        resource = '/v1/resource'

        expected_authorization_header = ('TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:'
                                         'vdUx5SPrVdyroKjSzC+gajBVdDL5pOLhiLx6ohI7r8w=')

        actual_headers = RestClient.generate_telesign_headers(self.customer_id,
                                                              self.secret_key,
                                                              method_name,
                                                              resource,
                                                              '',
                                                              date_rfc2616=date_rfc2616,
                                                              nonce=nonce,
                                                              user_agent='unit_test')

        self.assertEqual(expected_authorization_header, actual_headers['Authorization'])
