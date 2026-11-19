from collections.abc import Mapping
from functools import cached_property

from paddle_billing.Entities.Notifications import NotificationEvent
from paddle_billing.Notifications import Secret, Verifier
from paddle_billing.Notifications.Requests import BodyRequest, ContentRequest, DataRequest, Request
from paddle_billing.Notifications.Requests.Headers import Headers


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


class CustomRequest:
    def __init__(self) -> None:
        self.headers = {"Paddle-Signature": "ts=1;h1=abc"}
        self.body = b"{}"


class ProtocolRequest(Request):
    def __init__(self) -> None:
        self.body: bytes | None = b"{}"
        self.content: bytes | None = None
        self.data: bytes | None = None
        self.headers: Headers = {}


def handle(request: Request | BodyRequest | ContentRequest | DataRequest) -> None:
    if Verifier(10).verify(request, Secret("WEBHOOK_SECRET_KEY")):
        print(NotificationEvent.from_request(request).event_type)


handle(DjangoLikeRequest())
handle(FlaskLikeRequest())
handle(HttpxLikeRequest())
handle(CustomRequest())
handle(ProtocolRequest())
