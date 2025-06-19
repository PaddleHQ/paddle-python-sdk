from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

from paddle_billing.Entities.Simulation import SimulationScenarioType


@dataclass
class SimulationConfigCreate(ABC):
    @staticmethod
    @abstractmethod
    def get_simulation_type() -> SimulationScenarioType:
        pass
