from dataclasses import dataclass
from json        import dumps as json_dumps
from typing      import Any


@dataclass
class CustomData:
    data: dict | list | Any  # JSON serializable Python types


    def json_serialize(self) -> str:
        return json_dumps(self.data)  # serialize the data to a JSON string
