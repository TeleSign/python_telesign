import unittest
import mock
import telesign.api
import requests


class VerifyTest(unittest.TestCase):
    '''Test for Verify telesign sdk'''

    def setUp(self):
        self.expected_cid = "99999999-1F7E-11E1-B760-000000000000"
        self.expected_secret_key = "8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M=="
        self.expected_phone_no = "12343455678"
        self.expected_language = "en"
        self.expected_verify_code = 54321
        self.expected_ref_id = "99999999999999999"
        self.expected_data = "{ \"a\": \"AA\", \"b\":\"BB\" }"
        self.expected_sms_resource = "https://rest.telesign.com/v1/verify/sms"
        self.expected_call_resource = "https://rest.telesign.com/v1/verify/call"
        self.expected_status_resource = "https://rest.telesign.com/v1/verify/%s" % self.expected_ref_id
        self.proxy = "localhost:8080"
        self.expected_proxy = "https://localhost:8080"

    def tearDown(self):
        pass

    @mock.patch.object(requests, "post")
    def test_verify_sms(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.sms(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs['url'], self.expected_sms_resource, "Sms verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(kwargs["data"]["verify_code"], self.expected_verify_code, "Verify code field did not match")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "post")
    def test_verify_call(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.call(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs['url'], self.expected_call_resource, "Call verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(kwargs["data"]["verify_code"], self.expected_verify_code, "Verify code field did not match")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "post")
    def test_verify_sms_default_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.sms(self.expected_phone_no, language=self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_sms_resource, "Sms verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "post")
    def test_verify_call_default_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.call(self.expected_phone_no, language=self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_call_resource, "Call verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_status_check(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.status(self.expected_ref_id)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_status_resource, "Status resource was incorrect")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "get")
    def test_report_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        p.status(self.expected_ref_id, self.expected_verify_code)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_status_resource, "Status resource was incorrect")
        self.assertEqual(kwargs["params"]["verify_code"], self.expected_verify_code, "Verify code did not match")
        self.assertFalse(kwargs['proxies'])

    @mock.patch.object(requests, "post")
    def test_verify_sms_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key, proxy_host="localhost:8080")
        p.sms(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs['url'], self.expected_sms_resource, "Sms verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(kwargs["data"]["verify_code"], self.expected_verify_code, "Verify code field did not match")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "post")
    def test_verify_call_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.call(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs['url'], self.expected_call_resource, "Call verify resource was incorrect")
        self.assertEqual(kwargs["data"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(kwargs["data"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(kwargs["data"]["verify_code"], self.expected_verify_code, "Verify code field did not match")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "get")
    def test_status_check_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.status(self.expected_ref_id)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_status_resource, "Status resource was incorrect")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

    @mock.patch.object(requests, "get")
    def test_report_code_with_proxy(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status_code = 200
        response.text = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key, proxy_host=self.proxy)
        p.status(self.expected_ref_id, self.expected_verify_code)

        self.assertTrue(req_mock.called)
        _, kwargs = req_mock.call_args
        self.assertEqual(kwargs["url"], self.expected_status_resource, "Status resource was incorrect")
        self.assertEqual(kwargs["params"]["verify_code"], self.expected_verify_code, "Verify code did not match")
        self.assertEqual(kwargs["proxies"]["https"], self.expected_proxy, "Proxy did not match")

