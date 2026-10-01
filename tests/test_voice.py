from __future__ import unicode_literals

import json
import os

import pytest
from unittest.mock import patch, Mock

from telesign.voice import VoiceClient


@pytest.fixture
def voice_client():
    customer_id = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
    api_key = os.getenv(
        "API_KEY",
        "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    )

    return VoiceClient(customer_id, api_key)


@pytest.fixture
def phone_number():
    return os.getenv("PHONE_NUMBER", "phone_number")


def test_voice_constructor(voice_client):
    customer_id = os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")
    api_key = os.getenv(
        "API_KEY",
        "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    )

    assert voice_client.customer_id == customer_id
    assert voice_client.api_key == api_key


def test_voice_call(voice_client, phone_number):
    expected_response = {
        "reference_id": "0123456789ABCDEF0123456789ABCDEF",
        "external_id": None,
        "status": {
            "code": 130,
            "description": "Call blocked by TeleSign",
            "updated_on": "2026-05-29T21:09:19.378673Z",
        },
        "voice": {"caller_id": "+16268723943"},
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

        response = voice_client.call(
            phone_number, "Hello, this is a test message!", "ARN"
        )

        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1] if mock_post.call_args else {}
        called_data = called_kwargs.get("data", "")

        assert "/v1/voice" in called_url
        assert called_data, "POST data is empty, expected form parameters"
        assert (
            response.headers.get("Content-Type") == "application/json"
        ), "Content-Type args do not match expected"
        assert response.status_code == 200, "Status code args do not match expected"
        assert (
            response.json == expected_response
        ), "Response does not match expected mock response"


def test_voice_status(voice_client):
    expected_response = {
        "reference_id": "0123456789ABCDEF0123456789ABCDEF",
        "status": {
            "code": 100,
            "description": "Call answered",
            "updated_on": "2026-05-29T17:38:49.049000Z",
        },
    }

    with patch("telesign.rest.requests.Session.get") as mock_get:
        mock_response = Mock(
            status_code=201,
            headers={"Content-Type": "application/json"},
            ok=True,
            text=json.dumps(expected_response),
        )
        mock_response.json.return_value = expected_response
        mock_get.return_value = mock_response

        response = voice_client.status("0123456789ABCDEF0123456789ABCDEF")

        called_url = mock_get.call_args[0][0]

        assert "/v1/voice/0123456789ABCDEF0123456789ABCDEF" in called_url
        assert (
            response.headers.get("Content-Type") == "application/json"
        ), "Content-Type args do not match expected"
        assert response.status_code == 201, "Status code args do not match expected"
        assert (
            response.json == expected_response
        ), "Response does not match expected mock response"
