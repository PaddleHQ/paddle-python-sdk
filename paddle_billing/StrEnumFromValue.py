from enum import Enum


class StrEnumFromValue(Enum):
    @classmethod
    def from_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No enum found for value: {value}")
