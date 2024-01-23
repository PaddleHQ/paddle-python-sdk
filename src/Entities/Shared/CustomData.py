from dataclasses import dataclass
from json        import dumps as json_dumps


@dataclass
class CustomData:
    data: dict  # or any other type that's JSON serializable

    def json_serialize(self):
        return json_dumps(self.data)  # serialize the data to a JSON string
