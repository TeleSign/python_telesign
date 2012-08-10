import unittest
import mock
import telesign.api
import urllib3

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
        self.expected_sms_resource = "/v1/verify/sms"
        self.expected_call_resource = "/v1/verify/call"
        self.expected_status_resource = "/v1/verify/%s" % self.expected_ref_id
        
    def tearDown(self):
        pass

    @mock.patch.object(urllib3.HTTPConnectionPool, "request_encode_body")
    def test_verify_sms(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.sms(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "POST", "Expected POST")
        self.assertEqual(args[0][1], self.expected_sms_resource, "Sms verify resource was incorrect")
        self.assertEqual(args[1]["fields"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(args[1]["fields"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(args[1]["fields"]["verify_code"], self.expected_verify_code, "Verify code field did not match")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request_encode_body")
    def test_verify_call(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.call(self.expected_phone_no, self.expected_verify_code, self.expected_language)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "POST", "Expected POST")
        self.assertEqual(args[0][1], self.expected_call_resource, "Call verify resource was incorrect")
        self.assertEqual(args[1]["fields"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(args[1]["fields"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(args[1]["fields"]["verify_code"], self.expected_verify_code, "Verify code field did not match")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request_encode_body")
    def test_verify_sms_default_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.sms(self.expected_phone_no, language=self.expected_language)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "POST", "Expected POST")
        self.assertEqual(args[0][1], self.expected_sms_resource, "Sms verify resource was incorrect")
        self.assertEqual(args[1]["fields"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(args[1]["fields"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(len("%s" % args[1]["fields"]["verify_code"]), 5, "Expected default verify code to be 5 digits")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request_encode_body")
    def test_verify_call_default_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.call(self.expected_phone_no, language=self.expected_language)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "POST", "Expected POST")
        self.assertEqual(args[0][1], self.expected_call_resource, "Call verify resource was incorrect")
        self.assertEqual(args[1]["fields"]["phone_number"], self.expected_phone_no, "Phone number field did not match")
        self.assertEqual(args[1]["fields"]["language"], self.expected_language, "Language field did not match")
        self.assertEqual(len("%s" % args[1]["fields"]["verify_code"]), 5, "Expected default verify code to be 5 digits")     

    @mock.patch.object(urllib3.HTTPConnectionPool, "request")
    def test_status_check(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.status(self.expected_ref_id)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "GET", "Expected GET")
        self.assertEqual(args[0][1], self.expected_status_resource, "Status resource was incorrect")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request")
    def test_report_code(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.Verify(self.expected_cid, self.expected_secret_key)
        r = p.status(self.expected_ref_id, self.expected_verify_code)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "GET", "Expected GET")
        self.assertEqual(args[0][1], self.expected_status_resource, "Status resource was incorrect")
        self.assertEqual(args[1]["fields"]["verify_code"], self.expected_verify_code, "Verify code did not match")
        