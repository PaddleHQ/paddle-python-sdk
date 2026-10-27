from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class RootAuthType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApiKey: "RootAuthType" = "api_key"
    Oauth: "RootAuthType" = "oauth"
    ClientToken: "RootAuthType" = "client_token"
    Session: "RootAuthType" = "session"
