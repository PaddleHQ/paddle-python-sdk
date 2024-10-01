class CustomData:
    data: dict | list  # JSON serializable Python types

    def __init__(self, data: dict | list):
        self.data = data

    def get_parameters(self):
        return self.data

    def to_json(self):
        return self.data
