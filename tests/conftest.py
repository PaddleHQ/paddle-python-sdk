import pytest
import httpx
from paddle_billing_python_sdk.Environment import Environment


@pytest.fixture(scope="session")
def http_client():
    return httpx.Client(base_url=Environment.SANDBOX.base_url)
