from __future__ import annotations
from typing import Protocol


class EntityDict(Protocol):
    def to_dict(self) -> dict: ...
