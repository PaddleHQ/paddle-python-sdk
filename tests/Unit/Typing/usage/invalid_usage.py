from paddle_billing import Client
from paddle_billing.Notifications import Secret, Verifier


class NoBodyRequest:
    def __init__(self) -> None:
        self.headers: dict[str, str] = {}


Client(123)
Verifier().verify(NoBodyRequest(), Secret("WEBHOOK_SECRET_KEY"))
