from __future__ import unicode_literals

import os
import pytest

from urllib.parse import quote
from unittest.mock import Mock, patch

from telesign.score import ScoreClient


@pytest.fixture
def customer_id():
    return os.getenv("CUSTOMER_ID", "FFFFFFFF-EEEE-DDDD-1234-AB1234567890")


@pytest.fixture
def api_key():
    return os.getenv(
        "API_KEY",
        "ABC12345yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw==",
    )


@pytest.fixture
def phone_number():
    return os.getenv("PHONE_NUMBER", "11234567890")


@pytest.fixture
def email_address():
    return os.getenv(
        "EMAIL_ADDRESS",
        "support@vero-finto.com",
    )


@pytest.fixture
def account_lifecycle_event():
    return "create"


@pytest.fixture
def score_client(customer_id, api_key):
    return ScoreClient(customer_id, api_key)


def test_score_method(
    score_client,
    phone_number,
    account_lifecycle_event,
):
    with patch("telesign.rest.requests.Session.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {
            "risk": {
                "level": "LOW",
                "recommendation": "allow",
            }
        }

        mock_post.return_value = mock_response

        response = score_client.score(
            phone_number,
            account_lifecycle_event,
        )

        mock_post.assert_called_once()

        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]
        called_data = called_kwargs.get("data", "")

        assert "/intelligence/phone" in called_url
        assert called_data

        assert f"phone_number={phone_number}" in called_data
        assert f"account_lifecycle_event={account_lifecycle_event}" in called_data

        assert response.status_code == 200
        assert response.ok
        assert response.headers.get("Content-Type") == "application/json"

        assert "risk" in response.json
        assert response.json["risk"]["level"] == "LOW"
        assert response.json["risk"]["recommendation"] == "allow"


def test_email_intelligence_method(
    score_client,
    email_address,
    account_lifecycle_event,
):
    with patch("telesign.rest.requests.Session.post") as mock_post:
        mock_response = Mock()
        mock_response.ok = True
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {
            "risk": {
                "level": "LOW",
                "recommendation": "allow",
            }
        }

        mock_post.return_value = mock_response

        response = score_client.email_intelligence(
            email_address,
            account_lifecycle_event,
        )

        mock_post.assert_called_once()

        called_url = mock_post.call_args[0][0]
        called_kwargs = mock_post.call_args[1]
        called_data = called_kwargs.get("data", "")

        assert "/intelligence/email" in called_url
        assert called_data

        assert f"email_address={quote(email_address)}" in called_data

        assert f"account_lifecycle_event={account_lifecycle_event}" in called_data

        assert response.status_code == 200
        assert response.ok
        assert response.headers.get("Content-Type") == "application/json"

        assert "risk" in response.json
        assert response.json["risk"]["level"] == "LOW"
        assert response.json["risk"]["recommendation"] == "allow"
