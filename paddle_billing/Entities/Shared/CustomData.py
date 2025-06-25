from typing import Any


class CustomData:
    data: dict[str, Any] | list[Any]  # JSON serializable Python types

    def __init__(self, data: dict[str, Any] | list[Any]):
        self.data = data

    def to_json(self):
        return self.data
