from __future__ import unicode_literals
import os
import pytest

from telesign.phoneid import PhoneIdClient


@pytest.fixture
def customer_id():
    return os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")


@pytest.fixture
def api_key():
    return os.getenv(
        "API_KEY",
        "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    )


@pytest.fixture
def phone_number():
    return "11234567890"


@pytest.fixture
def phoneid_client(customer_id, api_key):
    return PhoneIdClient(customer_id, api_key)


def test_phoneid_constructor(phoneid_client, customer_id, api_key):
    assert phoneid_client.customer_id == customer_id
    assert phoneid_client.api_key == api_key


def test_phoneid_pid(phoneid_client, phone_number):
    content_type_expected = "application/json"
    status_code_expected = 200

    response = phoneid_client.phoneid(phone_number)

    assert response.headers.get("Content-Type") == content_type_expected
    assert response.status_code == status_code_expected
