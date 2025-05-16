from __future__ import annotations
from typing import Any
from paddle_billing.Notifications.Entities.EntityDict import EntityDict


class UndefinedEntity(EntityDict):
    def __init__(
        self,
        data: dict[Any, Any],
    ):
        self._data = data

    def to_dict(self) -> dict[Any, Any]:
        return self._data
