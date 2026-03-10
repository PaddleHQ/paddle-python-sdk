from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class EventTypesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self) -> EventTypeCollection:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return EventTypeCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), EventTypeCollection)
            )
        return self.client._get("/event-types", None, parse)
