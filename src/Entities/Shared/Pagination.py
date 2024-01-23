from __future__  import annotations
from dataclasses import dataclass


@dataclass
class Pagination:
    perPage:        int
    next:           str
    hasMore:        bool
    estimatedTotal: int


    @staticmethod
    def from_dict(data: dict) -> Pagination:
        return Pagination(
            perPage        = data['perPage'],
            next           = data['next'],
            hasMore        = data['hasMore'],
            estimatedTotal = data['estimatedTotal'],
        )
