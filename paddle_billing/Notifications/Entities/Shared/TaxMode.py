from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class TaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    AccountSetting: "TaxMode" = member("account_setting")
    External: "TaxMode" = member("external")
    Internal: "TaxMode" = member("internal")
    Location: "TaxMode" = member("location")
