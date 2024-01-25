from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client                     import Client
    from paddle_billing_python_sdk.Entities.Collections       import Collection
    from paddle_billing_python_sdk.Entities.Shared.Pagination import Pagination


class Paginator:
    def __init__(self, client: 'Client', pagination: 'Pagination', mapper: 'Collection'):
        self._client     = client
        self._pagination = pagination
        self._mapper     = mapper


    def has_more(self) -> bool:
        return self._pagination.has_more


    def next_page(self):
        response        = self._client.get_raw(self._pagination.next)
        response_parser = ResponseParser(response)

        return self._mapper.from_array(
            response_parser.get_data(),
            Paginator(self._client, response_parser.get_pagination(), self._mapper)
        )
