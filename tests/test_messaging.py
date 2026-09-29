from __future__ import unicode_literals

import json
import os
import pytest
from unittest.mock import Mock, patch

from telesign.messaging import MessagingClient


@pytest.fixture
def messaging_client():
    customer_id = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
    api_key = os.getenv(
        "API_KEY",
        "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    )
    return MessagingClient(customer_id, api_key)


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
    return os.getenv("PHONE_NUMBER", "phone_number")


def test_messaging_constructor(messaging_client, customer_id, api_key):
    assert messaging_client.customer_id == customer_id
    assert messaging_client.api_key == api_key


def test_messaging_message(messaging_client, phone_number):
    expected_response = {
        "reference_id": "0123456789ABCDEF0123456789ABCDEF",
        "external_id": None,
        "status": {"code": 290, "description": "Message in progress"},
    }

    with patch("telesign.rest.requests.Session.post") as mock_post:
        mock_response = Mock(
            status_code=200,
            headers={"Content-Type": "application/json"},
            ok=True,
            text=json.dumps(expected_response),
        )
        mock_response.json.return_value = expected_response
        mock_post.return_value = mock_response

        response = messaging_client.message(
            phone_number, "Hello, this is a test message!", "ARN"
        )

        mock_post.assert_called_once()

        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]

        assert "/v1/messaging" in called_url
        assert called_kwargs.get("data")

        assert response.headers.get("Content-Type") == "application/json"
        assert response.status_code == 200
        assert response.json == expected_response


def test_messaging_status(messaging_client):
    reference_id = "0123456789ABCDEF0123456789ABCDEF"

    expected_response = {
        "status": {
            "updated_on": "2026-05-29T17:38:49.049000Z",
            "code": 203,
            "description": "Delivered to gateway",
        },
        "reference_id": reference_id,
    }

    with patch("telesign.rest.requests.Session.get") as mock_get:
        mock_response = Mock(
            status_code=200,
            headers={"Content-Type": "application/json"},
            ok=True,
            text=json.dumps(expected_response),
        )
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = messaging_client.status(reference_id)

        mock_get.assert_called_once()

        called_url = mock_get.call_args[0][0]

        assert called_url.endswith(f"/v1/messaging/{reference_id}")
        assert response.headers.get("Content-Type") == "application/json"
        assert response.status_code == 200
        assert response.json == expected_response
