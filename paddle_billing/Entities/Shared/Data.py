from dataclasses import dataclass
from typing import Any


@dataclass
class Data:
    data: dict[str, Any] | list[Any] | Any  # TODO Any? Should be JSON serializable Python types though

    # from_dict method isn't needed, unless specific processing of 'data' is required.
