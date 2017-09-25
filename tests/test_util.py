from __future__ import unicode_literals

from datetime import datetime
from unittest import TestCase

from pytz import UTC

import telesign.util as util


class TestRest(TestCase):
    def setUp(self):
        self.customer_id = "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"
        self.api_key = "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="

    def test_to_utc_rfc3339(self):
        utc_rfc3339 = util.to_utc_rfc3339(datetime.fromtimestamp(1493146971.0, tz=UTC))

        self.assertEqual(utc_rfc3339,
                         '2017-04-25T19:02:51+00:00Z',
                         "utc_rfc3339 format is not correct")

    def test_random_with_n_digits(self):
        random_with_5_digits = util.random_with_n_digits(5)
        random_with_3_digits = util.random_with_n_digits(3)

        self.assertTrue(random_with_5_digits.isdigit(), "random_with_5_digits is not digits")
        self.assertEqual(len(random_with_5_digits), 5, "random_with_5_digits is not requested length")
        self.assertEqual(len(random_with_3_digits), 3, "random_with_3_digits is not requested length")

    def test_verify_telesign_callback_signature_correct(self):
        signature = "B97g3N9lPdVaptvifxRau7bzVAC5hhRBZ6HKXABN744="
        json_str = "{'test': 123}"

        self.assertTrue(util.verify_telesign_callback_signature(self.api_key, signature, json_str))

    def test_verify_telesign_callback_signature_incorrect(self):
        incorrect_signature = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB="
        json_str = "{'test': 123}"

        self.assertFalse(util.verify_telesign_callback_signature(self.api_key, incorrect_signature, json_str))
