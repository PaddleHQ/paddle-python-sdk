from os import getenv
from pytest import fixture
from requests_mock import Mocker
from logging import Logger

from paddle_billing import Client, Environment, Options


class TestClient:
    def __init__(
        self,
        client: Client | None = None,
        api_secret_key: str | None = None,
        environment: Environment = Environment.SANDBOX,
        logger: Logger | None = None,
        timeout: float | None = None,
    ):
        self._environment = environment
        self._base_url = self._environment.base_url
        self._client = client or self.create_client(api_secret_key, logger, timeout)

    @property
    def client(self):
        return self._client

    @property
    def base_url(self):
        return self._base_url

    @property
    def environment(self):
        return self._environment

    def create_client(self, api_secret_key: str | None = None, logger: Logger | None = None, timeout=None):
        config = {
            "api_key": getenv("PADDLE_API_SECRET_KEY") if api_secret_key is None else api_secret_key,
            "options": Options(self._environment),
            "logger": logger,
        }

        if timeout is not None:
            config["timeout"] = timeout

        return Client(**config)


@fixture(autouse=True)
def test_client(test_logger):
    return TestClient(environment=Environment.SANDBOX, logger=test_logger)


@fixture
def mock_requests():
    with Mocker() as m:
        yield m
