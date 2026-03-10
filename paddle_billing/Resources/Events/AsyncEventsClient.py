# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Events/EventsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return EventCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), EventCollection)
            )
        return await self.client._get("/events", operation.get_parameters(), parse)
