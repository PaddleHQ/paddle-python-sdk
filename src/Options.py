from __future__   import annotations
from .Environment import Environment
from dataclasses  import dataclass


@dataclass
class Options:
    environment: Environment = Environment.PRODUCTION
    retries:     int         = 1
