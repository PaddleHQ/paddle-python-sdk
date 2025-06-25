from __future__ import annotations
from typing import Protocol, Any


class EntityDict(Protocol):
    def to_dict(self) -> dict[str, Any]: ...
