from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

from paddle_billing.Entities.Reports import ReportFilterOperator

from paddle_billing.Entities.Reports import ReportFilterName


@dataclass
class Filter(ABC):
    def to_json(self) -> dict[str, str | list[str] | ReportFilterName | ReportFilterOperator | None]:
        return {
            "name": self.get_name(),
            "operator": self.get_operator(),
            "value": self.get_value(),
        }

    @staticmethod
    @abstractmethod
    def get_name() -> ReportFilterName:
        pass

    @abstractmethod
    def get_value(self) -> str | list[str]:
        pass

    def get_operator(self) -> ReportFilterOperator | None:
        return None
