from paddle_billing.ResponseParser       import ResponseParser
from paddle_billing.Entities.Collections import Paginator, EventTypeCollection

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from paddle_billing.Client import Client


class EventTypesClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self) -> EventTypeCollection:
        self.response = self.client.get_raw('/event-types')
        parser        = ResponseParser(self.response)

        return EventTypeCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), EventTypeCollection)
        )
