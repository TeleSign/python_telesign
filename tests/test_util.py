from __future__ import unicode_literals

from datetime import datetime

import pytest
from pytz import UTC

import telesign.util as util


@pytest.fixture
def credentials():
    return {
        "customer_id": "FFFFFFFF-EEEE-DDDD-1234-AB1234567890",
        "api_key": "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    }


def test_to_utc_rfc3339():
    utc_rfc3339 = util.to_utc_rfc3339(datetime.fromtimestamp(1493146971.0, tz=UTC))

    assert (
        utc_rfc3339 == "2017-04-25T19:02:51+00:00Z"
    ), "utc_rfc3339 format is not correct"


def test_random_with_n_digits():
    random_with_5_digits = util.random_with_n_digits(5)
    random_with_3_digits = util.random_with_n_digits(3)

    assert random_with_5_digits.isdigit(), "random_with_5_digits is not digits"
    assert (
        len(random_with_5_digits) == 5
    ), "random_with_5_digits is not requested length"
    assert (
        len(random_with_3_digits) == 3
    ), "random_with_3_digits is not requested length"


def test_verify_telesign_callback_signature_correct(credentials):
    signature = "B97g3N9lPdVaptvifxRau7bzVAC5hhRBZ6HKXABN744="
    json_str = "{'test': 123}"

    assert util.verify_telesign_callback_signature(
        credentials["api_key"], signature, json_str
    )


def test_verify_telesign_callback_signature_incorrect(credentials):
    incorrect_signature = "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB="
    json_str = "{'test': 123}"

    assert not util.verify_telesign_callback_signature(
        credentials["api_key"], incorrect_signature, json_str
    )
