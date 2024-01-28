import pytest
import requests_mock
from os import environ

from paddle_billing_python_sdk.Client      import Client
from paddle_billing_python_sdk.Environment import Environment
from paddle_billing_python_sdk.Options     import Options


class TestClient:
    def __init__(
        self,
        client:         Client | None = None,
        api_secret_key: str    | None = None,
        base_url:       str           = Environment.SANDBOX.base_url,
     ):
        self._client   = client or self.create_client(api_secret_key)
        self._base_url = base_url


    @property
    def client(self):
        return self._client

    @property
    def base_url(self):
        return self._base_url


    @staticmethod
    def create_client(api_secret_key: str | None = None):
        return Client(
            api_key = environ.get('PADDLE_API_SECRET_KEY') if api_secret_key is None else api_secret_key,
            options = Options(Environment.SANDBOX),
        )


@pytest.fixture(autouse=True)
def setup_test_client():
    return TestClient()


@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m
