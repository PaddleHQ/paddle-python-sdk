from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventCollection
from paddle_billing.Resources.Events.Operations import ListEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class EventsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListEvents | None = None) -> EventCollection:
        if operation is None:
            operation = ListEvents()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return EventCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), EventCollection)
            )
        return self.client._get("/events", operation.get_parameters(), parse)
