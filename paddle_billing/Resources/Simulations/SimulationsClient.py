from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Simulation import Simulation
from paddle_billing.Entities.Collections import SimulationCollection
from paddle_billing.Resources.Simulations.Operations import CreateSimulation, ListSimulations, UpdateSimulation

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListSimulations | None = None) -> SimulationCollection:
        if operation is None:
            operation = ListSimulations()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SimulationCollection)
            )
        return self.client._get("/simulations", operation.get_parameters(), parse)

    def get(self, simulation_id: str) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/simulations/{simulation_id}", None, parse)

    def create(self, operation: CreateSimulation) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/simulations", operation, parse)

    def update(self, simulation_id: str, operation: UpdateSimulation) -> Simulation:
        def parse(response):
            self.response = response
            return Simulation.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/simulations/{simulation_id}", operation, parse)
