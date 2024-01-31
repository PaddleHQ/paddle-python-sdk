from enum import StrEnum


class Environment(StrEnum):
    PRODUCTION = 'production'
    SANDBOX    = 'sandbox'


    @property
    def base_url(self) -> str:
        return {
            'production': 'https://api.paddle.com',
            'sandbox':    'https://sandbox-api.paddle.com',
        }[self.value]
