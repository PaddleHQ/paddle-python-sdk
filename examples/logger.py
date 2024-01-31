import logging
from os             import getenv
from paddle_billing import Client, Environment, Options


# Verify your Paddle API key was provided
api_key = getenv('PADDLE_SECRET_API_KEY', None)
if not api_key:
    raise ValueError("You must provide the PADDLE_API_KEY in your environment variables")

# Determine the environment, defaulting to sandbox
paddle_environment = getattr(Environment, getenv('PADDLE_ENVIRONMENT', 'sandbox'))

# Initialize the Paddle client
paddle = Client(
    api_key,
    options = Options(paddle_environment),
    logger  = logging.getLogger('test_logger'),
)

# Set up logging to standard output
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
paddle.log.addHandler(stdout_handler)

# List products
paddle.products.list()
