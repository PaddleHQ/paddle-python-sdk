from __future__  import annotations
from dataclasses import dataclass
from typing      import Union, Any


@dataclass
class Data:
    data: Union[dict, list, Any]  # JSON serializable Python types

    # from_dict method isn't needed, unless specific processing of 'data' is required.
