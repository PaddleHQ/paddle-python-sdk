from __future__  import annotations
from dataclasses import dataclass

from paddle_billing.Entities.Shared.Pagination import Pagination


@dataclass
class MetaPaginated:
    request_id: str
    pagination: Pagination


    @staticmethod
    def from_dict(data: dict) -> MetaPaginated:
        return MetaPaginated(
            request_id = data['request_id'],
            pagination = Pagination.from_dict(data['pagination']),
        )
