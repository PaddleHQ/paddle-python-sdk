from enum import StrEnum


class Environment(StrEnum):
    PRODUCTION = 'production'
    SANDBOX    = 'sandbox'


    def base_url(self):
        return {
            'production': 'https://api.paddle.com',
            'sandbox':    'https://sandbox-api.paddle.com',
        }[self.value]
