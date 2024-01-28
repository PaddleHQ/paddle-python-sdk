from dataclasses import dataclass


@dataclass
class CustomData:
    data: dict | list  # JSON serializable Python types


    def get_parameters(self):
        return self.data
