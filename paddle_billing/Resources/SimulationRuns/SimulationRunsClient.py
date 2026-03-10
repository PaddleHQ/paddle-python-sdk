from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRun import SimulationRun
from paddle_billing.Entities.Collections import SimulationRunCollection
from paddle_billing.Resources.SimulationRuns.Operations import GetSimulationRun, ListSimulationRuns

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.Client import Client


class SimulationRunsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, simulation_id: str, operation: ListSimulationRuns | None = None) -> SimulationRunCollection:
        if operation is None:
            operation = ListSimulationRuns()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return SimulationRunCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), SimulationRunCollection)
            )
        return self.client._get(f"/simulations/{simulation_id}/runs", operation, parse)

    def get(
        self, simulation_id: str, simulation_run_id: str, operation: GetSimulationRun | None = None
    ) -> SimulationRun:
        if operation is None:
            operation = GetSimulationRun()

        def parse(response):
            self.response = response
            return SimulationRun.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/simulations/{simulation_id}/runs/{simulation_run_id}", operation, parse)

    def create(self, simulation_id: str) -> SimulationRun:
        def parse(response):
            self.response = response
            return SimulationRun.from_dict(ResponseParser(response).get_dict())
        return self.client._post(f"/simulations/{simulation_id}/runs", None, parse)
