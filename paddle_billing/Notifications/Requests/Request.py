from typing import Any, Protocol, Union


# Read-only members and an untyped headers object let framework requests match: Django exposes body and
# cached headers, Flask data, httpx and requests content.
class RequestWithBody(Protocol):
    @property
    def body(self) -> bytes: ...

    @property
    def headers(self) -> Any: ...


class RequestWithContent(Protocol):
    @property
    def content(self) -> bytes: ...

    @property
    def headers(self) -> Any: ...


class RequestWithData(Protocol):
    @property
    def data(self) -> bytes: ...

    @property
    def headers(self) -> Any: ...


Request = Union[RequestWithBody, RequestWithContent, RequestWithData]
