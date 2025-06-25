from dataclasses import dataclass
from typing import Any


@dataclass
class CustomData:
    data: dict[str, Any] | list[Any]  # JSON serializable Python types

    def to_json(self):
        return self.data
