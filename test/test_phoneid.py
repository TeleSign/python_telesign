import unittest
import mock
import telesign.api
import requests


class PhoneIdTest(unittest.TestCase):
    '''Test for phone id telesign sdk'''

    def setUp(self):
        self.expected_cid = "99999999-1F7E-11E1-B760-000000000000"
        self.expected_secret_key = "8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M=="
        self.expected_phone_no = "12343455678"
        self.expected_data = "{ \"a\": \"AA\", \"b\":\"BB\" }"
        self.expected_resource = "https://rest.telesign.com/v1/phoneid/%s/%s"
        self.proxy = "localhost:8080"
        self.expected_proxy = "https://localhost:8080"

    def tearDown(self):
        pass

    @mock.patch.object(requests, "get")
    def test_standard_phoneid(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)
        p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('standard', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_standard_phoneid_unauthorized(self, req_mock):
        response = mock.Mock()
        response.reason = "Unauthorized"
        response.status_code = 401
        response.text = "{ \"a\": \"AA\", \"b\":\"BB\", \"errors\": { \"code\": \"401\", \"description\":\"Unauthorized\" } }"
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)

        with self.assertRaises(telesign.exceptions.AuthorizationError):
            p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('standard', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_standard_phoneid_other_error(self, req_mock):
        response = mock.Mock()
        response.reason = "Bad Gateway"
        response.status_code = 502
        response.text = "{ \"a\": \"AA\", \"b\":\"BB\", \"errors\": { \"code\": \"502\", \"description\":\"Bad Gateway\" } }"
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)

        with self.assertRaises(telesign.exceptions.TelesignError):
            p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('standard', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_score_phoneid(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)
        p.score(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('score', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_contact_phoneid(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)
        p.contact(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args

        self.assertEqual(kwargs["url"], self.expected_resource % ('contact', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_live_phoneid(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)
        p.live(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('live', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_standard_phoneid_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('standard', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "get")
    def test_score_phoneid_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.score(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('score', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "get")
    def test_contact_phoneid_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.contact(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('contact', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "get")
    def test_live_phoneid_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.live(self.expected_phone_no, 'OTHR')

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_resource % ('live', self.expected_phone_no), "Phone ID resource name is incorrect")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")
