from paddle_billing.PaddleStrEnum import PaddleStrEnum


class Environment(PaddleStrEnum):
    PRODUCTION = 'production'
    SANDBOX    = 'sandbox'


    @property
    def base_url(self) -> str:
        return {
            'production': 'https://api.paddle.com',
            'sandbox':    'https://sandbox-api.paddle.com',
        }[self.value]
