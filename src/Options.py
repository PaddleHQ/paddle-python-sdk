from src.Environment import Environment


class Options:
    def __init__(self, environment=Environment.PRODUCTION, retries=1):
        self.environment = environment
        self.retries     = retries
