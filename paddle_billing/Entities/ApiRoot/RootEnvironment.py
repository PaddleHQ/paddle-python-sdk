from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class RootEnvironment(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Production: "RootEnvironment" = "production"
    Sandbox: "RootEnvironment" = "sandbox"
