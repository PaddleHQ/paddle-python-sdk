from logging import getLogger
from os import getenv
from sys import exit  # You should use classes/functions that returns instead of exits

from paddle_billing import Client, Environment, Options

from paddle_billing.Entities.Shared import (
    Action,
    AdjustmentType,
)

from paddle_billing.Exceptions.ApiError import ApiError

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustment, CreateAdjustmentItem

log = getLogger("my_app")

# Verify your Paddle API key was provided by a PADDLE_SECRET_API_KEY environment variable
# It is strongly advised that you do not include secrets in your source code
# Use environment variables, and/or secrets management like Vault to obtain your secrets
api_key: str = getenv("PADDLE_SECRET_API_KEY", None)
if not api_key:
    raise ValueError("You must provide the PADDLE_SECRET_API_KEY in your environment variables")

transaction_id: str = getenv("PADDLE_TRANSACTION_ID", None)
transaction_item_id: str = getenv("PADDLE_TRANSACTION_ITEM_ID", None)
full_adjustment_transaction_id: str = getenv("PADDLE_FULL_ADJUSTMENT_TRANSACTION_ID", None)

# Determine the environment, defaulting to sandbox
environment = Environment(getenv("PADDLE_ENVIRONMENT", "sandbox"))

# Initialize the Paddle client
paddle = Client(api_key, options=Options(environment), logger=log)


# ┌───
# │ Create Partial Adjustment │
# └───────────────────────────┘
try:
    partial_adjustment = paddle.adjustments.create(
        CreateAdjustment.partial(
            Action.Refund,
            [CreateAdjustmentItem(transaction_item_id, AdjustmentType.Partial, "100")],
            "error",
            transaction_id,
        )
    )
except ApiError as error:
    print(error)
    exit(1)

print(f"Partial Adjustment '{partial_adjustment.id}'")

# ┌───
# │ Create Full Adjustment │
# └────────────────────────┘
try:
    full_adjustment = paddle.adjustments.create(
        CreateAdjustment.full(
            Action.Refund,
            "error",
            full_adjustment_transaction_id,
        )
    )
except ApiError as error:
    print(error)
    exit(1)

print(f"Full Adjustment '{full_adjustment.id}'")
