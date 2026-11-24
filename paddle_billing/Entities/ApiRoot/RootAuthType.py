from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class RootAuthType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApiKey: "RootAuthType" = member("api_key")
    Oauth: "RootAuthType" = member("oauth")
    ClientToken: "RootAuthType" = member("client_token")
    Session: "RootAuthType" = member("session")
