from __future__   import annotations
from dataclasses  import dataclass

from src.Environment import Environment


@dataclass
class Options:
    environment: Environment = Environment.PRODUCTION
    retries:     int         = 1
