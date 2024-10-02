from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class Environment(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PRODUCTION: "Environment" = "production"
    SANDBOX: "Environment" = "sandbox"

    @property
    def base_url(self) -> str:
        return {
            "production": "https://api.paddle.com",
            "sandbox": "https://sandbox-api.paddle.com",
        }[self.value]
