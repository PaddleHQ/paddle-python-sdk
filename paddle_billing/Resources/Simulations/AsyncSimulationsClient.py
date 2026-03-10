# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Simulations/SimulationsClient.py
# Regenerate with: python scripts/generate_async_clients.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Simulation import Simulation
from paddle_billing.Entities.Collections import SimulationCollection
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

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SimulationCollection)
            )
        return await self.client._get("/simulations", operation.get_parameters(), parse)

    async def get(self, simulation_id: str) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return await self.client._get(f"/simulations/{simulation_id}", None, parse)

    async def create(self, operation: CreateSimulation) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return await self.client._post("/simulations", operation, parse)

    async def update(self, simulation_id: str, operation: UpdateSimulation) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return await self.client._patch(f"/simulations/{simulation_id}", operation, parse)
