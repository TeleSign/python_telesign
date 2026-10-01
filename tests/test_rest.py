from __future__ import unicode_literals

import requests
import pytest

from email.utils import parsedate_tz
from uuid import UUID
from unittest.mock import Mock, patch

from telesign.rest import RestClient
from telesign.util import AuthMethod


@pytest.fixture
def customer_id():
    return "FFFFFFFF-EEEE-DDDD-1234-AB1234567890"


@pytest.fixture
def api_key():
    return "EXAMPLE----TE8sTgg45yusumoN6BYsBVkh+yRJ5czgsnCehZaOYldPJdmFh6NeX8kunZ2zU1YWaUw/0wV6xfw=="


@pytest.fixture
def rest_endpoint():
    return "https://rest-api.telesign.com"


@pytest.fixture
def rest_client(customer_id, api_key):
    return RestClient(customer_id, api_key)


def test_rest_client_constructor_basic(rest_client, customer_id, api_key):
    assert rest_client.customer_id == customer_id
    assert rest_client.api_key == api_key


def test_rest_client_response_constructor_basic():
    requests_response = Mock(
        status_code=200,
        headers={"Header": "Value"},
        text="{'test': 123}",
        ok=True,
    )

    requests_response.json.return_value = {"test": 123}

    response = RestClient.Response(requests_response)

    assert response.status_code == requests_response.status_code
    assert response.headers == requests_response.headers
    assert response.body == requests_response.text
    assert response.ok == requests_response.ok
    assert response.json == requests_response.json()


def test_rest_client_response_constructor_from_full_service(
    customer_id,
    api_key,
    rest_endpoint,
):
    client = RestClient(
        customer_id,
        api_key,
        rest_endpoint,
        "python_telesign_enterprise",
        "1.0.0",
        "2.0.0",
    )

    assert "OriginatingSDK/python_telesign_enterprise" in client.user_agent
    assert "SDKVersion/1.0.0" in client.user_agent
    assert "DependencySDKVersion/2.0.0" in client.user_agent


def test_generate_telesign_headers_with_post(customer_id, api_key):
    expected_authorization_header = (
        "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:"
        "2xVlmbrxLjYrrPun3G3WMNG6Jon4yKcTeOoK9DjXJ/Q="
    )

    actual_headers = RestClient.generate_telesign_headers(
        customer_id,
        api_key,
        "POST",
        "/v1/resource",
        "test=param",
        date_rfc2616="Wed, 14 Dec 2016 18:20:12 GMT",
        nonce="A1592C6F-E384-4CDB-BC42-C3AB970369E9",
        user_agent="unit_test",
    )

    assert actual_headers["Authorization"] == expected_authorization_header


def test_generate_telesign_headers_unicode_content(customer_id, api_key):
    expected_authorization_header = (
        "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:"
        "h8d4I0RTxErbxYXuzCOtNqb/f0w3Ck8e5SEkGNj01+8="
    )

    actual_headers = RestClient.generate_telesign_headers(
        customer_id,
        api_key,
        "POST",
        "/v1/resource",
        "test=%CF%BF",
        date_rfc2616="Wed, 14 Dec 2016 18:20:12 GMT",
        nonce="A1592C6F-E384-4CDB-BC42-C3AB970369E9",
        user_agent="unit_test",
    )

    assert actual_headers["Authorization"] == expected_authorization_header


def test_generate_telesign_headers_with_get(customer_id, api_key):
    expected_authorization_header = (
        "TSA FFFFFFFF-EEEE-DDDD-1234-AB1234567890:"
        "aUm7I+9GKl3ww7PNeeJntCT0iS7b+EmRKEE4LnRzChQ="
    )

    actual_headers = RestClient.generate_telesign_headers(
        customer_id,
        api_key,
        "GET",
        "/v1/resource",
        "",
        date_rfc2616="Wed, 14 Dec 2016 18:20:12 GMT",
        nonce="A1592C6F-E384-4CDB-BC42-C3AB970369E9",
        user_agent="unit_test",
    )

    assert actual_headers["Authorization"] == expected_authorization_header


