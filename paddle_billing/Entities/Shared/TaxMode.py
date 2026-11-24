from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class TaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetting: "TaxMode" = member("account_setting")
    External: "TaxMode" = member("external")
    Internal: "TaxMode" = member("internal")
    Location: "TaxMode" = member("location")
