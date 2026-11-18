from typing import Any, Protocol, Union


class Request(Protocol):
    @property
    def headers(self) -> Any: ...


# Read-only members and an untyped headers object let framework requests match: Django exposes body and
# cached headers, Flask data, httpx and requests content.
class RequestWithBody(Request, Protocol):
    @property
    def body(self) -> bytes: ...


class RequestWithContent(Request, Protocol):
    @property
    def content(self) -> bytes: ...


class RequestWithData(Request, Protocol):
    @property
    def data(self) -> bytes: ...


WebhookRequest = Union[RequestWithBody, RequestWithContent, RequestWithData]
