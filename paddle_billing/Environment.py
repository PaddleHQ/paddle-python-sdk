from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class Environment(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    PRODUCTION: "Environment" = member("production")
    SANDBOX: "Environment" = member("sandbox")

    @property
    def base_url(self) -> str:
        return {
            "production": "https://api.paddle.com",
            "sandbox": "https://sandbox-api.paddle.com",
        }[self.value]
