import pytest
from os import environ

from paddle_billing_python_sdk.Client      import Client
from paddle_billing_python_sdk.Environment import Environment
from paddle_billing_python_sdk.Options     import Options


@pytest.fixture(scope="session")
def init_client(api_secret_key: str = None):
    """Instantiates our client and configures it to use the Paddle sandbox environment"""

    return Client(
        api_key = environ.get('PADDLE_API_SECRET_KEY') if api_secret_key is None else api_secret_key,
        options = Options(Environment.SANDBOX),
    )
