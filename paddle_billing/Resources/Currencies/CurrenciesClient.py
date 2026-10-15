from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import Paginator, CurrencyDefinitionCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CurrenciesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self) -> CurrencyDefinitionCollection:
        self.response = self.client.get_raw("/currencies")
        parser = ResponseParser(self.response)

        return CurrencyDefinitionCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), CurrencyDefinitionCollection)
        )
