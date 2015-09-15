import unittest
import mock
import telesign.api
import telesign.exceptions


class ExceptionTestTest(unittest.TestCase):
    '''Test for exceptions in telesign sdk'''

    def setUp(self):
        self.expected_errors = [{"code": 1, "description": "Error 1"}, {"code": 2, "description": "Error 2"}]
        self.expected_headers = {"a": "AA", "b": "BB"}
        self.expected_status = "200"
        self.expected_data = "abcdefg"
        self.expected_raw = "oh foo"
        
        self.expected_http_response = mock.Mock()
        self.expected_http_response.headers = self.expected_headers
        self.expected_http_response.status_code = self.expected_status
        self.expected_http_response.text = self.expected_data
        self.expected_http_response.raw = self.expected_raw 

    def tearDown(self):
        pass

    def __validate_exception_properties(self, x):
            self.assertEqual(x.errors, self.expected_errors, "Errors property was not set on exception")
            self.assertEqual(x.headers, self.expected_headers, "Headers property was not set on exception")
            self.assertEqual(x.status, self.expected_status, "Status property was not set on exception")
            self.assertEqual(x.data, self.expected_data, "Data property was not set on exception")
            self.assertEqual(x.raw, self.expected_raw, "RawData property was not set on exception")

            msg = x.__str__()
            for err in self.expected_errors:
                self.assertTrue(err["description"] in msg)

    def test_properties_are_populated_in_TelesignError(self):
        try:
            raise telesign.exceptions.TelesignError({"errors": self.expected_errors}, self.expected_http_response)
        except telesign.exceptions.TelesignError as x:
            self.__validate_exception_properties(x)

    def test_properties_are_populated_in_AuthorizationError(self):
        try:
            raise telesign.exceptions.AuthorizationError({"errors": self.expected_errors}, self.expected_http_response)
        except telesign.exceptions.AuthorizationError as x:
            self.__validate_exception_properties(x)

    def test_properties_are_populated_in_ValidationError(self):
        try:
            raise telesign.exceptions.ValidationError({"errors": self.expected_errors}, self.expected_http_response)
        except telesign.exceptions.ValidationError as x:
            self.__validate_exception_properties(x)
