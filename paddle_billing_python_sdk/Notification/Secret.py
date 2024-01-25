class Secret:
    def __init__(self, secret_key: str):
        self.__secret_key = secret_key


    @property
    def secret_key(self):
        return self.__secret_key
