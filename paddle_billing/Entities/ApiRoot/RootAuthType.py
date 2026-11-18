from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class RootAuthType(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    ApiKey: "RootAuthType" = member("api_key")
    Oauth: "RootAuthType" = member("oauth")
    ClientToken: "RootAuthType" = member("client_token")
    Session: "RootAuthType" = member("session")
