from __future__ import annotations


class OrderBy:
    def __init__(self, field: str, direction: str):
        self.field     = field
        self.direction = direction


    @classmethod
    def id_ascending(cls) -> OrderBy:
        return OrderBy('id', 'asc')


    @classmethod
    def id_descending(cls) -> OrderBy:
        return OrderBy('id', 'desc')


    def __str__(self):
        return f"{self.field}[{self.direction}]"
