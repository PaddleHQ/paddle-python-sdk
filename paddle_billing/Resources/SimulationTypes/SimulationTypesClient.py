from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import SimulationTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationTypesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self) -> SimulationTypeCollection:
        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationTypeCollection.from_list(parser.get_list())
        return self.client._get("/simulation-types", None, parse)
