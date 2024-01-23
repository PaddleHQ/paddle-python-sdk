from __future__  import annotations
from .Pagination import Pagination
from dataclasses import dataclass


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
