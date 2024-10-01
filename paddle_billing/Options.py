from __future__ import annotations
from dataclasses import dataclass, field

from paddle_billing.Environment import Environment


@dataclass
class Options:
    environment: Environment = field(default_factory=lambda: Environment.PRODUCTION)
    retries: int = 1
