import logging

from os             import getenv
from paddle_billing import Client, Environment, Options


# Verify your Paddle API key was provided by a PADDLE_SECRET_API_KEY environment variable
# It is strongly advised that you do not include secrets in your source code
# Use environment variables, and/or secrets management like Vault to obtain your secrets
api_key = getenv('PADDLE_SECRET_API_KEY', None)
if not api_key:
    raise ValueError("You must provide the PADDLE_SECRET_API_KEY in your environment variables")

# Determine the environment, defaulting to sandbox
environment        = getenv('PADDLE_ENVIRONMENT', 'sandbox')
paddle_environment = getattr(Environment, environment)  # E.g. Environment.sandbox

# Initialize the Paddle client
paddle = Client(
    api_key,
    options = Options(paddle_environment),
    logger  = logging.getLogger('my_app'),
)

# Set up logging to standard output
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
paddle.log.addHandler(stdout_handler)

# List products
paddle.products.list()
