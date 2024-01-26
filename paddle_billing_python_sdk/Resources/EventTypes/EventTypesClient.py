from typing      import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Collections.Paginator           import Paginator
from paddle_billing_python_sdk.Entities.Collections.EventTypeCollection import EventTypeCollection


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class EventTypesClient:
    def __init__(self, client: 'Client'):
        self.client = client


    def list(self) -> EventTypeCollection:
        response = self.client.get_raw('/event-types')
        parser   = ResponseParser(response)

        return EventTypeCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), EventTypeCollection)
        )