def test_generate_telesign_headers_with_post_basic_authentication(
    customer_id,
    api_key,
):
    expected_authorization_header = (
        "Basic RkZGRkZGRkYtRUVFRS1ERERELTEyMzQtQUIxMjM"
        "0NTY3ODkwOkVYQU1QTEUtLS0tVEU4c1RnZzQ1eXVzdW1vTjZCWXNCVmto"
        "K3lSSjVjemdzbkNlaFphT1lsZFBKZG1GaDZOZVg4a3VuWjJ6VTFZV2FV"
        "dy8wd1Y2eGZ3PT0="
    )

    actual_headers = RestClient.generate_telesign_headers(
        customer_id,
        api_key,
        "POST",
        "/v1/resource",
        "",
        date_rfc2616="Wed, 14 Dec 2016 18:20:12 GMT",
        nonce="A1592C6F-E384-4CDB-BC42-C3AB970369E9",
        user_agent="unit_test",
        auth_method=AuthMethod.BASIC.value,
    )

    assert actual_headers["Authorization"] == expected_authorization_header


def test_generate_telesign_headers_default_date_and_nonce(
    customer_id,
    api_key,
):
    headers = RestClient.generate_telesign_headers(
        customer_id,
        api_key,
        "GET",
        "/v1/resource",
        "",
        user_agent="unit_test",
    )

    assert parsedate_tz(headers.get("Date")) is not None

    UUID(headers.get("x-ts-nonce"))


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_post(mock_headers, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")
    client.session.post = Mock()

    client.post("/test/resource", test="123_\u03ff_test")

    client.session.post.assert_called_once()

    args, kwargs = client.session.post.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "data": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_post_body(mock_headers, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")
    client.session.post = Mock()

    params = {"test": "123_\u03ff_test"}

    client.post("/test/resource", body=params)

    client.session.post.assert_called_once()

    args, kwargs = client.session.post.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "json": params,
        "timeout": client.timeout,
    }


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_get(mock_headers, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")
    client.session.get = Mock()

    client.get("/test/resource", test="123_\u03ff_test")

    client.session.get.assert_called_once()

    args, kwargs = client.session.get.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "params": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_put(mock_headers, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")
    client.session.put = Mock()

    client.put("/test/resource", test="123_\u03ff_test")

    client.session.put.assert_called_once()

    args, kwargs = client.session.put.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "data": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_delete(mock_headers, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")
    client.session.delete = Mock()

    client.delete("/test/resource", test="123_\u03ff_test")

    client.session.delete.assert_called_once()

    args, kwargs = client.session.delete.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "params": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


@patch("requests.Session.patch")
@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_patch(mock_headers, mock_patch, customer_id, api_key):
    client = RestClient(customer_id, api_key, rest_endpoint="https://test.com")

    client.patch("/test/resource", test="123_\u03ff_test")

    client.session.patch.assert_called_once()

    args, kwargs = client.session.patch.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "params": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


@patch("time.time")
def test_create_session(mock_time, customer_id, api_key):
    mock_time.return_value = 1000

    client = RestClient(customer_id, api_key)

    assert client.session is not None
    assert client._session_created_at == 1000
    assert isinstance(client.session, requests.Session)


@patch("time.time")
def test_ensure_session(mock_time, customer_id, api_key):
    mock_time.return_value = 1000

    client = RestClient(
        customer_id,
        api_key,
        pool_recycle=10,
    )

    initial_session = client.session
    initial_created_at = client._session_created_at

    mock_time.return_value = 1012

    client._ensure_session()

    assert client.session is not initial_session
    assert client._session_created_at != initial_created_at


@patch("telesign.rest.RestClient.generate_telesign_headers", return_value={})
def test_post_basic_auth(mock_headers, customer_id, api_key):
    client = RestClient(
        customer_id,
        api_key,
        rest_endpoint="https://test.com",
        auth_method=AuthMethod.BASIC.value,
    )

    client.session.post = Mock()

    client.post("/test/resource", test="123_\u03ff_test")

    client.session.post.assert_called_once()

    args, kwargs = client.session.post.call_args

    assert args == ("https://test.com/test/resource",)
    assert kwargs == {
        "headers": {},
        "data": "test=123_%CF%BF_test",
        "timeout": client.timeout,
    }


def test_session_adapter_is_httpadapter(customer_id, api_key):
    client = RestClient(customer_id, api_key)

    https_adapter = client.session.adapters["https://"]

    assert isinstance(
        https_adapter,
        requests.adapters.HTTPAdapter,
    )


@patch("time.time")
def test_session_refresh_on_pool_recycle(
    mock_time,
    customer_id,
    api_key,
):
    mock_time.return_value = 1000

    client = RestClient(
        customer_id,
        api_key,
        pool_recycle=10,
    )

    created_at_first = client._session_created_at

    mock_time.return_value = 1012

    client._ensure_session()

    created_at_second = client._session_created_at

    assert created_at_first != created_at_second
