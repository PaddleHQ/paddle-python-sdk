from dataclasses import dataclass


@dataclass
class CustomData:
    data: dict | list  # JSON serializable Python types

    def to_json(self):
        return self.data
