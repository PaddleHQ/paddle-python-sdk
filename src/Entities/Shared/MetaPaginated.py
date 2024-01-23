from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.Pagination import Pagination


@dataclass
class MetaPaginated:
    requestId:  str
    pagination: Pagination


    @staticmethod
    def from_dict(data: dict) -> MetaPaginated:
        return MetaPaginated(
            requestId  = data['requestId'],
            pagination = Pagination.from_dict(data['pagination']),
        )
