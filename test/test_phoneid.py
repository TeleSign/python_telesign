import unittest
import mock
import telesign.api
import urllib3

class PhoneIdTest(unittest.TestCase):
    '''Test for phone id telesign sdk'''
    
    def setUp(self):
        self.expected_cid = "99999999-1F7E-11E1-B760-000000000000"
        self.expected_secret_key = "8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M8M=="
        self.expected_phone_no = "12343455678"
        self.expected_data = "{ \"a\": \"AA\", \"b\":\"BB\" }"
        self.expected_resource = "/v1/phoneid/standard/%s" % self.expected_phone_no
        
    def tearDown(self):
        pass

    @mock.patch.object(urllib3.HTTPConnectionPool, "request")
    def test_standard_phoneid(self, req_mock):
        response = mock.Mock()
        response.reason = ""
        response.status = 200
        response.data = self.expected_data
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)
        r = p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "GET", "Expected GET")
        self.assertEqual(args[0][1], self.expected_resource, "Phone ID resource name is incorrect")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request")
    def test_standard_phoneid_unauthorized(self, req_mock):
        response = mock.Mock()
        response.reason = "Unauthorized"
        response.status = 401
        response.data = "{ \"a\": \"AA\", \"b\":\"BB\", \"errors\": { \"code\": \"401\", \"description\":\"Unauthorized\" } }"
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)

        with self.assertRaises(telesign.exceptions.AuthorizationError):
            r = p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "GET", "Expected GET")
        self.assertEqual(args[0][1], self.expected_resource, "Phone ID resource name is incorrect")

    @mock.patch.object(urllib3.HTTPConnectionPool, "request")
    def test_standard_phoneid_other_error(self, req_mock):
        response = mock.Mock()
        response.reason = "Bad Gateway"
        response.status = 502
        response.data = "{ \"a\": \"AA\", \"b\":\"BB\", \"errors\": { \"code\": \"502\", \"description\":\"Bad Gateway\" } }"
        req_mock.return_value = response

        p = telesign.api.PhoneId(self.expected_cid, self.expected_secret_key)

        with self.assertRaises(telesign.exceptions.TelesignError):
            r = p.standard(self.expected_phone_no)

        self.assertTrue(req_mock.called)
        args = req_mock.call_args
        self.assertEqual(args[0][0], "GET", "Expected GET")
        self.assertEqual(args[0][1], self.expected_resource, "Phone ID resource name is incorrect")

