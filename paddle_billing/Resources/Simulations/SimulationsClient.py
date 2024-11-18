from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Simulation import Simulation
from paddle_billing.Entities.Collections import Paginator, SimulationCollection
from paddle_billing.Resources.Simulations.Operations import CreateSimulation, ListSimulations, UpdateSimulation

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListSimulations = None) -> SimulationCollection:
        if operation is None:
            operation = ListSimulations()

        self.response = self.client.get_raw("/simulations", operation.get_parameters())
        parser = ResponseParser(self.response)

        return SimulationCollection.from_list(
            parser.get_data(), Paginator(self.client, parser.get_pagination(), SimulationCollection)
        )

    def get(self, simulation_id: str) -> Simulation:
        self.response = self.client.get_raw(f"/simulations/{simulation_id}")
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_data())

    def create(self, operation: CreateSimulation) -> Simulation:
        self.response = self.client.post_raw("/simulations", operation)
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_data())

    def update(self, simulation_id: str, operation: UpdateSimulation) -> Simulation:
        self.response = self.client.patch_raw(f"/simulations/{simulation_id}", operation)
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_data())
