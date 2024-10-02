from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetting: "TaxMode" = "account_setting"
    External: "TaxMode" = "external"
    Internal: "TaxMode" = "internal"
