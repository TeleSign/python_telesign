import unittest
import mock
import telesign.api
import uuid 


class AuthTest(unittest.TestCase):
    '''Test for phone id telesign sdk'''

    def setUp(self):
        self.expected_cid = "99999999-1F7E-11E1-B760-000000000000"
        self.expected_secret_key = "8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M=="
        self.expected_resource = "/foo/bar/baz/"

    def tearDown(self):
        pass

    def test_headers_are_set_on_get(self):
        telesign.api.generate_auth_headers(
            self.expected_cid,
            self.expected_secret_key,
            self.expected_resource,
            "GET")

    @mock.patch.object(uuid, "uuid4")
    def test_nonce_is_set(self, random_mock):
        expected_nonce = "1234"
        random_mock.return_value = expected_nonce
        headers = telesign.api.generate_auth_headers(
                self.expected_cid,
                self.expected_secret_key,
                self.expected_resource,
                "GET")

        self.assertEqual(headers["x-ts-nonce"], expected_nonce, "Nonce header did not match")

    def test_date_is_set(self):
        headers = telesign.api.generate_auth_headers(
                self.expected_cid,
                self.expected_secret_key,
                self.expected_resource,
                "GET")

        # Can't mock datetime
        self.assertIsNotNone(headers["x-ts-date"])

    def test_sha1__default_auth_method(self):
        expected_auth_method = "HMAC-SHA256"

        headers = telesign.api.generate_auth_headers(
                self.expected_cid,
                self.expected_secret_key,
                self.expected_resource,
                "GET")

        self.assertEqual(headers["x-ts-auth-method"], expected_auth_method, "Auth method did not match")

    def test_sha256_auth_method(self):
        expected_auth_method = "HMAC-SHA256"
        headers = telesign.api.generate_auth_headers(
                self.expected_cid,
                self.expected_secret_key,
                self.expected_resource,
                "GET",
                "",
                "sha256")

        self.assertEqual(headers["x-ts-auth-method"], expected_auth_method, "Auth method did not match")

    def test_customer_id_in_auth(self):
        expected_auth_start = "TSA %s:" % self.expected_cid
        headers = telesign.api.generate_auth_headers(
                self.expected_cid,
                self.expected_secret_key,
                self.expected_resource,
                "GET")

        self.assertTrue(headers["Authorization"].startswith(expected_auth_start), "Authorization did not start with TSA and customer ID")
