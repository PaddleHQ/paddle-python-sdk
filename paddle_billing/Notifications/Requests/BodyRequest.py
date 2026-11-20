from typing import Any, Protocol


class BodyRequest(Protocol):
    # Read-only so framework requests, which expose these as properties, match.
    # headers is Any because framework header types don't match a get() protocol in both mypy and pyright.
    @property
    def headers(self) -> Any: ...

    @property
    def body(self) -> bytes: ...
