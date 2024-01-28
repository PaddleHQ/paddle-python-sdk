from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Collections.EventCollection import EventCollection
from paddle_billing_python_sdk.Entities.Collections.Paginator       import Paginator

from paddle_billing_python_sdk.Resources.Events.Operations.ListEvents import ListEvents


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class EventsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListEvents = None) -> EventCollection:
        if operation is None:
            operation = ListEvents()

        self.response = self.client.get_raw('/events', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return EventCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), EventCollection)
        )
