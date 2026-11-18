from collections.abc import Mapping
from functools import cached_property

from paddle_billing.Entities.Notifications import NotificationEvent
from paddle_billing.Notifications import Secret, Verifier


class DjangoLikeRequest:
    @property
    def body(self) -> bytes:
        return b"{}"

    @cached_property
    def headers(self) -> Mapping[str, str]:
        return {}


class FlaskLikeRequest:
    def __init__(self) -> None:
        self.headers: Mapping[str, str] = {}

    @property
    def data(self) -> bytes:
        return b"{}"


class HttpxLikeRequest:
    def __init__(self) -> None:
        self.headers: dict[str, str] = {}
        self.content = b"{}"


verifier = Verifier(10)
for request in (DjangoLikeRequest(), FlaskLikeRequest(), HttpxLikeRequest()):
    if verifier.verify(request, Secret("WEBHOOK_SECRET_KEY")):
        print(NotificationEvent.from_request(request).event_type)
