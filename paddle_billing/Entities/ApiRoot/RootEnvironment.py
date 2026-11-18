from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class RootEnvironment(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Production: "RootEnvironment" = member("production")
    Sandbox: "RootEnvironment" = member("sandbox")
