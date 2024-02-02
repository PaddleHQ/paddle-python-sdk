from paddle_billing.ResponseParser       import ResponseParser

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client               import Client
    from paddle_billing.Entities.Collections import Collection
    from paddle_billing.Entities.Shared      import Pagination


class Paginator:
    def __init__(self, client: 'Client', pagination: 'Pagination', mapper):
        self._client     = client
        self._pagination = pagination
        self._mapper     = mapper


    @property
    def has_more(self) -> bool:
        return self._pagination.has_more


    def next_page(self) -> 'Collection':
        response        = self._client.get_raw(self._pagination.next)
        response_parser = ResponseParser(response)

        return self._mapper.from_list(
            response_parser.get_data(),
            Paginator(self._client, response_parser.get_pagination(), self._mapper)
        )
