from paddle_billing.ResponseParser import ResponseParser

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient
    from paddle_billing.Entities.Collections import Collection
    from paddle_billing.Entities.Shared import Pagination


class AsyncPaginator:
    def __init__(self, client: "AsyncClient", pagination: "Pagination", mapper):
        self._client = client
        self._pagination = pagination
        self._mapper = mapper

    @property
    def has_more(self) -> bool:
        return self._pagination.has_more

    async def next_page(self) -> "Collection":  # type: ignore
        response = await self._client.get_raw(self._pagination.next)
        response_parser = ResponseParser(response)

        return self._mapper.from_list(
            response_parser.get_data(), AsyncPaginator(self._client, response_parser.get_pagination(), self._mapper)
        )
