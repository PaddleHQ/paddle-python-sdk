from os import getenv

from paddle_billing import Client, Environment, Options

from paddle_billing.Resources.Events.Operations import ListEvents
from paddle_billing.Resources.Shared.Operations import Pager


# Verify your Paddle API key was provided by a PADDLE_SECRET_API_KEY environment variable
# It is strongly advised that you do not include secrets in your source code
# Use environment variables, and/or secrets management like Vault to obtain your secrets
api_key: str = getenv('PADDLE_SECRET_API_KEY', None)
if not api_key:
    raise ValueError("You must provide the PADDLE_API_KEY in your environment variables")

# Determine the environment, defaulting to sandbox
environment = getenv('PADDLE_ENVIRONMENT', 'sandbox')
paddle_environment = getattr(Environment, environment)  # E.g. Environment.sandbox

# Initialize the Paddle client
paddle = Client(api_key, options=Options(paddle_environment))

# Placeholder for the last processed event ID
last_processed_event_id = 'evt_01hfxx8t6ek9h399srcrp36jt3'

try:
    # List events starting after the last processed event ID
    events = paddle.events.list(ListEvents(Pager(after=last_processed_event_id)))
except Exception as e:
    # Handle any exceptions
    raise Exception(f"Error: {e}")

for event in events:
    # Update the last processed event ID
    last_processed_event_id = event.event_id
    print(f"event: {event.event_id}\t\t Type: {event.event_type.value:28}\t\t Occurred At: {event.occurred_at.format()}")

# Here you're up-to-date, you'd keep a record of where you got to...
