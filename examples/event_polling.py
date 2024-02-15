from logging import getLogger
from os      import getenv
from sys     import exit  # You should use classes/functions that return instead of exit

from paddle_billing import Client, Environment, Options

from paddle_billing.Exceptions.ApiError                        import ApiError
from paddle_billing.Exceptions.SdkExceptions.MalformedResponse import MalformedResponse

from paddle_billing.Resources.Events.Operations import ListEvents
from paddle_billing.Resources.Shared.Operations import Pager

log = getLogger('my_app')

# Verify your Paddle API key was provided by a PADDLE_SECRET_API_KEY environment variable
# It is strongly advised that you do not include secrets in your source code
# Use environment variables, and/or secrets management like Vault to obtain your secrets
api_key: str = getenv('PADDLE_SECRET_API_KEY', None)
if not api_key:
    raise ValueError("You must provide the PADDLE_SECRET_API_KEY in your environment variables")

# Determine the environment, defaulting to sandbox
environment        = getenv('PADDLE_ENVIRONMENT', 'sandbox')
paddle_environment = getattr(Environment, environment)  # E.g. Environment.sandbox

# Initialize the Paddle client
paddle = Client(api_key, options=Options(paddle_environment), logger=log)

# Placeholder for the last processed event ID
last_processed_event_id = 'evt_01hfxx8t6ek9h399srcrp36jt3'

events = None
try:
    # List events starting after the last processed event ID
    events = paddle.events.list(ListEvents(Pager(after=last_processed_event_id)))
except (ApiError, MalformedResponse) as error:
    log.error(error)
    # Your additional logic that can handle Paddle's hints about what went wrong
except Exception as error:
    log.error(f"We received an error listing events: {error}")

if not events:
    print("There was an error trying to list events")
    exit(1)
if not len(events.items):
    log.warning("There are no events to list")
    print("There are no products to list")
    exit(0)

for event in events:
    last_processed_event_id = event.event_id  # Update the last processed event ID
    print(f"event: {event.event_id}\t\t Type: {event.event_type.value:28}\t\t Occurred At: {event.occurred_at.format()}")
    # Your additional logic for using each event

# Now you're up-to-date, you should keep a record of the last processed event...
# db.save(db_events.update({last_processed_event_id=last_processed_event_id})
