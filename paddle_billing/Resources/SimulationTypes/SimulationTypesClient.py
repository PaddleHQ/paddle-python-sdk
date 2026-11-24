from requests import Response

from paddle_billing.ResponseParser import ResponseParser as ResponseParser
from paddle_billing.Entities.Collections import SimulationTypeCollection as SimulationTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationTypesClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response: Response | None = None

    def list(self) -> SimulationTypeCollection:
        self.response = self.client.get_raw("/simulation-types")
        parser = ResponseParser(self.response)

        return SimulationTypeCollection.from_list(parser.get_list())
