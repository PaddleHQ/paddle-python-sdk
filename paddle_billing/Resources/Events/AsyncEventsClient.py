from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import AsyncPaginator, EventCollection
from paddle_billing.Resources.Events.Operations import ListEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncEventsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListEvents | None = None) -> EventCollection:
        if operation is None:
            operation = ListEvents()

        self.response = await self.client.get_raw("/events", operation.get_parameters())
        parser = ResponseParser(self.response)

        return EventCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), EventCollection)
        )
