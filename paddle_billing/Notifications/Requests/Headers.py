from typing import Protocol


class Headers(Protocol):
    def get(self, key: str, default=None) -> str | None: ...
