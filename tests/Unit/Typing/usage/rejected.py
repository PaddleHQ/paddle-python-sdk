from paddle_billing import Client
from paddle_billing.Notifications import Secret, Verifier


class RequestWithoutBody:
    headers: dict[str, str] = {}


Client(123)
Verifier().verify(RequestWithoutBody(), Secret("WEBHOOK_SECRET_KEY"))
