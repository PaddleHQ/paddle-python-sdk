from __future__ import annotations
from paddle_billing.Notifications.Entities.EntityDict import EntityDict


class UndefinedEntity(EntityDict):
    def __init__(
        self,
        data: dict,
    ):
        self._data = data

    def to_dict(self) -> dict:
        return self._data
