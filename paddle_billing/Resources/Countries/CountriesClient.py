from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import Paginator, CountryDefinitionCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class CountriesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self) -> CountryDefinitionCollection:
        self.response = self.client.get_raw("/countries")
        parser = ResponseParser(self.response)

        return CountryDefinitionCollection.from_list(
            parser.get_list(), Paginator(self.client, parser.get_pagination(), CountryDefinitionCollection)
        )
