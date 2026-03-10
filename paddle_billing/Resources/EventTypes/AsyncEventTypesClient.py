# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/EventTypes/EventTypesClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncEventTypesClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self) -> EventTypeCollection:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return EventTypeCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), EventTypeCollection)
            )
        return await self.client._get("/event-types", None, parse)
