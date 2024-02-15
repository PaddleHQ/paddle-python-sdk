from logging import getLogger
from os      import getenv
from sys     import exit  # You should use classes/functions that return instead of exit

from paddle_billing import Client, Environment, Options

from paddle_billing.Exceptions.ApiError                        import ApiError
from paddle_billing.Exceptions.SdkExceptions.MalformedResponse import MalformedResponse

log = getLogger('my_app')

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
paddle = Client(api_key, options=Options(paddle_environment), logger=log)

products = None
try:
    products = paddle.products.list()
except (ApiError, MalformedResponse) as error:
    log.error(error)
    # Your additional logic that can handle Paddle's hints about what went wrong
except Exception as error:
    log.error(f"We received an error listing products: {error}")

if not products:
    print("There was an error trying to list products")
    exit(1)
if not len(products.items):
    log.warning("There are no products to list, have you created one?")
    print("There are no products to list")
    exit(0)

# No need to specifically iterate products.items, products itself is iterable
for product in products:
    print(f"Product's id: {product.id}")
    # Your additional logic for using each product
