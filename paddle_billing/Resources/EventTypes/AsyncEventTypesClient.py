from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, EventTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncEventTypesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self) -> EventTypeCollection:
        self.response = await self.client.get_raw("/event-types")
        parser = ResponseParser(self.response)

        return EventTypeCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), EventTypeCollection)
        )
