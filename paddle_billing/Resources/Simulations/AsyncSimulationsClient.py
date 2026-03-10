from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Simulation import Simulation
from paddle_billing.Entities.Collections import AsyncPaginator, SimulationCollection

from paddle_billing.Resources.Simulations.Operations import CreateSimulation, ListSimulations, UpdateSimulation

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncSimulationsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListSimulations | None = None) -> SimulationCollection:
        if operation is None:
            operation = ListSimulations()

        self.response = await self.client.get_raw("/simulations", operation.get_parameters())
        parser = ResponseParser(self.response)

        return SimulationCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), SimulationCollection)
        )

    async def get(self, simulation_id: str) -> Simulation:
        self.response = await self.client.get_raw(f"/simulations/{simulation_id}")
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_dict())

    async def create(self, operation: CreateSimulation) -> Simulation:
        self.response = await self.client.post_raw("/simulations", operation)
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_dict())

    async def update(self, simulation_id: str, operation: UpdateSimulation) -> Simulation:
        self.response = await self.client.patch_raw(f"/simulations/{simulation_id}", operation)
        parser = ResponseParser(self.response)

        return Simulation.from_dict(parser.get_dict())
