from dataclasses import dataclass
from json        import dumps as json_dumps
from typing      import Union, Any


@dataclass
class CustomData:
    data: Union[dict, list, Any]  # JSON serializable Python types


    def json_serialize(self):
        return json_dumps(self.data)  # serialize the data to a JSON string
