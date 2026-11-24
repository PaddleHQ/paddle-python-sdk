from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser
from paddle_billing.Entities.Collections import EventCollection as EventCollection, Paginator as Paginator
from paddle_billing.Resources.Events.Operations import ListEvents as ListEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class EventsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def list(self, operation: ListEvents | None = None) -> EventCollection:
        if operation is None:
            operation = ListEvents()

        self.response = self.client.get_raw("/events", operation.get_parameters())
        parser = ResponseParser(self.response)

        return EventCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), EventCollection)
        )
